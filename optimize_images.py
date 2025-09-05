#!/usr/bin/env python3

import os
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from PIL import Image

def get_image_date(filepath):
    """Extrait la date de création depuis les métadonnées EXIF ou la date de modification"""
    try:
        if filepath.lower().endswith('.jpg'):
            img = Image.open(filepath)
            exif_data = img._getexif()
            if exif_data:
                from PIL.ExifTags import TAGS
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name in ['DateTimeOriginal', 'DateTime']:
                        return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except:
        pass
    
    if filepath.lower().endswith('.heic'):
        try:
            result = subprocess.run(['sips', '-g', 'creation', filepath], 
                                  capture_output=True, text=True)
            if 'creation' in result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if 'creation' in line:
                        date_str = line.split('creation:')[1].strip()
                        return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
        except:
            pass
    
    return datetime.fromtimestamp(os.path.getmtime(filepath))

def convert_heic_to_jpg(heic_path, output_path):
    """Convertit un fichier HEIC en JPG en utilisant sips (macOS)"""
    temp_jpg = output_path.replace('.jpg', '_temp.jpg')
    subprocess.run(['sips', '-s', 'format', 'jpeg', heic_path, '--out', temp_jpg], 
                   check=True, capture_output=True)
    return temp_jpg

def optimize_image(input_path, output_path, max_width=2000, quality=85):
    """Optimise une image pour le web"""
    img = Image.open(input_path)
    
    # Conserver l'orientation EXIF
    try:
        exif = img.info['exif']
    except:
        exif = None
    
    # Redimensionner si nécessaire
    if img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    
    # Convertir en RGB si nécessaire
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Sauvegarder avec optimisation
    if exif:
        img.save(output_path, 'JPEG', quality=quality, optimize=True, exif=exif)
    else:
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
    
    return output_path

def main():
    raw_dir = Path('photoRAW')
    output_dir = Path('assets/images/gallery')
    
    # Créer le dossier de sortie
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Collecter toutes les images avec leurs métadonnées
    images_info = []
    
    print("📸 Analyse des images...")
    for file in raw_dir.iterdir():
        if file.suffix.lower() in ['.jpg', '.jpeg', '.heic', '.png']:
            date = get_image_date(str(file))
            images_info.append({
                'original_name': file.name,
                'path': str(file),
                'date': date,
                'extension': file.suffix.lower()
            })
            print(f"  ✓ {file.name} - {date.strftime('%Y-%m-%d %H:%M')}")
    
    # Trier par date chronologique
    images_info.sort(key=lambda x: x['date'])
    
    print(f"\n🔄 Traitement de {len(images_info)} images...")
    
    # Traiter chaque image
    for i, img_info in enumerate(images_info, 1):
        # Nouveau nom basé sur l'ordre chronologique
        date_str = img_info['date'].strftime('%Y%m%d')
        new_name = f"camilo_{date_str}_{i:03d}.jpg"
        output_path = output_dir / new_name
        
        print(f"\n[{i}/{len(images_info)}] {img_info['original_name']}")
        print(f"  → {new_name}")
        
        try:
            # Convertir HEIC en JPG si nécessaire
            if img_info['extension'] == '.heic':
                print("  ⚙️  Conversion HEIC → JPG...")
                temp_jpg = convert_heic_to_jpg(img_info['path'], str(output_path))
                print("  ⚙️  Optimisation pour le web...")
                optimize_image(temp_jpg, str(output_path))
                os.remove(temp_jpg)
            else:
                print("  ⚙️  Optimisation pour le web...")
                optimize_image(img_info['path'], str(output_path))
            
            # Afficher la taille finale
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"  ✅ Sauvegardé ({size_mb:.1f} MB)")
            
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    print(f"\n✨ Terminé! {len(images_info)} images optimisées dans {output_dir}")
    
    # Créer un fichier index avec les informations
    index_path = output_dir / 'index.json'
    import json
    
    index_data = []
    for i, img_info in enumerate(images_info, 1):
        date_str = img_info['date'].strftime('%Y%m%d')
        new_name = f"camilo_{date_str}_{i:03d}.jpg"
        index_data.append({
            'filename': new_name,
            'original': img_info['original_name'],
            'date': img_info['date'].isoformat(),
            'order': i
        })
    
    with open(index_path, 'w') as f:
        json.dump(index_data, f, indent=2)
    
    print(f"📝 Index créé: {index_path}")

if __name__ == "__main__":
    main()
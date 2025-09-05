#!/usr/bin/env python3

import os
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from PIL import Image

def get_image_date(filepath):
    """Extrait la date de création depuis les métadonnées ou la date de modification"""
    try:
        if filepath.lower().endswith('.heic'):
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

def convert_heic_to_jpg(heic_path, temp_path):
    """Convertit HEIC en JPG temporaire"""
    subprocess.run(['sips', '-s', 'format', 'jpeg', heic_path, '--out', temp_path], 
                   check=True, capture_output=True)
    return temp_path

def optimize_for_mobile(input_path, output_path, max_width=800, quality=72):
    """Optimise pour mobile ultra-rapide"""
    img = Image.open(input_path)
    
    # Redimensionner si nécessaire
    if img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    
    # Convertir en RGB si nécessaire
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Sauvegarder avec compression mobile
    img.save(output_path, 'JPEG', quality=quality, optimize=True, progressive=True)
    
    return output_path

def main():
    source_dir = Path('photoRAW')  # Dossier des images sources HEIC
    gallery_dir = Path('assets/images/gallery')
    
    print("🎯 Remplacement des 20 images par les versions rognées optimisées\n")
    
    # Collecter les images HEIC rognées
    heic_files = []
    for file in source_dir.iterdir():
        if file.suffix.lower() in ['.heic']:
            date = get_image_date(str(file))
            heic_files.append({
                'path': str(file),
                'name': file.name,
                'date': date
            })
    
    # Trier par date chronologique
    heic_files.sort(key=lambda x: x['date'])
    
    # Limiter à 20 images
    heic_files = heic_files[:20]
    
    print(f"📸 {len(heic_files)} images rognées trouvées, triées par date\n")
    
    # Remplacer une par une
    for i, img_info in enumerate(heic_files, 1):
        oeuvre_name = f"OEUVRE{i}.jpg"
        output_path = gallery_dir / oeuvre_name
        temp_path = f"/tmp/temp_{i}.jpg"
        
        print(f"[{i:2d}/20] {img_info['name']}")
        print(f"         → {oeuvre_name}")
        
        try:
            # Convertir HEIC → JPG temporaire
            print("         ⚙️  Conversion HEIC → JPG...")
            convert_heic_to_jpg(img_info['path'], temp_path)
            
            # Optimiser pour mobile
            print("         📱 Optimisation mobile...")
            optimize_for_mobile(temp_path, str(output_path))
            
            # Taille finale
            size_kb = os.path.getsize(output_path) / 1024
            dimensions = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(output_path)], 
                                      capture_output=True, text=True)
            
            print(f"         ✅ Remplacé ({size_kb:.0f}KB)")
            
            # Nettoyer temp
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
        except Exception as e:
            print(f"         ❌ Erreur: {e}")
            if os.path.exists(temp_path):
                os.remove(temp_path)
        
        print()
    
    print("✨ Remplacement terminé! Images optimisées pour mobile 📱")

if __name__ == "__main__":
    main()
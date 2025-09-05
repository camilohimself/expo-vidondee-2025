# 📋 CLAUDE.md - Mémo Projet Expo Vidondée 2025

## 🎯 État Actuel du Projet

### Structure
- **20 pages œuvres** : `oeuvre1.html` à `oeuvre20.html` 
- **Images optimisées** : 87-184KB dans `assets/images/gallery/`
- **Format mobile** : 800px max, qualité 72%
- **Étiquettes impression** : `etiquettes-impression.html` avec QR codes

### 🖼️ Images
- **Images optimisées** : `assets/images/gallery/OEUVRE1-20.jpg` (87-184KB)
- **Images sources** : Stockées hors projet (dossier photoRAW/)
- **Format mobile** : 800px max, qualité 72% JPEG

## 💰 Prix Actuels (04/09/2025)

### Prix par dimensions
- **160×120 cm** : 
  - Abstrait 632 : 6'500 CHF
  - Abstrait 237 : 7'000 CHF
  
- **143×171 cm** :
  - Abstrait 143 : 6'500 CHF

- **120×120 cm** : 
  - Abstrait 55 : 6'000 CHF
  - Autres : 6'000 CHF (standard)

- **70×100 cm** : 
  - TOUS à 3'500 CHF (Abstrait 32, 55, 122, 90)

- **Autres formats** : Prix variables selon l'œuvre

## 🔧 Commandes Utiles

### Optimisation images
```bash
python3 replace_images.py  # Convertit et optimise les 20 images
```

### Git
```bash
git add -A
git commit -m "Message"
git push origin main
```

### Ouvrir localement
```bash
open etiquettes-impression.html  # Pour imprimer les étiquettes
open oeuvre1.html                # Pour tester une page
```

## 📝 TODO / En cours

- [x] Images optimisées pour mobile (90% réduction)
- [x] Prix mis à jour dans toutes les pages
- [x] Étiquettes avec QR codes prêtes pour impression
- [ ] Push GitHub en attente
- [ ] Configuration audio SoundCloud à finaliser
- [ ] Tests sur mobile réel

## ⚠️ Points d'Attention

1. **Deux Abstrait 55** différents :
   - 120×120 cm = 6'000 CHF (oeuvre13)
   - 70×100 cm = 3'500 CHF (oeuvre15)

2. **Images** : Utiliser UNIQUEMENT `gallery/OEUVRE*.jpg` (optimisées)

3. **Push GitHub** : Peut timeout, utiliser `run_in_background` si nécessaire

4. **Impression** : Toujours vérifier les prix dans `etiquettes-impression.html` avant impression

## 🚀 Prochaines Étapes

1. Finaliser configuration SoundCloud
2. Tester sur appareils mobiles réels
3. Déploiement sur Netlify
4. Tests QR codes in situ

---
*Dernière mise à jour : 04/09/2025 - 16h45*
# Compagnon Digital Exposition - Camilo Rivera

## 🎨 Concept

Ce projet crée un **compagnon digital d'exposition** où chaque œuvre physique a sa propre page web isolée. Les visiteurs scannent un QR code placé à côté de l'œuvre et accèdent à une expérience digitale enrichie de cette œuvre spécifiquement.

**Important** : Ce N'EST PAS un site portfolio classique. Chaque page est isolée - pas de navigation entre œuvres car les visiteurs sont physiquement dans l'exposition.

## 🚀 Structure du Projet

```
/
├── dialogue-interieur.html      # Page œuvre 1
├── composition-no7.html         # Page œuvre 2
├── traces-urbaines.html         # Page œuvre 3
├── assets/
│   ├── css/
│   │   └── style.css           # Styles partagés
│   ├── js/
│   │   └── qr-generator.js     # Logique QR & interactions
│   ├── audio/
│   │   ├── dialogue-interieur.mp3
│   │   ├── composition-no7.mp3
│   │   └── traces-urbaines.mp3
│   └── images/
│       ├── dialogue-interieur.jpg
│       ├── composition-no7.jpg
│       └── traces-urbaines.jpg
└── admin/
    └── generate-qr-codes.html  # Génération des QR codes
```

## ✨ Fonctionnalités

### Pour les visiteurs
- **Page isolée par œuvre** (pas de navigation)
- **Image haute qualité** avec lightbox
- **Audio SoundCloud** intégré (30-60 sec par œuvre)
- **Contact WhatsApp** direct pour le prix
- **Lien Instagram** @camiloriverart
- **QR code** auto-généré (pour partage)
- **100% mobile-first**

### Pour l'artiste
- **Admin simple** pour générer tous les QR codes
- **Système modulaire** : dupliquer une page = nouvelle œuvre
- **No-code** : juste changer texte, image, audio

## 📱 Expérience Utilisateur (1-2 min)

1. Visiteur devant une œuvre physique
2. Scanne le QR code
3. Arrive sur la page dédiée
4. Voit l'œuvre en haute qualité
5. Lit les informations techniques
6. Écoute l'artiste parler de cette œuvre
7. Peut contacter via WhatsApp pour le prix
8. Retourne à la contemplation physique

## 🛠️ Installation

### 1. Cloner le repository
```bash
git clone https://github.com/camilohimself/expo-vidondee-2025.git
cd expo-vidondee-2025
```

### 2. Ajouter vos contenus
```bash
# Placer vos images dans assets/images/
# Configurer SoundCloud (voir SOUNDCLOUD-SETUP.md)
# Modifier le numéro WhatsApp dans qr-generator.js
```

### 3. Hébergement
- Upload sur votre serveur web
- Ou utiliser GitHub Pages, Netlify, Vercel
- Aucune base de données requise

## ➕ Ajouter une Nouvelle Œuvre

### Méthode simple :
1. **Dupliquer** `dialogue-interieur.html`
2. **Renommer** `nouvelle-oeuvre.html`
3. **Modifier** dans le fichier :
   - Titre de la page (`<title>`)
   - Nom de l'œuvre (`<h1>`)
   - Description
   - Code œuvre (ex: CR-2025-XXX)
   - Chemins vers image et audio
   - Informations techniques

### Le QR code se génère automatiquement !

## 🎯 Configuration

### WhatsApp
Dans `assets/js/qr-generator.js`, ligne 45 :
```javascript
const phoneNumber = '+41794567890'; // Votre numéro
```

### URLs de production
Dans `admin/generate-qr-codes.html`, ligne 64 :
```javascript
const BASE_URL = 'https://votredomaine.com/';
```

## 📊 Génération des QR Codes

1. Ouvrir `admin/generate-qr-codes.html`
2. Vérifier que l'URL de base est correcte
3. Cliquer "Imprimer tous les QR codes"
4. Découper et placer à côté de chaque œuvre

## 🎨 Design

- **Fond noir** (#0a0a0a) - Ambiance galerie
- **Texte blanc cassé** (#f5f5f0)
- **Typography légère** (font-weight: 200-300)
- **L'œuvre est la star**, l'interface s'efface
- **Mobile-first** responsive

## 🔧 Personnalisation

### CSS
Modifier `assets/css/style.css` pour changer :
- Couleurs
- Typographie
- Animations
- Layout mobile

### JavaScript
Modifier `assets/js/qr-generator.js` pour :
- Changer les contacts
- Modifier les interactions
- Ajouter des analytics

## 🚫 Ce qui a été VOLONTAIREMENT retiré

- ❌ Navigation entre œuvres
- ❌ Menu principal
- ❌ Galerie globale
- ❌ Portfolio classique
- ❌ Swipe/flèches

**Pourquoi ?** Car l'expérience réelle se passe dans l'exposition physique !

## 🎪 Exposition

**Lieu** : La Vidondée, Riddes  
**Date** : Septembre 2025  
**Artiste** : Camilo Rivera  
**Instagram** : [@camiloriverart](https://instagram.com/camiloriverart)

---

*🤖 Système créé avec Claude Code*
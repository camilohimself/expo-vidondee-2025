# 🎵 Configuration SoundCloud

## Comment obtenir les URLs pour vos tracks

### 1. Uploader vos audios sur SoundCloud

1. Créer un compte SoundCloud (gratuit)
2. Upload vos audios de 30-60 secondes par œuvre
3. **Important** : Mettre en **PUBLIC** ou **UNLISTED** (pas privé)

### 2. Obtenir l'URL d'embed pour chaque track

**Méthode simple :**
1. Aller sur votre track SoundCloud
2. Cliquer sur **"Share"** sous le player
3. Cliquer sur **"Embed"** 
4. **Personnaliser l'embed :**
   - Décocher "Show related tracks"
   - Décocher "Show comments" 
   - Décocher "Show user"
   - Décocher "Enable automatic play"
5. Copier le code iframe généré

### 3. Remplacer dans vos pages HTML

Dans chaque page (dialogue-interieur.html, etc.), remplacez :
```html
src="https://w.soundcloud.com/player/?url=YOUR_SOUNDCLOUD_TRACK_URL&..."
```

Par l'URL de votre track, exemple :
```html
src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/camilorivera/dialogue-interieur&color=%23f5f5f0&auto_play=false&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false&visual=false"
```

## ⚙️ Paramètres optimisés pour l'exposition

L'embed est déjà configuré avec :
- `color=%23f5f5f0` → Couleur assortie au design
- `auto_play=false` → Pas de lecture automatique
- `hide_related=true` → Cache les suggestions
- `show_comments=false` → Cache les commentaires
- `show_user=false` → Cache le nom d'utilisateur
- `show_reposts=false` → Cache les reposts
- `visual=false` → Player compact sans waveform

## 🔄 Workflow simple

1. **Upload** → SoundCloud
2. **Share** → Embed → Personnaliser → Copier
3. **Coller** dans la page HTML
4. **Tester** l'iframe

## 💡 Tips

- **Nommer vos tracks** avec le nom de l'œuvre
- **Description courte** sur SoundCloud si besoin
- **Durée optimale** : 30-60 secondes max
- **Qualité** : MP3 128kbps minimum

## 🎯 Exemple concret

Si votre track est à l'adresse :
`https://soundcloud.com/camilorivera/dialogue-interieur`

L'URL encodée devient :
`https%3A//soundcloud.com/camilorivera/dialogue-interieur`

Et l'embed final :
```html
<iframe width="100%" height="166" 
        src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/camilorivera/dialogue-interieur&color=%23f5f5f0&auto_play=false&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false&visual=false"
        frameborder="0" 
        allow="autoplay">
</iframe>
```
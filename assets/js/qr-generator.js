// QR Code generation for admin and test pages only
function generateQRCode() {
    const currentUrl = window.location.href;
    const qrContainer = document.getElementById('qrcode');
    
    if (qrContainer && typeof QRCode !== 'undefined') {
        // Clear existing QR code
        qrContainer.innerHTML = '';
        
        // Generate new QR code
        const qr = new QRCode(qrContainer, {
            text: currentUrl,
            width: 150,
            height: 150,
            colorDark: '#000000',
            colorLight: '#ffffff',
            correctLevel: QRCode.CorrectLevel.M
        });
        
        // Display URL
        const urlDisplay = document.getElementById('currentUrl');
        if (urlDisplay) {
            // Create a cleaner display URL
            const displayUrl = currentUrl.replace(window.location.origin, 'expo.camilorivera.art');
            urlDisplay.textContent = displayUrl;
        }
    }
}

// Initialize QR code when page loads (only if QR container exists)
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('qrcode')) {
        setTimeout(generateQRCode, 100);
    }
});

// Lightbox functionality
function openLightbox() {
    const lightbox = document.getElementById('lightbox');
    if (lightbox) {
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    if (lightbox) {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Social media actions
function contactWhatsApp(artworkTitle = '') {
    const phoneNumber = '+41794567890'; // Remplacez par votre numéro
    const message = encodeURIComponent(`Bonjour Camilo, je suis intéressé(e) par l'œuvre "${artworkTitle}" que j'ai découverte lors de votre exposition. Pourriez-vous me donner plus d'informations ?`);
    const whatsappUrl = `https://wa.me/${phoneNumber}?text=${message}`;
    window.open(whatsappUrl, '_blank');
}

function openInstagram() {
    window.open('https://www.instagram.com/camiloriverart/', '_blank');
}

// Remove loader after page load
window.addEventListener('load', () => {
    setTimeout(() => {
        const loader = document.getElementById('loader');
        if (loader) {
            loader.classList.add('hidden');
        }
    }, 800);
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && document.getElementById('lightbox')?.classList.contains('active')) {
        closeLightbox();
    }
});

// Prevent context menu on images to protect artwork
document.addEventListener('contextmenu', function(e) {
    if (e.target.tagName === 'IMG') {
        e.preventDefault();
    }
});

// Disable right-click save on images
document.addEventListener('dragstart', function(e) {
    if (e.target.tagName === 'IMG') {
        e.preventDefault();
    }
});
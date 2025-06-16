// Attendre que le DOM (Document Object Model) soit entièrement chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', () => {
    // Sélectionner le bouton du menu burger par son ID
    const hamburgerButton = document.getElementById('hamburger-button');
    // Sélectionner le menu de navigation mobile par son ID
    const mobileMenu = document.getElementById('mobile-menu');

    // Ajouter un écouteur d'événements 'click' au bouton du menu burger
    hamburgerButton.addEventListener('click', () => {
        // Basculer la classe 'hidden' sur le menu mobile
        mobileMenu.classList.toggle('hidden');

        // Basculer la classe '-translate-x-full' et 'translate-x-0' sur le menu mobile
        // Cela gère l'animation de glissement du menu :
        // - '-translate-x-full' déplace le menu complètement hors de l'écran vers la gauche
        // - 'translate-x-0' ramène le menu à sa position d'origine (visible)
        mobileMenu.classList.toggle('-translate-x-full');
        mobileMenu.classList.toggle('translate-x-0');

        // Basculer la classe 'open' sur l'icône du menu burger
        // Cette classe est utilisée par le CSS pour animer l'icône (passer des barres à la croix et vice-versa)
        hamburgerButton.querySelector('.hamburger-icon').classList.toggle('open');
    });

   
});

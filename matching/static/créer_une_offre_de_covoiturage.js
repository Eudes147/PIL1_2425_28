// Attendre que le DOM (Document Object Model) soit entièrement chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', () => {
    // Sélectionner le bouton du menu burger par son ID
    const hamburgerButton = document.getElementById('hamburger-button');
    // Sélectionner le menu de navigation mobile par son ID
    const mobileMenu = document.getElementById('mobile-menu');
    // Sélectionner la zone de notification
    const notificationMessageDiv = document.getElementById('notification-message');

    // Fonction pour afficher une notification
    function showNotification(message, isSuccess = true) {
        notificationMessageDiv.textContent = message;
        // Changer la couleur de fond en fonction du succès ou de l'erreur
        if (isSuccess) {
            notificationMessageDiv.classList.remove('bg-red-500');
            notificationMessageDiv.classList.add('bg-green-500');
        } else {
            notificationMessageDiv.classList.remove('bg-green-500');
            notificationMessageDiv.classList.add('bg-red-500');
        }
        notificationMessageDiv.classList.remove('hidden'); // Afficher la notification

        // Cacher la notification après 3 secondes
        setTimeout(() => {
            notificationMessageDiv.classList.add('hidden');
        }, 3000); // 3000 millisecondes = 3 secondes
    }

    // Ajouter un écouteur d'événements 'click' au bouton du menu burger
    hamburgerButton.addEventListener('click', () => {
        // Basculer la classe 'hidden' sur le menu mobile
        mobileMenu.classList.toggle('hidden');

        // Basculer la classe '-translate-x-full' et 'translate-x-0' sur le menu mobile
        mobileMenu.classList.toggle('-translate-x-full');
        mobileMenu.classList.toggle('translate-x-0');

        // Basculer la classe 'open' sur l'icône du menu burger
        hamburgerButton.querySelector('.hamburger-icon').classList.toggle('open');
    });

    // --- Début du code pour la connexion au backend (Page de publication d'offre) ---

    // 1. Sélectionner le formulaire de publication d'offre par son ID
    const offerForm = document.getElementById('offer-form');

    // Vérifier si le formulaire existe sur cette page avant d'ajouter l'écouteur d'événements
    if (offerForm) {
        // 2. Ajouter un écouteur d'événements pour la soumission du formulaire
        offerForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            // 3. Récupérer les valeurs des champs du formulaire
            const pointDepart = document.getElementById('point-depart').value.trim();
            const pointArrivee = document.getElementById('point-arrivee').value.trim();
            const heureDepart = document.getElementById('heure-depart').value.trim();
            const placesDisponibles = document.getElementById('places-disponibles').value.trim();

            // Validation simple côté client
            if (!pointDepart || !pointArrivee || !heureDepart || !placesDisponibles) {
                showNotification("Veuillez remplir tous les champs de l'offre.", false); // Notification d'erreur
                return;
            }

            const numPlaces = parseInt(placesDisponibles);
            if (isNaN(numPlaces) || numPlaces < 1 || numPlaces > 6) {
                showNotification("Le nombre de places doit être un chiffre entre 1 et 6.", false); // Notification d'erreur
                return;
            }

            // 4. Construire l'objet de données à envoyer au backend
            const offerData = {
                point_depart: pointDepart,
                point_arrivee: pointArrivee,
                heure_depart: heureDepart,
                places_disponibles: numPlaces
            };

            console.log("Données de l'offre prêtes à être envoyées :", offerData);

            try {
                // 5. Envoyer la requête POST au backend via l'API Fetch
                const response = await fetch('http://localhost:8000/api/offers/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(offerData),
                });

                // 6. Gérer la réponse du backend
                if (response.ok) {
                    const result = await response.json();
                    console.log('Offre publiée avec succès:', result);
                    showNotification("Votre offre de covoiturage a été publiée avec succès !", true); // Notification de succès
                    
                 

                } else {
                    const errorData = await response.json();
                    console.error('Erreur lors de la publication de l\'offre:', response.status, errorData);
                    showNotification('Erreur lors de la publication : ' + (errorData.message || 'Une erreur inconnue est survenue.'), false); // Notification d'erreur
                }
            } catch (error) {
                console.error('Erreur de connexion au serveur ou problème inattendu:', error);
                showNotification('Impossible de se connecter au serveur. Veuillez vérifier votre connexion et l\'état du backend.', false); // Notification d'erreur
            }
        });
    }
});

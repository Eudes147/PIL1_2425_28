// Attendre que le DOM (Document Object Model) soit entièrement chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', () => {
    // Sélectionner le bouton du menu burger par son ID
    const hamburgerButton = document.getElementById('hamburger-button');
    // Sélectionner le menu de navigation mobile par son ID
    const mobileMenu = document.getElementById('mobile-menu');
    // Sélectionner la zone de notification
    const notificationMessageDiv = document.getElementById('notification-message');

    // Fonction pour afficher une notification (réutilisée de la page précédente)
    function showNotification(message, isSuccess = true) {
        // Vérifie si l'élément de notification existe dans le HTML
        if (!notificationMessageDiv) {
            console.error("L'élément de notification #notification-message n'a pas été trouvé dans le HTML.");
            alert(message); // Fallback vers une alerte simple si l'élément n'est pas là
            return;
        }

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

    // --- Début du code pour la connexion au backend (Page de publication de demande) ---

    // 1. Sélectionner le formulaire de publication de demande par son ID
    const requestForm = document.getElementById('request-form');

    // Vérifier si le formulaire existe sur cette page avant d'ajouter l'écouteur d'événements
    if (requestForm) {
        // 2. Ajouter un écouteur d'événements pour la soumission du formulaire
        requestForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Empêcher le rechargement de la page

            // 3. Récupérer les valeurs des champs du formulaire
            const pointDepartDemande = document.getElementById('point-depart-demande').value.trim();
            const pointArriveeDemande = document.getElementById('point-arrivee-demande').value.trim();
            const heureDepartSouhaitee = document.getElementById('heure-depart-souhaitee').value.trim();

            // Validation simple côté client
            if (!pointDepartDemande || !pointArriveeDemande || !heureDepartSouhaitee) {
                showNotification("Veuillez remplir tous les champs de la demande.", false); // Notification d'erreur
                return;
            }

            // 4. Construire l'objet de données à envoyer au backend
            // Pour l'exemple, nous enverrons à '/api/requests/'
            const requestData = {
                point_depart: pointDepartDemande,
                point_arrivee: pointArriveeDemande,
                heure_depart_souhaitee: heureDepartSouhaitee
                // Vous pourriez ajouter d'autres données ici si nécessaire, comme l'ID de l'utilisateur
            };

            console.log("Données de la demande prêtes à être envoyées :", requestData);

            try {
                // 5. Envoyer la requête POST au backend via l'API Fetch
                // IMPORTANT: L'URL ci-dessous doit correspondre à l'endpoint de votre backend
                // Si votre backend gère les offres et les demandes via un seul endpoint (ex: /api/publications/),
                // vous devrez adapter l'URL et la structure de 'requestData' en conséquence.
                const response = await fetch('http://localhost:8000/api/requests/', { // Exemple d'URL
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        // Si Django CSRF est actif, vous devrez inclure le token ici.
                    },
                    body: JSON.stringify(requestData), // Convertir l'objet JS en chaîne JSON
                });

                // 6. Gérer la réponse du backend
                if (response.ok) { // Si la réponse est un succès (statut 2xx)
                    const result = await response.json();
                    console.log('Demande publiée avec succès:', result);
                    showNotification("Votre demande de covoiturage a été publiée avec succès !", true); // Notification de succès

                    // Optionnel : Rediriger l'utilisateur après la notification
                    setTimeout(() => {
                        window.location.href = 'chargement_matching.html'; // Redirige après la disparition de la notification
                    }, 3000);

                } else { // Si le backend a renvoyé une erreur
                    const errorData = await response.json();
                    console.error('Erreur lors de la publication de la demande:', response.status, errorData);
                    showNotification('Erreur lors de la publication : ' + (errorData.message || 'Une erreur inconnue est survenue.'), false); // Notification d'erreur
                }
            } catch (error) { // Erreurs réseau ou autres
                console.error('Erreur de connexion au serveur ou problème inattendu:', error);
                showNotification('Impossible de se connecter au serveur. Veuillez vérifier votre connexion et l\'état du backend.', false); // Notification d'erreur
            }
        });
    }
});

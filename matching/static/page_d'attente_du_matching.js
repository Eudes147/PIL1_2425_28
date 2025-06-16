// Attendre que le DOM (Document Object Model) soit entièrement chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', () => {
    // Sélectionner le bouton du menu burger par son ID
    const hamburgerButton = document.getElementById('hamburger-button');
    // Sélectionner le menu de navigation mobile par son ID
    const mobileMenu = document.getElementById('mobile-menu');

    // Variable pour stocker l'intervalle d'interrogation du backend
    let checkMatchingInterval;
    // URL de l'endpoint du backend pour vérifier le statut du matching
    // IMPORTANT: Remplacez cette URL par l'URL exacte que votre backend fournira pour le statut du matching
    const MATCHING_STATUS_API_URL = 'http://localhost:8000/api/matching-status/';
    // Fréquence d'interrogation du backend (en millisecondes)
    const POLLING_INTERVAL_MS = 5000; // Vérifier toutes les 5 secondes

    // Fonction pour afficher une notification (peut être nécessaire pour des messages d'erreur si l'interrogation échoue)
    function showNotification(message, isSuccess = true) {
        const notificationDiv = document.getElementById('notification-message');
        if (!notificationDiv) {
            console.error("L'élément de notification #notification-message n'a pas été trouvé.");
            alert(message); // Fallback en cas d'absence de l'élément de notification
            return;
        }

        notificationDiv.textContent = message;
        if (isSuccess) {
            notificationDiv.classList.remove('bg-red-500');
            notificationDiv.classList.add('bg-green-500');
        } else {
            notificationDiv.classList.remove('bg-green-500');
            notificationDiv.classList.add('bg-red-500');
        }
        notificationDiv.classList.remove('hidden');

        setTimeout(() => {
            notificationDiv.classList.add('hidden');
        }, 3000);
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

    // --- Logique d'interrogation du backend pour le statut du matching ---

    /**
     * Fonction pour interroger le backend afin de vérifier le statut du processus de matching.
     * Si le matching est terminé, redirige vers la page des résultats.
     */
    async function checkMatchingStatus() {
        console.log(`Interrogation du backend pour le statut du matching à ${MATCHING_STATUS_API_URL}...`);
        try {
            const response = await fetch(MATCHING_STATUS_API_URL, {
                method: 'GET', // Une requête GET pour récupérer le statut
                headers: {
                    'Content-Type': 'application/json',
                    // Ajoutez ici tout header d'authentification si nécessaire pour le backend
                },
            });

            if (response.ok) {
                const statusData = await response.json(); // Le backend doit renvoyer un JSON comme { "is_completed": true, "result_id": "..." }
                console.log("Statut de matching reçu:", statusData);

                // Vérifier si le matching est terminé selon la réponse du backend
                if (statusData.is_completed) {
                    console.log("Matching terminé ! Redirection vers la page des résultats.");
                    clearInterval(checkMatchingInterval); // Arrêter l'interrogation une fois le travail fini

                    // Rediriger vers la page des résultats.
                    // Si le backend renvoie un ID de résultat, vous pouvez l'inclure dans l'URL:
                    // window.location.href = `resultats_matching.html?id=${statusData.result_id}`;
                    window.location.href = 'affichage_des_résultats.html'; // Nom du fichier de la page des résultats

                } else {
                    console.log("Matching toujours en cours. Prochaine vérification dans " + (POLLING_INTERVAL_MS / 1000) + " secondes.");
                }
            } else {
                // Gérer les erreurs de réponse HTTP du backend
                const errorData = await response.json();
                console.error('Erreur lors de la vérification du statut du matching:', response.status, errorData);
                showNotification(`Erreur backend: ${errorData.message || 'Impossible de vérifier le statut.'}`, false);
                clearInterval(checkMatchingInterval); // Arrêter l'interrogation en cas d'erreur grave
            }
        } catch (error) {
            // Gérer les erreurs réseau (ex: serveur backend non accessible)
            console.error('Erreur réseau lors de l\'interrogation du statut du matching:', error);
            showNotification('Erreur de connexion au serveur de matching. Veuillez vérifier le backend.', false);
            clearInterval(checkMatchingInterval); // Arrêter l'interrogation en cas d'erreur de connexion
        }
    }

    // Démarrer l'interrogation du backend dès que la page est chargée
    // Appeler la fonction une première fois immédiatement, puis à intervalles réguliers
    checkMatchingStatus();
    checkMatchingInterval = setInterval(checkMatchingStatus, POLLING_INTERVAL_MS);

    // --- Fin du code pour la logique de la page d'attente du matching ---
});

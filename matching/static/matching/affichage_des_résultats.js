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

    // --- Début du code pour la connexion au backend (Page d'affichage des résultats de matching) ---

    // Sélectionner le conteneur où les résultats seront affichés
    const resultsListContainer = document.getElementById('results-list');
    // Sélectionner l'élément du message "aucun résultat"
    const noResultsMessage = document.getElementById('no-results-message');

    // URL de l'endpoint du backend pour récupérer les résultats de matching
    // IMPORTANT: Remplacez cette URL par l'URL exacte que votre backend fournira pour les résultats
    const MATCHING_RESULTS_API_URL = 'http://localhost:8000/api/matches/';

    /**
     * Fonction pour récupérer les résultats de matching du backend et les afficher.
     */
    async function fetchAndDisplayResults() {
        // Effacer les résultats précédents et cacher le message "aucun résultat"
        if (resultsListContainer) {
            resultsListContainer.innerHTML = '';
        }
        if (noResultsMessage) {
            noResultsMessage.classList.add('hidden');
        }

        try {
            // Récupérer les résultats du backend
            const response = await fetch(MATCHING_RESULTS_API_URL, {
                method: 'GET', // Requête GET pour récupérer des données
                headers: {
                    'Content-Type': 'application/json',
                    // Ajoutez ici tout header d'authentification si nécessaire pour le backend
                },
            });

            if (response.ok) {
                const matches = await response.json(); // Parser le tableau JSON des correspondances
                console.log('Résultats de matching reçus :', matches);

                if (matches && matches.length > 0) {
                    // Parcourir chaque correspondance et créer sa carte HTML
                    matches.forEach(match => {
                        const matchCard = document.createElement('div');
                        matchCard.className = 'bg-gray-50 p-4 rounded-lg shadow-md flex flex-col md:flex-row items-center md:items-start space-y-4 md:space-y-0 md:space-x-6';

                        // Déterminer s'il s'agit d'une offre ou d'une demande basée sur les données du backend (par exemple, un champ 'type')
                        // Ajustez ces conditions en fonction de la façon dont votre backend distingue les offres/demandes
                        const isOffer = match.type === 'offer'; // Supposons que le backend envoie 'type' : 'offer' ou 'request'
                        const userType = isOffer ? 'Conducteur' : 'Passager';
                        const buttonText = isOffer ? 'Contacter' : 'Proposer un trajet';
                        const iconPlaces = isOffer ? 'fas fa-car' : 'fas fa-user-friends';
                        const placesInfo = isOffer ?
                            `<p class="text-gray-600"><i class="${iconPlaces} text-[#1E8449] mr-2"></i>Places disponibles: ${match.places_disponibles}</p>` :
                            `<p class="text-gray-600"><i class="${iconPlaces} text-[#1E8449] mr-2"></i>Passagers: ${match.passengers_count || 1}</p>`; // Supposons 1 passager pour la demande si non spécifié

                        matchCard.innerHTML = `
                            <div class="flex-shrink-0">
                                <img src="${match.user_photo_url || 'https://placehold.co/80x80/cccccc/ffffff?text=User'}" alt="Photo de profil" class="rounded-full w-20 h-20 object-cover border-2 border-[#1E8449]">
                            </div>
                            <div class="flex-grow text-center md:text-left">
                                <h2 class="text-xl font-semibold text-gray-800 mb-1">${isOffer ? 'Trajet avec' : 'Demande de'} ${match.user_name} <span class="text-sm font-normal text-gray-500">(${userType})</span></h2>
                                <p class="text-gray-600 mb-2"><i class="fas fa-map-marker-alt text-[#1E8449] mr-2"></i>De: ${match.point_depart} à ${match.point_arrivee}</p>
                                <p class="text-gray-600 mb-2"><i class="far fa-clock text-[#1E8449] mr-2"></i>Heure de départ: ${match.heure_depart}</p>
                                ${placesInfo}
                            </div>
                            <div class="flex-shrink-0 mt-4 md:mt-0">
                                <button class="btn-primary py-2 px-6 text-base rounded-md">${buttonText}</button>
                            </div>
                        `;
                        resultsListContainer.appendChild(matchCard);

                        // Optionnel: Ajouter un écouteur d'événements au bouton "Contacter" ou "Proposer un trajet"
                        // matchCard.querySelector('.btn-primary').addEventListener('click', () => {
                        //     // Gérer la logique de contact, par exemple, rediriger vers le chat ou afficher un modal
                        //     console.log(`Bouton cliqué pour le match ID: ${match.id}`);
                        //     // Vous pourriez vouloir passer match.id ou d'autres détails à l'interaction suivante
                        // });
                    });
                } else {
                    // Aucune correspondance trouvée, afficher le message "aucun résultat"
                    if (noResultsMessage) {
                        noResultsMessage.classList.remove('hidden');
                    }
                }
            } else {
                // Gérer les erreurs HTTP du backend
                const errorData = await response.json();
                console.error('Erreur lors de la récupération des résultats de matching :', response.status, errorData);
                if (resultsListContainer) {
                    resultsListContainer.innerHTML = `<p class="text-red-500 text-center">Erreur lors du chargement des correspondances : ${errorData.message || 'Une erreur inconnue est survenue.'}</p>`;
                }
            }
        } catch (error) {
            // Gérer les erreurs réseau ou d'autres problèmes inattendus
            console.error('Erreur réseau ou problème inattendu lors de la récupération des résultats de matching :', error);
            if (resultsListContainer) {
                resultsListContainer.innerHTML = `<p class="text-red-500 text-center">Impossible de se connecter au serveur pour récupérer les correspondances. Veuillez vérifier votre connexion et l'état du backend.</p>`;
            }
        }
    }

    // Appeler la fonction pour récupérer et afficher les résultats lorsque la page est chargée
    // Vous pourriez vouloir retarder ceci si les résultats sont passés via des paramètres de requête depuis la page de matching
    fetchAndDisplayResults();

    // --- Fin du code pour la connexion au backend (Page d'affichage des résultats de matching) ---
});

// Récupérer les éléments du DOM
const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
const messageList = document.getElementById('message-list');

// Récupérer l'ID de la conversation depuis l'URL
const conversationId = window.location.pathname.split('/')[2];

// Configurer la connexion WebSocket
const chatSocket = new WebSocket(
    `ws://${window.location.host}/chat/2/`
);

// Écouter les messages reçus via WebSocket
chatSocket.onmessage = function (event) {
    const data = JSON.parse(event.data);

    // Ajouter le message reçu à la liste des messages
    const messageItem = document.createElement('li');
    messageItem.classList.add('py-2');
    messageItem.innerHTML = `<strong>${data.sender}</strong>: ${data.message}`;
    messageList.appendChild(messageItem);
};

// Gérer les erreurs de connexion WebSocket
chatSocket.onerror = function (error) {
    console.error('WebSocket error:', error);
};

// Gérer la fermeture de la connexion WebSocket
chatSocket.onclose = function () {
    console.log('WebSocket connection closed.');
};

// Envoyer un message via WebSocket
messageForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const message = messageInput.value;

    if (message.trim() !== '') {
        chatSocket.send(JSON.stringify({
            'message': message,
            'sender_id': userId, // Remplacez par l'ID de l'utilisateur connecté
            'receiver_id': receiverId // Remplacez par l'ID du destinataire
        }));

        // Réinitialiser le champ de saisie
        messageInput.value = '';
    }
});
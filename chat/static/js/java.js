document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('messageInput');
    const sendMessageBtn = document.getElementById('sendMessageBtn');
    const chatMessages = document.getElementById('chatMessages');

    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', type);
        const paragraph = document.createElement('p');
        paragraph.textContent = text;

        messageDiv.appendChild(paragraph);
        chatMessages.appendChild(messageDiv);

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    sendMessageBtn.addEventListener('click', () => {
        const messageText = messageInput.value.trim();
        if (messageText !== '') {
            addMessage(messageText, 'sent');
            messageInput.value = '';
            setTimeout(() => {
                addMessage("merci pour votre message !", 'received');
            }, 1000);
        }
    });
    messageInput.addEventListener('keypress', (Event) => {
        if (Event.key === 'Enter') {
            sendMessageBtn.click();
        }
    });
    chatMessages.scrollTop = chatMessages.scrollHeight;
});
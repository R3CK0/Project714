<!DOCTYPE html>
<html>
<head>
    <title>Green Chat Bot</title>
    <style>
        /* Style the chat window */
        .chat-window {
        width: 300px;
        height: 400px;
        background-color: #fff;
        border: 2px solid #3CB371;
        border-radius: 10px;
        overflow-y: scroll;
        margin: 50px auto;
        padding: 20px;
    }

    /* Style the user input box */
        .user-input {
        width: 100%;
        border: none;
        border-top: 2px solid #3CB371;
        padding: 10px;
        margin-top: 20px;
        font-size: 16px;
    }

    /* Style the chat messages */
        .chat-message {
        background-color: #3CB371;
        color: #fff;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* Style the chat bot response */
        .bot-response {
        background-color: #fff;
        color: #3CB371;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
</head>
<body>
    <div class="chat-window">
        <div class="chat-message">
            <p>Welcome to the Green Chat Bot!</p>
            <p>How can I assist you today?</p>
        </div>
    </div>

    <input type="text" class="user-input" placeholder="Enter your message...">

        <script>     const chatWindow = document.querySelector('.chat-window');
            const userInput = document.querySelector('.user-input');

            // Function to add user message to chat window

            function addUserMessage(message) {
                const userMessage = document.createElement('div');
                userMessage.textContent = message;
                userMessage.classList.add('chat-message');
                chatWindow.appendChild(userMessage);
        }

        // Function to add chat bot response to chat window
            function addBotResponse(response) {
                const botResponse = document.createElement('div');
                botResponse.textContent = response;
                botResponse.classList.add('bot-response');
                chatWindow.appendChild(botResponse);
        }

        // Function to handle user input
            function handleUserInput(event) {
            if (event.keyCode === 13) {
                const userInputText = userInput.value;
                addUserMessage(userInputText);
                userInput.value = '';

                // Call function to generate bot response
                generateBotResponse(userInputText);
            }
        }

        // Function to generate chat bot response
            function generateBotResponse(userInputText) {
            // You can add your own bot response logic here
            const botResponseText = "I'm sorry, I don't understand. Please try again.";
            addBotResponse(botResponseText);
        }
            // Event listener for user input
            userInput.addEventListener('keydown', handleUserInput);
        </script>
    </body>
</html>
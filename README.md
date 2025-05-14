
# Today in History Bot

This is a Flask-based chatbot that integrates with SwiftChat to provide historical events from Wikipedia. It can respond to user input about today's events or events on specific dates (in DD-MM format). 

## Features:
- **Welcome Message**: Greets the user and provides options to either get historical events for **Today** or a **Specific Date (DD-MM)**.
- **Today's Events**: Fetches and sends 5 historical events for the current date from Wikipedia.
- **Specific Date Events**: Fetches and sends historical events for any given date in DD-MM format (e.g., 14-05).
- **Event Details**: Each event includes the year, description, and a link to read more on Wikipedia.

## Requirements:
- Python 3.x
- Flask
- Requests
- A valid SwiftChat API Key
- An active SwiftChat bot setup

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://your-repo-url.git
   cd your-repo-folder
   ```

2. **Set up a Python virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup SwiftChat Bot**:
   - Create a SwiftChat bot at [SwiftChat](https://swiftchat.ai) and get your API key and bot ID.
   - Replace `SWIFTCHAT_API_KEY` and `SWIFTCHAT_API_URL` in the code with your bot's API key and endpoint.

## Running the App

1. **Start the Flask app**:
   ```bash
   python app.py
   ```

2. **Webhook for SwiftChat**:
   - Expose the Flask server to the internet using tools like [ngrok](https://ngrok.com/) or deploy it to a cloud server.
   - Make sure to configure SwiftChat to call your webhook URL.

## How It Works:

- **User starts the conversation**:
  - The bot will greet the user and offer two options: 
    - "Today" to fetch events for the current day.
    - "Specific Date (DD-MM)" to let the user input a specific date.
  
- **When "Today" is selected**:
  - The bot fetches and sends 5 historical events for the current date.
  
- **When "Specific Date" is selected**:
  - The bot prompts the user to enter a date in DD-MM format (e.g., 14-05), and fetches the corresponding events.

## API Endpoints:

- **Webhook URL**:
  - This Flask app listens on `/swiftchat-webhook` for incoming messages from SwiftChat.
  - The app responds to button interactions and provides historical events based on user input.

## Sample Responses:

- **On "Today" button click**:
  - The bot fetches today's events from Wikipedia and sends them.
  
- **On "Specific Date" button click**:
  - The bot prompts the user to enter a date in the format DD-MM.

## Testing

- Use a tool like [Postman](https://www.postman.com/) to simulate webhook requests.
- Send a `POST` request to the `/swiftchat-webhook` endpoint with a sample payload to test the flow.

### Example Payload:

```json
{
    "from": "+919689865795",
    "type": "button_response",
    "button_response": {
        "button_index": 0,
        "body": "Today"
    }
}
```

## Application/Bot link

https://web.convegenius.ai/bots?botId=0289706498212451

## Troubleshooting

- Ensure the `SWIFTCHAT_API_KEY` and `SWIFTCHAT_API_URL` are correctly set with your SwiftChat bot's details.
- If you encounter any issues with API responses, check if the API key has the necessary permissions or if the bot is correctly configured.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

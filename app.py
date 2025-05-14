from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

SWIFTCHAT_API_URL = 'https://v1-api.swiftchat.ai/api/bots/0289706498212451/messages'
SWIFTCHAT_API_KEY = '<api-key>'

# Function to send a text message to SwiftChat
def send_text_message(user_id, body):
    payload = {
        "to": user_id,
        "type": "text",
        "text": {
            "body": body
        },
        "rating_type": "thumb"
    }
    headers = {
        'Authorization': f'Bearer {SWIFTCHAT_API_KEY}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(SWIFTCHAT_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        print(f"✅ Sent message: {body}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send message: {e}")

# Function to fetch events for a specific date and send them to SwiftChat
def fetch_and_send_events(user_id, month, day):
    try:
        wiki_url = f'https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{month}/{day}'
        response = requests.get(wiki_url)
        response.raise_for_status()
        events = response.json().get("events", [])[:5]

        if not events:
            send_text_message(user_id, "No historical events found for that date.")
            return

        for event in events:
            title = f"{event['year']} – {event['text'].split('.')[0]}"
            subtitle = event['text']
            link = event['pages'][0]['content_urls']['desktop']['page']
            message = f"{title}\n\n{subtitle}\n\nRead more: {link}"
            send_text_message(user_id, message)

    except Exception as e:
        print(f"❌ Error fetching or sending events: {e}")
        send_text_message(user_id, "Sorry, something went wrong while fetching the events.")

@app.route('/swiftchat-webhook', methods=['GET', 'POST'])
def swiftchat_webhook():
    if request.method == 'GET':
        return "SwiftChat webhook is up! (GET)"

    elif request.method == 'POST':
        data = request.get_json()
        print("📩 Incoming SwiftChat message:", data)

        user_id = data.get("from")
        message = data.get("text", {}).get("body", "").strip()

        # Check if message matches a DD-MM pattern
        if len(message) == 5 and message[2] == '-':
            try:
                day, month = map(int, message.split('-'))
                if 1 <= day <= 31 and 1 <= month <= 12:
                    send_text_message(user_id, f"📅 Fetching historical events for {message}...")
                    fetch_and_send_events(user_id, month, day)
                    return jsonify({"status": "custom-date-events-sent"})
            except:
                pass  # If parsing fails, continue to normal flow

        # Step 1: Welcome message
        send_text_message(user_id, "👋 Welcome to Today in History! Here's what happened today:")

        # Step 2: Today's events
        today = datetime.now()
        fetch_and_send_events(user_id, today.month, today.day)

        # Step 3: Ask for custom date
        send_text_message(user_id, "Would you like to know events for a specific date?\nReply in DD-MM format (e.g., 04-07).")

        return jsonify({"status": "today-and-custom-request-sent"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

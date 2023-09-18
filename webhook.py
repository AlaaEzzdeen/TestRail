from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('X-GitHub-Event') == 'push':
        payload = request.get_json()
        print("Received push event from GitHub:")
        print(payload)
        # Perform TestRail actions based on the received payload
    else:
        return 'Invalid event', 400

    return 'Webhook received', 200

if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Schwab API OAuth callback test!"

# This route handles the OAuth callback after user logs in with Schwab
@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    
    if code:
        # Process the authorization code, typically exchanged for an access token here
        return f"Authorization successful with code: {code} and state: {state}"
    else:
        return "Error: Authorization code not found", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

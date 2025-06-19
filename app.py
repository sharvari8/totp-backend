from flask import Flask, request, jsonify
from flask_cors import CORS
import pyotp

# Initialize the app
app = Flask(__name__)
CORS(app)  # Enable CORS so Bubble can call it

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()  # Get JSON data from Bubble

    token = data.get('token')   # The 6-digit code from user
    secret = data.get('secret') # The shared secret stored in Bubble

    if not token or not secret:
        return jsonify({"valid": False, "error": "Missing token or secret"}), 400

    # Validate the code
    totp = pyotp.TOTP(secret)
    is_valid = totp.verify(token)

    # Return result
    return jsonify({"valid": is_valid})

# Run the app locally (port 3000)
if __name__ == '__main__':
    app.run(port=3000)

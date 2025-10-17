from flask import Flask, request, jsonify
import joblib
import numpy as np
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

model = joblib.load("fall_detection_model.pkl")

def send_sms(message_body):
    """Send alert SMS via Twilio"""
    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=TARGET_PHONE_NUMBER
        )
        print("SMS sent:", message.sid)
    except Exception as e:
        print("SMS sending failed:", e)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        ax = float(request.form.get('ax'))
        ay = float(request.form.get('ay'))
        az = float(request.form.get('az'))
        gx = float(request.form.get('gx'))
        gy = float(request.form.get('gy'))
        gz = float(request.form.get('gz'))

        data = np.array([[ax, ay, az, gx, gy, gz]])
        print("📩 Received:", data)

        result = model.predict(data)
        print("🔍 Prediction:", result)

        if result[0] == 1:
            send_sms("Fall detected! Please check immediately.")
            return jsonify({"status": "fall_detected"}), 200
        else:
            return jsonify({"status": "no_fall"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    print("Flask server running on port 5000...")
    app.run(host='0.0.0.0', port=5000)

import base64
import hmac
import hashlib
import time

SECRET_KEY="abcdefghijklmnopqrstuvwxyz"

def generate_token(id,name):
    data = f"{id}|{name}"
    token = base64.b64encode(hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.sha256).digest()).decode('utf-8')
    return f"{data}|{token}"


def decode_token(token):
    try:
        parts = token.split('|')
        if len(parts) != 3:
            raise ValueError("Invalid token format.")
        user_data = '|'.join(parts[:2])
        received_token = parts[2]
        expected_token = base64.b64encode(
            hmac.new(SECRET_KEY.encode(), user_data.encode(), hashlib.sha256).digest()
        ).decode('utf-8')
        if hmac.compare_digest(expected_token, received_token):
            user_id, username = parts[:2]
            return user_id
        else:
            return "Invalid Token"
    except Exception as e:
        return f"Error: {e}"
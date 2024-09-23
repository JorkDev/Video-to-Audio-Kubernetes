from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401

    # Token generation
    token = jwt.encode({
        'user': auth.get('username'),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'token': token})

# Protected endpoint
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('x-access-token')
    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    except:
        return jsonify({'message': 'Token is invalid'}), 401
    
    return jsonify({'message': 'Valid token! Welcome.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

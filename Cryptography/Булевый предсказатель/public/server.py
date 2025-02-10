from flask import Flask, request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os

app = Flask(__name__)


def generate_rsa_keypair(bits=2048):
    key = RSA.generate(bits)
    return key, key.publickey()


def encrypt_flag(public_key, flag):
    m = bytes_to_long(flag.encode())
    c = pow(m, public_key.e, public_key.n)
    return c


def parity_oracle(ciphertext):
    m = pow(ciphertext, PRIVATE_KEY.d, PRIVATE_KEY.n)
    return m % 2 == 0


PRIVATE_KEY, PUBLIC_KEY = generate_rsa_keypair()
FLAG = ""
ENCRYPTED_FLAG = encrypt_flag(PUBLIC_KEY, FLAG)


@app.route('/public_key', methods=['GET'])
def get_public_key():
    return jsonify({
        "n": str(PUBLIC_KEY.n),
        "e": str(PUBLIC_KEY.e),
        "ciphertext": str(ENCRYPTED_FLAG)
    })


@app.route('/oracle', methods=['GET'])
def oracle():
    try:
        ciphertext = int(request.args.get('ciphertext', '0'))
        if ciphertext <= 0 or ciphertext >= PUBLIC_KEY.n:
            return jsonify({"error": "Invalid ciphertext"}), 400
        
        is_even = parity_oracle(ciphertext)
        return jsonify({"even": is_even})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

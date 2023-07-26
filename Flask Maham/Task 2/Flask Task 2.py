from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/md5', methods=['POST'])
def calculate_md5():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        im_bytes = file.read()
        im_hash = hashlib.md5(im_bytes).hexdigest()
        return jsonify({"md5_hash": im_hash})

    except Exception as e:
        return jsonify({"error": "Error occurred while processing the image"}), 500

if __name__ == '__main__':
    app.run(debug=True)


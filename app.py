from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to AI Cloud Storage!"

# Example API endpoint
@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        # Here you would add code to save to cloud (e.g., Google Cloud Storage)
        return jsonify({"status": "success", "filename": file.filename})
    return jsonify({"status": "error", "message": "No file uploaded"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

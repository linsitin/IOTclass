from flask import Flask, request

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    print("收到請求")
    print("request.files:", request.files)
    print("request.form:", request.form)
    if 'file' not in request.files:
        print("沒有收到 file")
        return "No file received", 400
    file = request.files['file']
    file.save("test.jpg")
    return "File received successfully", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

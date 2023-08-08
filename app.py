from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods =["POST","GET"])
def index():
    return jsonify({
        "response" : "hello world"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
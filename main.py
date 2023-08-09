from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import openai, requests
load_dotenv()


app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods =["POST","GET"])
def index():
   data = request.json
   data = data["animal"]
   for item in data:
       if "id" in item:
           del item["id"]
   print("DATA",data)
   response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=data
        )
   response = response.choices[0].message
   print(response) 
   return jsonify({"result" : response})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug = True)
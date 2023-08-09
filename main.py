from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import openai, requests
load_dotenv()


app = Flask(__name__)
CORS(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)
openai.api_key = os.getenv("OPENAI_API_KEY")
env_variable = os.getenv("DEV")

@app.route("/", methods =["POST","GET"])
def index():
   data = request.json
   
   if data["key"] != "123456":
       print("ABORT")
       return make_response(jsonify({"error":"something went wrong"}), 500)
    
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

if env_variable == "development":
    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug = True)
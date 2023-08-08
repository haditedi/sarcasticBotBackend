from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import openai
load_dotenv()


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods =["POST","GET"])
def index():
  
   response = openai.Completion.create(
            model="text-davinci-003",
            prompt="HOW ARE YOU?",
            temperature=0.6,
        )
   response = response.choices[0].text
    
   return jsonify({"result" : response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        genre = data.get("genre", "general")
        length = data.get("length", "short")

        word_count = {"short": 100, "medium": 300, "long": 600}
        words = word_count.get(length, 100)

        system_prompt = f"You are a creative story writer. Write a {genre} short story in approximately {words} words based on the user's prompt. Make it engaging and vivid."

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        story = response.choices[0].message.content
        return jsonify({"story": story})

    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"story": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
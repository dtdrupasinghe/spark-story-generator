# ✨ Spark - AI Story Generator

> Turn your ideas into stories with AI — built for the Microsoft Agents League 2026 challenge.

![Spark App](https://img.shields.io/badge/Track-Creative%20Apps-e94560?style=for-the-badge)
![Built With](https://img.shields.io/badge/Built%20With-GitHub%20Copilot-blue?style=for-the-badge)

## 📖 What is Spark?

Spark is an AI-powered short story generator that transforms simple prompts into engaging stories in seconds. Users type a prompt, choose a genre and length, and get a unique story instantly. Don't like it? Hit Remix for a fresh take!

## ✨ Features

- 🎭 **7 Genres** — General, Mystery, Comedy, Romance, Horror, Sci-Fi, Fantasy
- 📏 **3 Story Lengths** — Flash (100 words), Short (300 words), Full (600 words)
- 🔀 **Remix Button** — Generate a new story from the same prompt instantly
- 📋 **Copy to Clipboard** — Save your story with one click
- 🌙 **Beautiful dark UI** — Clean, polished, and easy to use

## 🤖 How GitHub Copilot Helped

GitHub Copilot was used throughout the entire development process:

- **Backend code** — Copilot suggested the Flask route structure and Groq API integration
- **HTML & CSS** — Copilot helped generate the dark gradient UI and responsive layout
- **JavaScript** — Copilot autocompleted the fetch API calls and error handling
- **Debugging** — Copilot Chat helped diagnose and fix API connection issues

## 🛠️ Tech Stack

- **Frontend** — HTML, CSS, JavaScript
- **Backend** — Python, Flask
- **AI Model** — Groq API (LLaMA 3.3 70B)
- **Dev Tool** — GitHub Copilot in VS Code

## 🚀 How to Run Locally

1. Clone the repository:
\```bash
git clone https://github.com/dtdrupasinghe/spark-story-generator.git
cd spark-story-generator
\```

2. Create a virtual environment:
\```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\```

3. Install dependencies:
\```bash
pip install flask groq python-dotenv
\```

4. Create a `.env` file:
\```
GROQ_API_KEY=your-groq-api-key-here
\```

5. Run the app:
\```bash
python app.py
\```

6. Open your browser at `http://127.0.0.1:5000`

## 📦 Project Structure

\```
spark-story-generator/
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Frontend UI
├── .env                # API key (not included in repo)
├── .gitignore          # Excludes secrets
└── README.md           # This file
\```

## 🏆 Competition

Built for the **Microsoft Agents League 2026** — Creative Apps Track.
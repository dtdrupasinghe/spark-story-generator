# ✨ Spark - AI Story Generator

> Turn your ideas into stories with AI — built for the Microsoft Agents League 2026 challenge.

![Spark App](https://img.shields.io/badge/Track-Creative%20Apps-e94560?style=for-the-badge)
![Built With](https://img.shields.io/badge/Built%20With-GitHub%20Copilot-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📖 What is Spark?

Spark is an AI-powered short story generator that transforms simple prompts into engaging stories in seconds. Users type a prompt, choose a genre and length, and get a unique story instantly. Don't like it? Hit Remix for a fresh take!

## ✨ Features

- 🎭 **7 Genres** — General, Mystery, Comedy, Romance, Horror, Sci-Fi, Fantasy
- 📏 **3 Story Lengths** — Flash (100 words), Short (300 words), Full (600 words)
- 🔀 **Remix Button** — Generate a new story from the same prompt instantly
- 📋 **Copy to Clipboard** — Save your story with one click
- 🌙 **Beautiful dark UI** — Clean, polished, and easy to use

## 🧠 Problem Solving Approach

1. **User need identified** — People have creative ideas but struggle to develop them into full stories
2. **Solution designed** — A prompt-based generator with genre control gives users creative direction
3. **Multi-step generation** — The app combines user prompt + genre + length into a structured system prompt for better story quality
4. **Iteration built in** — The Remix feature lets users refine results without retyping their prompt
5. **Safety considered** — API keys stored in environment variables, no user data stored or logged
6. **Reliability ensured** — Error handling on both frontend and backend with clear user feedback

## 🤖 How GitHub Copilot Helped

GitHub Copilot was used throughout the entire development process:

### Code Generation
- Copilot suggested the Flask route structure (`@app.route`) and helped complete functions automatically
- Copilot autocompleted the Groq API integration including the messages array format
- Copilot generated the CSS gradient styling and responsive layout for the UI

### Problem Solving with Copilot Chat
- Used Copilot Chat to debug API connection errors and resolve module import issues
- Asked Copilot Chat to explain how `python-dotenv` loads environment variables securely
- Copilot Chat suggested using `jsonify()` for returning JSON responses from Flask

### JavaScript Assistance
- Copilot autocompleted the `fetch()` API call to the backend
- Copilot suggested the async/await pattern for handling the story generation response
- Copilot generated the clipboard copy functionality

### Overall Impact
GitHub Copilot significantly accelerated development by reducing boilerplate code and suggesting best practices, allowing focus on the creative and user experience aspects of the app.

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
├── LICENSE             # MIT License
└── README.md           # This file
\```

## 🏆 Competition

Built for the **Microsoft Agents League 2026** — Creative Apps Track.

## 👨‍💻 Developer

Developed by **Thisara Rupasinghe**

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
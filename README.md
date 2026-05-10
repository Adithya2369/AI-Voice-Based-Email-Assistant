# 🎙️ Iris Voice Email Assistant

An AI-powered voice-controlled email assistant built with Python that can:

* Read unread emails
* Count unread emails
* Generate professional emails using Gemini AI
* Send emails using voice commands
* Convert speech to text and text to speech
* Use fuzzy matching for contact detection

---

# 🎓 Academic Project Information

This repository is part of my B.Tech Final Year Project and represents **Module 5** of the complete system.

This module focuses on developing an AI-powered voice-based email assistant designed to improve accessibility and hands-free communication. The system integrates speech recognition, text-to-speech conversion, Gmail services, and Gemini AI to automate email reading and email generation using natural voice commands.

The project demonstrates the integration of artificial intelligence, voice processing, and email automation technologies in a real-time assistive application.

---

# ✨ Features

### 🎤 Voice Commands

The assistant listens for commands like:

* "Read my unread emails"
* "How many unread emails do I have?"
* "Write an email to Adi"
* "Exit"

### 🤖 AI Email Generation

Uses Google's Gemini AI to generate complete and professional emails automatically.

### 🔊 Text-to-Speech

The assistant responds using voice output.

### 🗣️ Speech Recognition

Converts your voice into commands and email prompts.

### 📧 Smart Contact Matching

Uses fuzzy matching to recognize contact names even if pronunciation varies.

<p align="center">
  <img src="https://raw.githubusercontent.com/Adithya2369/AI-Voice-Based-Email-Assistant/main/block_diagram.png" width="600"/>
</p>

---

# 🛠️ Technologies Used

* Python
* Google Gemini AI
* SpeechRecognition
* gTTS
* Pyglet
* SMTP
* IMAP
* Difflib

---

# 📁 Project Structure

```bash
.
├── main.py
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Voice-Based-Email-Assistant.git
cd AI-Voice-Based-Email-Assistant
```

## 2️⃣ Install Dependencies

```bash
pip install SpeechRecognition gtts pyglet google-generativeai pyaudio
```

---

# 🔐 Gmail Setup

## Enable App Passwords

1. Enable 2-Step Verification in your Google Account
2. Generate an App Password
3. Replace the credentials inside the script

```python
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
GEMINI_API_KEY = "your_gemini_api_key"
```

4. Replace the contacts inside the script

```python
CONTACTS = {
    "alpha": "contact1@gmail.com",
    "beta": "contact2@gmail.com",
    "charlie": "contact3@gmail.com"
}
```
---

# 🚀 How It Works

## ▶️ Start the Assistant

```bash
python main.py
```

The assistant will ask:

```text
What would you like to do?
```

You can then speak commands naturally.

---

# 💡 Example Commands

## 📬 Count Unread Emails

```text
How many unread emails do I have?
```

## 📖 Read Latest Email

```text
Read my unread email
```

## ✍️ Send AI Generated Email

```text
Write an email
```

Then speak the receiver's name.
```text
alpha
```

Then describe the email content verbally.

---

# 🧠 AI Email Generation

Gemini AI automatically creates:

* Professional tone
* Complete email formatting
* Greeting and closing
* Ready-to-send emails

---

# ⚠️ Security Warning

Do NOT hardcode sensitive credentials in production projects.

Instead, use:

* Environment variables
* `.env` files
* Secret managers

---

# 🔮 Future Improvements

* GUI dashboard
* Multi-language support
* Attachment support
* Email summarization
* Contact database integration
* Wake-word detection
* Real-time notifications

---

# 📜 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

T. Adithya Reddy

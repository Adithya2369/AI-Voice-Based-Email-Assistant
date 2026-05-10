import smtplib
import imaplib
import email
import speech_recognition as sr
from gtts import gTTS
import pyglet
import time, os
import google.generativeai as genai
import difflib

# ==============================
# CONFIGURATION
# ==============================

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
GEMINI_API_KEY = "your_gemini_api_key"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# ==============================
# HARDCODED CONTACTS
# ==============================

CONTACTS = {
    "alpha": "contact1@gmail.com",
    "beta": "contact2@gmail.com",
    "charlie": "contact3@gmail.com"
}

# ==============================
# TEXT TO SPEECH
# ==============================

def speak(text):
    print("Assistant:", text)
    tts = gTTS(text)
    filename = "voice.mp3"
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(filename)

# ==============================
# SPEECH TO TEXT
# ==============================

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        speak("Sorry, I did not understand.")
        return ""

# ==============================
# SMART CONTACT FETCH (FUZZY MATCH)
# ==============================

def get_contact_email(name):
    name = name.lower()
    contact_names = CONTACTS.keys()

    match = difflib.get_close_matches(name, contact_names, n=1, cutoff=0.6)

    if match:
        matched_name = match[0]
        speak(f"Sending email to {matched_name}")
        return CONTACTS[matched_name]

    return None

# ==============================
# COUNT UNREAD MAILS
# ==============================

def count_unread():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")
    status, messages = mail.search(None, '(UNSEEN)')
    mail_ids = messages[0].split()
    mail.logout()
    return len(mail_ids)

# ==============================
# READ LATEST UNREAD MAIL
# ==============================

def read_latest_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")
    status, messages = mail.search(None, '(UNSEEN)')
    mail_ids = messages[0].split()

    if not mail_ids:
        speak("You have no unread emails.")
        return

    latest_id = mail_ids[-1]
    status, msg_data = mail.fetch(latest_id, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])

    subject = msg["Subject"]
    sender = msg["From"]

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = msg.get_payload(decode=True).decode()

    mail.logout()

    speak(f"Mail from {sender}. Subject: {subject}. Message: {body}")

# ==============================
# GENERATE EMAIL USING GEMINI (UPDATED)
# ==============================

def generate_email_content(prompt):
    system_prompt = """
You are an email writing assistant.

STRICT INSTRUCTIONS:
- You MUST generate a COMPLETE and FINAL email.
- DO NOT leave placeholders like [Name], [Date], etc.
- DO NOT ask the user to fill anything manually.
- DO NOT include options or multiple versions.
- DO NOT include explanations.

EMAIL FORMAT RULES:
- Start with a general greeting like "Hello there,".
- Write a clear, professional, and complete email based on the request.
- The email must be fully ready to send as-is.
- End the email with the sender name: Iris_Adithya

Generate ONLY the email content.
"""

    response = model.generate_content(
        system_prompt + "\n\nUser request:\n" + prompt
    )

    return response.text.strip()

# ==============================
# SEND EMAIL
# ==============================

def send_email(to_email, content):
    subject = "Regarding your request"
    message = f"Subject: {subject}\n\n{content}"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL, APP_PASSWORD)
    server.sendmail(EMAIL, to_email, message)
    server.quit()

# ==============================
# MAIN SYSTEM LOOP
# ==============================

speak("Voice based email assistant started.")

while True:
    speak("What would you like to do?")
    command = listen()

    if "unread" in command:
        count = count_unread()
        speak(f"You have {count} unread emails.")

    elif "read" in command:
        read_latest_mail()

    elif "write" in command:
        speak("Tell me the name of the recipient.")
        name = listen()
        recipient_email = get_contact_email(name)

        if recipient_email:
            speak("What should I write in the email?")
            user_prompt = listen()

            ai_email = generate_email_content(user_prompt)

            # DIRECT SEND (NO CONFIRMATION)
            send_email(recipient_email, ai_email)
            speak("Email sent successfully.")

        else:
            speak("Contact not found.")

    elif "exit" in command:
        speak("Goodbye.")
        break

    else:
        speak("Sorry, I cannot understand your request.")
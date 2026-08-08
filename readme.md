# 📧 Local AI Email Generator

A privacy-focused AI Email Generator that runs completely on your local machine using **Ollama** and **Qwen 3.5**. The application generates high-quality emails in different writing styles without sending your data to any cloud service.

---

## ✨ Features

- 🤖 AI-powered email generation
- 🔒 100% Local Processing (No Cloud APIs)
- ⚡ FastAPI backend
- 📝 Multiple email styles
  - Professional
  - Formal
  - Casual
  - Friendly
  - Apology
  - Request
  - Thank You
  - Custom
- 🎯 Simple and responsive web interface
- ⚙️ Easy to customize prompts
- 💻 Cross-platform support

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Ollama
- Qwen 3.5

### Frontend
- HTML
- CSS

### AI
- Ollama
- Qwen 3.5

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Local-AI-Email-Generator.git
```

```bash
cd Local-AI-Email-Generator
```

---

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install Ollama

Download Ollama from

https://ollama.com

---

### 4. Pull Qwen 3.5 Model

```bash
ollama pull qwen3.5:4b
```

*Replace the model name if you're using a different version.*

---

### 5. Start Ollama

```bash
ollama serve
```

---

### 6. Run FastAPI

```bash
uvicorn main:app --reload
```

---

### 7. Open the Frontend

Open `index.html`

or

Visit

```
http://localhost:8000
```

---

## 📖 Usage

1. Enter the email subject or prompt.
2. Select the desired writing style.
3. Click **Generate**.
4. Copy or edit the generated email.

---

## 📸 Screenshots

Add screenshots of the application here.

```
screenshots/home.png
screenshots/generated-email.png
```

---

## 🎯 Future Improvements

- Gmail Integration
- Outlook Integration
- AI Email Summarization
- Grammar Correction
- Tone Detection
- Email Templates
- Multi-language Support
- Dark Mode
- User Profiles
- Export to PDF/Word

---

## 🔒 Privacy

Unlike cloud-based AI assistants, this project processes everything **locally**.

No prompts, emails, or user data are sent to external servers, making it suitable for privacy-conscious users and organizations.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.
---

## 👨‍💻 Author

**Himanshu Tushar Chaudhari**

Computer Engineering Student

AI • Machine Learning • Python • FastAPI • Automation

If you found this project useful, consider giving it a ⭐ on GitHub!

# 🎵 MelodyVerse AI

### Turn your thoughts into music.

MelodyVerse AI is an AI-powered songwriting platform designed to transform creative ideas, memories, emotions, and stories into meaningful song lyrics.

Built using Django and Google's Gemini API.

## ✨ Features

- AI-powered lyrics generation.
- Multiple language support: Hindi, Bengali, English and Hinglish.
- Multiple music genres and emotional moods.
- Custom storytelling prompts.
- Vocal preference and song duration selection.
- Structured songwriting.
- AI-based lyrics improvement (planned).
- Original and reviewed lyrics management (planned).
- Lyrics library and export functionality (planned).

## 🛠️ Technology Stack

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Google Gemini API

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/melodyverse-ai.git
cd melodyverse-ai
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install django python-dotenv google-genai
```

### 5. Configure environment variables

Create `.env`:

```env
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=your_supported_gemini_model
GEMINI_FALLBACK_MODELS=
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start development server

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

## 🏗️ Project Vision

MelodyVerse AI aims to become a complete AI songwriting studio featuring:

1. AI Lyrics Creator.
2. AI Lyrics Reviewer.
3. Original vs Improved Lyrics Comparison.
4. Human Review and Approval.
5. Lyrics Management Library.
6. AI Music Production Prompt Generator.
7. Music Production Workflow Integration.

## 📌 Project Status

Currently under active development.

## 👨‍💻 Author

Sudip Bera
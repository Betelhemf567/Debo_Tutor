# Debo – Student Peer-to-Peer Learning Platform  
(ደቦ – ተማሪዎች ብቻ የሚጠቀሙበት የጋራ ትምህርት መድረክ)

**Live Public URL** → https://debo-tutor-collaboration.onrender.com/


## Summative Submission Links (28 November 2025)

- **Video Demo (5–10 min)** → https://drive.google.com/file/d/YOUR_VIDEO_ID/view?usp=sharing ←←← REPLACE THIS  
- **SRS Document** → https://docs.google.com/document/d/YOUR_SRS_ID/edit?usp=sharing ←←← REPLACE THIS  
- **Live Deployed App** → https://debo-tutor-collaboration.onrender.com/

---

### Problem Statement & Why It Matters
In Ethiopia — especially in underserved regions like **Benishangul-Gumuz** — students face:
- Very few qualified tutors
- Expensive or completely unavailable private tutoring
- No structured platform for peer academic support
- Lack of free, localized study materials

UNESCO (2022) estimates Africa needs **17 million more teachers by 2030**. In rural Ethiopia, students rely on informal study groups that are inconsistent, location-bound, and often unproductive.

**Debo** solves this by providing a **free, student-only, mobile-friendly platform** where learners can ask questions, answer each other, and truly learn together — embodying the Amharic word “Debo” (collective effort).

### Implemented Features (Exactly as required by SRS)
- Register / Login / Logout (simple 4-digit PIN system – ideal for students)
- Post academic questions (title, description, subject: Math, Science, English, History, Other)
- Reply to any question
- View all questions (newest first)
- Clean, fully responsive design that works perfectly on low-end phones and slow internet
- Fully deployed and publicly accessible worldwide

### Technology Stack
- Backend: Django (Python)
- Database: SQLite (development) → PostgreSQL (production)
- Frontend: HTML5 + custom responsive CSS
- Deployment: Render.com (free tier) + Gunicorn + Whitenoise
- Authentication: Django built-in auth

### How to Run Locally – Step-by-Step (100% reproducible)

```bash
# 1. Clone the repository
git clone https://github.com/Betelhemf567/debo-tutor.git
cd debo-tutor

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Create superuser for admin panel
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver

Open your browser → http://127.0.0.1:8000

Register at /register/
Login at /login/
Start posting and answering questions!

Production Deployment (Already Live)
The application is fully deployed and publicly accessible at the link above.
Deployed using:

Render.com free web service
Automatic builds via build.sh and Procfile
Free PostgreSQL add-on
All environment variables configured in Render dashboard

Anyone in the world can visit the live URL, register, and use the platform right now.

### Project Structure

debo-tutor/
├── core/                  # Main app (models, views, urls, templates)
├── templates/             # Register, login, home, question list, etc.
├── static/                # CSS, images
├── debo/                  # Project settings & wsgi
├── manage.py
├── Procfile               # For Render/Heroku/Fly.io
├── build.sh               # Install → collectstatic → migrate
├── requirements.txt
└── README.md              # ← You are reading this


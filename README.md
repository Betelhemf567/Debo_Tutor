# Debo – Student Peer-to-Peer Learning Platform  
*(ደቦ – ተማሪዎች ብቻ የሚጠቀሙበት የጋራ ትምህርት መድረክ)*

**Live Public URL:** https://debo-tutor-collaboration.onrender.com  

  

---

## Summative Submission Links – 28 November 2025

| Item                          | Link |
|-------------------------------|------|
| Video Demo (5–10 min)         | https://drive.google.com/file/d/YOUR_VIDEO_ID/view?usp=sharing ←←← **Replace this** |
| SRS Document                  | https://docs.google.com/document/d/1J6yLgQK9Ac2XJU789VaHqVuAVfUeyviW3YjiMMichSk/edit?usp=sharing |
| Live Deployed Application     | https://debo-tutor-collaboration.onrender.com |



---

### Problem Statement & Impact
In underserved regions of Ethiopia — especially **Benishangul-Gumuz** — students face critical barriers to academic success:
- Severe shortage of qualified tutors
- High cost or complete absence of private tutoring
- Reliance on inconsistent, location-bound informal study groups
- Limited access to supplementary learning materials

According to UNESCO (2022), Africa requires **17 million additional teachers by 2030** to achieve quality education goals. In rural and semi-urban Ethiopia, these gaps disproportionately affect secondary and university students preparing for national exams.

**Debo** addresses this challenge by providing a **free, student-only, mobile-first peer learning platform** that enables collaborative question-asking, answering, and knowledge sharing — embodying the Ethiopian cultural value of **"Debo"** (collective effort).

---

### Implemented Features (Aligned with SRS & System Design)

| Feature                        | Status   | Description |
|--------------------------------|----------|-----------|
| User Registration & Login      | Done     | Simple username + 4-digit PIN (ideal for students) |
| Secure Logout                  | Done     | Full session termination |
| Post Academic Questions        | Done     | Title, description, subject selection |
| Reply to Questions             | Done     | Threaded, timestamped responses |
| View All Questions             | Done     | Chronological listing (newest first) |
| Responsive & Mobile-First UI   | Done     | Works flawlessly on low-end devices |
| Publicly Accessible Deployment | Done     | Live on Render.com with PostgreSQL |



---

### Technology Stack
- **Framework:** Django 4.x (Python)
- **Database:** SQLite (development) → PostgreSQL (production)
- **Frontend:** HTML5, CSS3, Django Templates (fully responsive)
- **Authentication:** Django Auth with custom 4-digit PIN
- **Deployment:** Render.com (free tier), Gunicorn, Whitenoise
- **Build Automation:** `Procfile` + `build.sh`

---

### How to Run Locally (100% Reproducible Steps)

```bash
# 1. Clone the repository
git clone https://github.com/Betelhemf567/debo-tutor.git
cd debo-tutor

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Create admin user
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver

Open your browser → http://127.0.0.1:8000

Register → /register/
Login → /login/
Start posting and answering questions!

Production Deployment (Live & Publicly Accessible)
Live URL: https://debo-tutor-collaboration.onrender.com
Deployed successfully using:

Render.com free web service
Automatic builds triggered by GitHub pushes
build.sh script: install → collectstatic → migrate
Free PostgreSQL database add-on
All environment variables securely configured

Anyone worldwide can access, register, and use the platform immediately.


Project Structure
textdebo-tutor/
├── core/                  # Main app (models, views, URLs, templates)
├── templates/             # register.html, login.html, question list, etc.
├── static/                # Custom CSS and assets
├── debo/                  # Project settings & WSGI
├── manage.py
├── Procfile               # Deployment command
├── build.sh               # Build automation
├── requirements.txt
└── README.md              # ← You are reading this


Made with passion, purpose, and true collective effort
Betelhem Feleke Chelebo
African Leadership University 
For every student who has ever needed help but had no one to ask.

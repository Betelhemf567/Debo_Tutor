# **Debo – Student Peer-to-Peer Learning Platform**  
*(ደቦ – ተማሪዎች ብቻ የሚጠቀሙበት የጋራ ትምህርት መድረክ)*  

**🌐 Live URL:** https://debo-tutor-collaboration.onrender.com  

---

## 📌 **Overview**

**Debo** is a mobile-first, student-only peer learning platform designed to support secondary and university students in underserved regions—especially **Benishangul-Gumuz, Ethiopia**.

It enables students to:

- Ask academic questions  
- Receive peer answers  
- Share study materials  
- Learn collaboratively using low bandwidth  

Debo is inspired by the Ethiopian cultural value **“ደቦ”**, meaning *collective effort*.  
This aligns with SDG 4 (Quality Education) by expanding access to free learning support.

---

## ❗ **Problem Statement**

Students in underserved Ethiopian regions face:

- Shortage of qualified tutors  
- High cost or lack of private tutoring  
- Limited supplementary study materials  
- Inconsistent, location-based study groups  
- Lack of structured academic support  

UNESCO (2022) states that **Africa needs 17 million more teachers by 2030**, meaning millions of students remain without academic assistance.

**Debo** solves this by providing a **free, accessible, student-driven academic support platform**.

---

## 🎯 **Core Features (Aligned with SRS)**

| Feature | Status |
|--------|--------|
| User Registration | ✔ Completed |
| Login / Logout | ✔ Completed |
| Post Questions | ✔ Completed |
| Reply to Questions | ✔ Completed |
| View Questions Feed | ✔ Completed |
| Upload Resources (PDF/JPG/PNG/TXT ≤10MB) | ✔ Completed |
| Download Resources | ✔ Completed |
| Mobile-First UI | ✔ Completed |
| Public Deployment | ✔ Completed |

All features match the SRS functional requirements and system design diagrams.

---

## 🏗 **Technology Stack**

### **Backend**
- Django 4.x  
- Django ORM  
- Django Authentication  

### **Frontend**
- HTML5  
- CSS3  
- Django Template Engine  

### **Database**
- SQLite (Development)  
- PostgreSQL (Production on Render)  

### **Deployment**
- Render.com  
- Gunicorn  
- Whitenoise  
- `Procfile` + `build.sh` automation  

---

## 💻 **How to Run the Project Locally**

```bash
# 1. Clone the repository
git clone https://github.com/Betelhemf567/Debo_Tutor.git
cd Debo_Tutor

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create admin account
python manage.py createsuperuser  
# → Enter username (e.g., admin)
# → Enter email (you can press Enter to skip)
# → Enter a strong password (or 4-digit PIN like 1234 for testing)
# → Confirm password
# → Success! Admin account created

# 5. Start the development server
python manage.py runserver
```

Now open the browser:  
👉 http://127.0.0.1:8000

---

## 🧪 **Using the System (Local or Live)**

### 🔐 **Register**
`/register/`

### 🔑 **Login**
`/login/`

### 📝 **Ask a Question**
- Go to the home page  
- Click **“Ask Question”**  

### 💬 **Reply to Questions**
- Open any question  
- Submit a reply  

### 📁 **Upload Resources**
- Upload academic files (PDF, JPG, PNG, TXT ≤10MB)  

### ⬇ **Download Resources**
- Accessible from the resources page  

### 🚪 **Logout**
- Ends the current session safely  

---

## 🌍 **Production Deployment Details**

**Live URL:** https://debo-tutor-collaboration.onrender.com  

Deployment stack:

- Render Web Service (Free Tier)  
- PostgreSQL Database  
- Auto-builds triggered by GitHub commits  
- Static files served via Whitenoise  
- `build.sh` handles:  
  - dependency installation  
  - `collectstatic`  
  - database migration  

Anyone can access the platform publicly.

---

## 📁 **Project Structure**

```
debo-tutor/
├── core/                # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       ├── login.html
│       ├── register.html
│       ├── question_list.html
│       ├── question_detail.html
│       └── upload_resource.html
├── static/              # CSS, images
├── media/               # Uploaded resources
├── debo/                # Project settings
├── manage.py
├── Procfile
├── build.sh
├── requirements.txt
└── README.md
```

---

## 📚 **Documentation Links**

| Item | Link |
|------|------|
| **SRS  Document** | *https://docs.google.com/document/d/1J6yLgQK9Ac2XJU789VaHqVuAVfUeyviW3YjiMMichSk/edit?usp=sharing* |
| **Demo Video (5–10 min)** | *https://youtu.be/n1K-43y6_I0* |
| **Live Deployed App** | https://debo-tutor-collaboration.onrender.com/ |

---

## 👩🏽‍💻 **Author**

**Betelhem Feleke Chelebo**  
African Leadership University  

Built with passion, purpose, and the belief that **students learn best together**.

---

## ❤️ **Mission Statement**

Debo is created *for every student who ever needed help but had no one to ask*.  
This platform empowers students through **collaboration, community, and culture**.

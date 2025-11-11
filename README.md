# 📝 Blog Application

## 📘 Overview  
The *Blog Application* is a full-stack web platform built using *Python (Django Framework)* that allows users to create, read, update, and delete blog posts.  
It provides an interactive space for writers and readers, featuring authentication, post management, commenting, and user-friendly content organization.  
This project demonstrates the implementation of Django’s MVT architecture, database integration, and secure user authentication.

---

## 🚀 Features
- 🧑‍💻 *User Authentication* – Sign up, login, and logout functionalities with password protection.  
- 📰 *Create & Manage Posts* – Add, edit, and delete blog posts dynamically.  
- 💬 *Comment Section* – Readers can share thoughts and feedback on posts.  
- 🏷 *Categories & Tags* – Organize content by categories and tags for easy navigation.  
- 🔍 *Search Functionality* – Quickly find posts by title or keyword.  
- 📅 *Timestamps* – Each post includes a created and updated date.  
- 🎨 *Responsive UI* – Clean, mobile-friendly design using HTML, CSS, and Bootstrap.  

---

## 🛠 Tech Stack
*Frontend:* HTML, CSS, Bootstrap  
*Backend:* Python, Django Framework  
*Database:* SQLite / MySQL  
*Tools & Libraries:* Django ORM, Django Admin, Crispy Forms, REST Framework  

---

## ⚙ Installation & Setup
1. *Clone the Repository*
   ```bash
   git clone https://github.com/yourusername/django-blog-app.git
   cd django-blog-app
   Create a Virtual Environment

python -m venv env
source env/bin/activate     # (Linux/Mac)
env\Scripts\activate        # (Windows)


Install Dependencies

pip install -r requirements.txt


Run Database Migrations

python manage.py makemigrations
python manage.py migrate


Create Superuser

python manage.py createsuperuser


Run the Server

python manage.py runserver


Access the Application

Open your browser and visit: http://127.0.0.1:8000

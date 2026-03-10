# 🌙 Iftar Name Selection System

A simple **Django web application** for managing Iftar name registration.  
Users can submit their name and select an Iftar name through a clean and responsive interface.

---

## ✨ Features

- 📝 Iftar name registration form
- 🎨 Ramadan-themed UI with background image
- 📱 Fully responsive design (mobile + desktop)
- 🎉 Thank You page with celebration popper animation
- 🗂 Django static files support for images
- 🔒 Simple and secure form submission using Django forms

---

## 🛠 Technologies Used

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **JavaScript**

---

## 📂 Project Structure

```
iftar-name-selection
├─ manage.py
├─ names
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_iftar_delete_name.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ static
│  │  └─ images
│  │     └─ ifthar.jpg
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ nameSelection
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ README.md
├─ requirements.txt
└─ templates
   ├─ register.html
   └─ thanks.html

```
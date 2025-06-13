# 🎓 CertiGen - Web Certificate Generator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-success?logo=django)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

CertiGen is a simple web-based application that allows you to generate, download, and manage SSL certificates with customizable options such as key size, validity period, and hash algorithm.

---

## 🚀 Features

- ✅ Web interface to generate X.509 certificates  
- 📥 Download certificates in `.crt` format  
- 🧹 Delete expired certificates  
- 🔐 Customize key size, hash algorithm, and domain name  
- 🌐 REST API to interact programmatically  

---

## 🛠 Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/your-username/certigen.git
cd certigen
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

### 🌐 Access the Application
Once the server is running, open your browser and go to:

```bash
http://127.0.0.1:8000/
```
You can now use the interface to generate, download, and manage certificates.
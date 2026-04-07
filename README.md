```markdown
# Full-Stack E-Commerce Platform

A robust, production-ready E-Commerce web application built with Django. This project features a fully dynamic frontend synced with a customized Django Admin panel, a serverless cloud database architecture, and secure media storage. 

Developed as an internship task for **DEVELOPERSHUB**.

---

## Key Features

* **Dynamic Inventory Management:** Complete CRUD operations for Products, Categories, Brands, and Suppliers.
* **Custom Admin Interface:** Enhanced Django admin panel with inline models for managing multiple product images and specifications seamlessly.
* **Serverless Cloud Database:** Integrated with **Supabase** (PostgreSQL) ensuring high availability, zero latency sleep, and persistent data storage.
* **Cloud Media Storage:** Uses **Cloudinary** CDN for storing and serving user-uploaded product images permanently.
* **Optimized Static Files:** Configured with **WhiteNoise** for lightning-fast and efficient static file serving in production environments.
* **Serverless Deployment:** Fully deployed and optimized for **Vercel** serverless architecture.

## Technology Stack

* **Backend:** Python, Django 6.0.2
* **Database:** PostgreSQL via Supabase
* **Media Storage:** Cloudinary
* **Static Files:** WhiteNoise
* **Hosting/Server:** Vercel (Serverless)
* **Frontend:** HTML, CSS, JavaScript

## Live Demo
**URL:** (https://developershub-task-phase-1-vercel-d.vercel.app/)

---

## Local Setup & Installation

Follow these steps to run the project on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/mabdullah236/DEVELOPERSHUB-task-Phase-1-Vercel-deploy-.git
cd ecommerce_project
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory and add your cloud credentials securely:
```env
DATABASE_URL=your_supabase_postgresql_url
CLOUD_NAME=your_cloudinary_cloud_name
CLOUD_API_KEY=your_cloudinary_api_key
CLOUD_API_SECRET=your_cloudinary_api_secret
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser to view the application. Access the admin panel at `http://127.0.0.1:8000/admin`.

---

## 👨‍💻 Author
**Muhammad Abdullah**
Software Engineering Student | Python Developer | QA analyst
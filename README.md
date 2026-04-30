# 🚀 Learning Django REST Framework

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A personal learning repository where I explore and practice **Django REST Framework (DRF)** — building REST APIs with Django. This repo documents my journey from the basics to more advanced concepts.

---

## 📚 What I'm Learning

- Setting up Django & DRF from scratch
- Creating models, serializers, and views
- API authentication (Token, Session, JWT)
- Class-based views & ViewSets
- Routers and URL configuration
- Permissions and throttling
- Filtering, searching, and pagination
- Testing REST APIs

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Django | Web framework |
| Django REST Framework | API toolkit |
| SQLite3 | Local development database |
| Postman / Thunder Client | API testing |

---

## ⚙️ Getting Started

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

---

## 📁 Project Structure

```
├── myapp/
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # App URL routing
│   └── tests.py           # Unit tests
├── project/
│   ├── settings.py        # Project settings
│   └── urls.py            # Root URL config
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

---

## 📝 Notes & Progress

> I'll update this section as I learn new things!

- [x] Django project setup
- [x] Created first API endpoint
- [ ] Authentication with JWT
- [ ] Pagination and filtering
- [ ] Deploying the API

---

## 🤝 Contributing

This is a personal learning repo, but feel free to open an issue or suggest improvements!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Made with ❤️ while learning Django REST Framework
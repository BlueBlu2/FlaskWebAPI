# FlaskWebAPI 🚀

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**FlaskWebAPI** is a step-by-step **Flask-based REST API** created for **practice and learning purposes**. Each step introduces a new concept or tool to enhance the project and reinforce backend development skills.

---

## 📌 Project Overview

This project is structured as a hands-on learning journey in backend API development with Flask. The app evolves incrementally with real-world practices like Docker, API validation, database interaction, and more.

---

## 🛠️ Development Steps

### ✅ 1. Create REST API Endpoints

- Built RESTful routes using **Flask**.
- Supported CRUD operations (GET, POST, PUT, DELETE).
- Organized using Blueprints for scalable structure.

### ✅ 2. Add Docker & Docker Compose

- Added a `Dockerfile` to containerize the application.
- Used `docker-compose.yml` for managing services.
- Enabled **debug mode** for development with auto-reloading.

### ✅ 3. Integrate Flask-Smorest, Swagger UI & Marshmallow

- Adopted **Flask-Smorest** for modular route handling.
- Enabled **Swagger UI** for auto API documentation.
- Added **Marshmallow** for schema validation.

### ✅ 4. Store Data in a SQL Database with SQLAlchemy & SQLite

- Integrated **SQLAlchemy** as the ORM.
- Used **SQLite** for simplicity and portability.
- Defined models and schema.
- Full CRUD operations on persistent data.

---

## 📦 Tech Stack

- **Python 3.10+**
- **Flask**
- **Flask-Smorest**
- **Marshmallow**
- **SQLAlchemy**
- **SQLite**
- **Docker / Docker Compose**
- **Swagger UI**

---

## 📁 Project Structure

```
FlaskWebAPI/
├── app/                  # Core application
│   ├── models/           # SQLAlchemy models
│   ├── routes/           # API Blueprints
│   ├── schemas/          # Marshmallow schemas
│   ├── __init__.py       # App factory
│   └── ...
├── migrations/           # Alembic (if added later)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 How to Run

### ▶️ Using Docker (Recommended)

```bash
docker-compose up --build
```

- App will run at: `http://localhost:5000`
- Swagger UI: `http://localhost:5000/swagger-ui`

---

### 🔧 Manual Setup (Without Docker)

```bash
# Clone the repository
git clone https://github.com/BlueBlu2/FlaskWebAPI.git
cd FlaskWebAPI

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
flask run
```

---

## 📬 Example API Call

```bash
curl -X POST http://localhost:5000/items      -H "Content-Type: application/json"      -d '{"name": "Book", "price": 19.99}'
```

---

## 📖 API Documentation

Interactive Swagger UI is available at:

👉 [http://localhost:5000/swagger-ui](http://localhost:5000/swagger-ui)

---

## 🚧 Work in Progress

Planned next steps:

- 🔐 Add JWT-based authentication
- 🛢️ Switch to PostgreSQL for production
- 🧪 Add unit and integration tests
- ☁️ Prepare for deployment (e.g., Render, Heroku, Fly.io)

---

## 🤝 Contributions

This is a personal learning project. If you’re learning too, feel free to fork it, experiment, or give feedback!

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE.txt) file for details.

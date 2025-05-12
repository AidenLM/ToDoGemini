ToDoGemini
ToDoGemini is a simple yet powerful task management web application built using FastAPI and SQLAlchemy. It allows users to create, view, and manage their tasks through a clean and intuitive interface.

🚀 Features
Create, list, and delete to-do tasks

Fast and asynchronous API endpoints using FastAPI

SQLAlchemy-based database operations

Modern UI with HTML, CSS, and JavaScript

SQLite database support for lightweight storage

🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/AidenLM/ToDoGemini.git
cd ToDoGemini
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Initialize the database:

bash
Copy
Edit
alembic upgrade head
Run the application:

bash
Copy
Edit
uvicorn main:app --reload
Open your browser and go to http://localhost:8000 to use the app.

📁 Project Structure
csharp
Copy
Edit
ToDoGemini/
├── alembic/            # Database migration scripts
├── routers/            # API routers
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── alembic.ini         # Alembic configuration
├── database.py         # Database connection setup
├── main.py             # Application entry point
├── models.py           # SQLAlchemy models
├── requirements.txt    # Python dependencies
└── todoai_app.db       # SQLite database file
🤝 Contributing
Contributions are welcome! Here's how to contribute:

Fork the repository

Create a new branch: git checkout -b feature-name

Make your changes and commit them: git commit -m 'Add feature'

Push to your branch: git push origin feature-name

Open a pull request

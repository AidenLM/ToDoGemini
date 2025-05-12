# ToDoGemini

**ToDoGemini** is a simple yet powerful task management web application built using FastAPI and SQLAlchemy. It allows users to create, view, and manage their tasks through a clean and intuitive interface.

## 🚀 Features

- Create, list, and delete to-do tasks  
- Fast and asynchronous API endpoints using FastAPI  
- SQLAlchemy-based database operations  
- Modern UI with HTML, CSS, and JavaScript  
- SQLite database support for lightweight storage  

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AidenLM/ToDoGemini.git
   cd ToDoGemini
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   alembic upgrade head
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and go to `http://localhost:8000` to use the app.

## 📁 Project Structure

```
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
```

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. Fork the repository  
2. Create a new branch: `git checkout -b feature-name`  
3. Make your changes and commit them: `git commit -m 'Add feature'`  
4. Push to your branch: `git push origin feature-name`  
5. Open a pull request  

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

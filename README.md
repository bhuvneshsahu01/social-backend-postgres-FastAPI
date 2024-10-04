# Social Media Backend Server

This project is a backend server for a social media site, built using **FastAPI** and **PostgreSQL**. The backend supports all essential features of a social media platform, including user authentication, CRUD operations for posts and user data, and more.

## Features

- **User Authentication**: Secure user registration, login, and JWT-based authentication.
- **CRUD Operations**: Full support for creating, reading, updating, and deleting posts and user profiles.
- **Database Integration**: Utilizes PostgreSQL for data storage and SQLAlchemy as the ORM.
- **API Endpoints**: RESTful API endpoints for handling user actions, posts, comments, likes, etc.
- **Scalable Architecture**: Built with FastAPI for asynchronous request handling and scalability.
- **Input Validation**: Strong input validation using Pydantic.

## Tech Stack

- **FastAPI**: A modern, fast web framework for building APIs.
- **PostgreSQL**: An open-source relational database management system.
- **SQLAlchemy**: The Python SQL toolkit and ORM for handling database operations.
- **Pydantic**: Data validation and settings management using Python type hints.
- **JWT**: JSON Web Tokens for secure authentication.

## Installation

### Prerequisites

- **Python 3.8+** installed on your system.
- **PostgreSQL** database setup and running.

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Ensure PostgreSQL is running.
    - Create a new database in PostgreSQL for the project.

5. **Configure environment variables**:
    - Create a `.env` file in the root of the project to store database credentials and other environment settings:
    ```ini
    DATABASE_URL=postgresql://username:password@localhost/dbname
    SECRET_KEY=your_jwt_secret_key
    ```

6. **Run the database migrations**:
    ```bash
    alembic upgrade head
    ```

7. **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```

    The server will start on `http://127.0.0.1:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation, available at:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **Redoc**: `http://127.0.0.1:8000/redoc`

## Usage

Once the server is running, you can interact with the API using tools like **Postman**, **cURL**, or via the Swagger UI provided by FastAPI.

### Example Endpoints

- **User Registration**: `POST /auth/register`
- **User Login**: `POST /auth/login`
- **Create a Post**: `POST /posts/`
- **Get All Posts**: `GET /posts/`
- **Like a Post**: `POST /posts/{post_id}/like`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

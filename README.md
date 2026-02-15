# LexiLearn

LexiLearn is a web-based learning platform built with FastAPI and MongoDB. It features user authentication, quiz functionality, and an admin dashboard for managing content.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **MongoDB**: You need a running MongoDB instance (cloud or local). This project uses MongoDB Atlas by default.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd LexiLearn
    ```

2.  **Create a virtual environment (Recommended):**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Environment Variables:**

    The project uses a `.env` file for configuration. Ensure you have a `.env` file in the root directory with the following keys:

    ```env
    MONGO_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>?retryWrites=true&w=majority
    SECRET_KEY=your_secret_key_here
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=120
    ```

    > **Note:** Do not commit your `.env` file to version control if it contains production secrets.

## Running the Application

You can run the application using `uvicorn`:

1.  **Start the server:**

    ```bash
    uvicorn app.main:app --reload
    ```

    The `--reload` flag enables hot-reloading for development.

2.  **Access the application:**

    Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Project Structure

-   `app/`: Core application logic.
    -   `main.py`: Entry point of the application.
    -   `database.py`: Database connection and configuration.
    -   `auth.py`: Authentication logic.
    -   `routes/`: API and Web routes.
    -   `templates/`: HTML templates (Jinja2).
    -   `static/`: Static assets (CSS, JS, Images).
-   `requirements.txt`: Python dependencies.
-   `.env`: Environment variables.

## Usage

-   **Home Page**: `/`
-   **Sign In**: `/signin`
-   **Sign Up**: `/signup`
-   **Dashboard (Admin)**: `/dashboard`
-   **Quiz (User)**: `/quiz`

## Contributing

1.  Fork the repository.
2.  Create a feature branch.
3.  Commit your changes.
4.  Push to the branch.
5.  Open a Pull Request.

## License

[MIT License](LICENSE)

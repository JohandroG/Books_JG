from books_app import app
from books_app.controllers import authors, books


if __name__ == "__main__":
    app.run(debug=True)
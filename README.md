# Welcome to the Hackathon Guide

This is a simple Flask application to help you get started with web development in Python.

## Features

- Minimal Flask setup
- Example routes
- Easy to extend

## Getting Started

1. **Clone the repository (choose one method):**

    - **HTTPS:**
        ```bash
        git clone https://github.com/ItamarShalev/hackathon_guide.git
        cd hackathon_guide
        ```
    - **SSH:**
        ```bash
        git clone git@github.com:ItamarShalev/hackathon_guide.git
        cd hackathon_guide
        ```

2. **Install dependencies:**
    ```bash
    python -m pip install uv
    ```

3. **Run the app:**
    ```bash
    uv run flask --app client:app run --reload --port 80 --host 0.0.0.0
    ```

4. **Visit in your browser:**
    ```
    http://127.0.0.1/
    ```

5. **Run fastAPI:**
    ```bash
    uv run uvicorn server:app --reload --port 8000 --host 0.0.0.0
    ```

6. **Visit fastAPI in your browser:**
    ```
    http://127.0.0.1:8000
    ```

## How to:

- **Add a new python package:**
  - Run the following command:
    ```bash
    uv add <package_name>
    ```

- **Run jupyter notebook:**
  - Run the following command:
    ```bash
    uv run jupyter nbconvert --to notebook --execute jupyter_file.ipynb --output output.ipynb
    ```


## Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python.org](https://www.python.org/)

---

Happy coding!

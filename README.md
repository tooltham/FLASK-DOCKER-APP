# Flask Docker Application

This project is a simple Flask application that is containerized using Docker. It serves as a starting point for building RESTful APIs with Flask.

## Project Structure

```
flask-docker-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   └── templates
│       └── post_with_js.html
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd flask-docker-app
   ```

2. **Build the Docker image:**

   ```bash
   docker build -t flask-docker-app .
   ```

3. **Run the application using Docker Compose:**
   ```bash
   docker-compose up
   ```

## Usage

Once the application is running, you can access the API at `http://localhost:5000`. You can test the endpoints using tools like Postman or curl.

## Dependencies

The application requires the following dependencies, which are listed in `app/requirements.txt`:

- Flask

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.

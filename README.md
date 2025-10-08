Stock Tracker WebSocket

A real-time stock tracking web application built with Django, Celery, Redis, and Django Channels.

This project demonstrates asynchronous task management and live data updates using WebSockets.
Features

    Real-time stock updates using WebSockets

    Background task processing with Celery + Redis

    Scalable and asynchronous architecture in Django

    Clean separation of tasks, consumers, and views

Tech Stack

    Backend: Django

    Asynchronous Tasks: Celery

    Message Broker: Redis

    Real-Time Communication: Django Channels / WebSockets

    Database: PostgreSQL / SQLite

Installation
1. Clone the repository

git clone [https://github.com/your-username/Stock-Tracker-Websocket.git](https://github.com/your-username/Stock-Tracker-Websocket.git)
cd Stock-Tracker-Websocket


2. Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Configure Django settings

Update backend/settings.py with your database and Redis configuration.
Running the Project
1. Start Redis server

redis-server


2. Start Celery worker

celery -A backend worker -l info


3. Start Django development server

python manage.py runserver


4. Start Django Channels (ASGI server)

daphne backend.asgi:application


Project Structure

backend/           # Django project folder
core/              # App with consumers, tasks, views
requirements.txt   # Python dependencies


Usage

    Connect to the WebSocket endpoint to receive live stock updates

    Celery tasks fetch and process stock data in the background, sending real-time updates to connected clients

Contribution

Contributions are welcome!

    Fork the repository

    Create a branch for your feature or bugfix

    Open a pull request

License

This project is licensed under the MIT License.

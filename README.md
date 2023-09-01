# Project Title

## Prerequisites

- Python 3.x
- Docker

## Using venv

### Installation
1. Clone this repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Run the project: `python manage.py runserver`

## Using Docker

### Building the Docker Image
docker build -t your_image_name .
docker run -it your_image_name
# PokeCollector

## Overview
This application is a Django-based platform designed to serve as a comprehensive database for Pokémon Trading Card collections. Utilizing the Pokémon TCG API, the app allows users to navigate through various Pokémon card sets that are stored in a SQL database. Users can create accounts, log in, and log out to personalize their experience, adding or removing cards from their collection as they wish.

## Features
- Browse Pokémon Card Sets: Navigate through a variety of Pokémon trading card collections (sets) retrieved via the Pokémon TCG API.
- Detailed Card View: Within each set, view detailed information and images for each individual card.
- Add to Collection: Logged-in users can add cards from any set to their personal collection.
- Remove from Collection: Cards can also be easily removed from a user's collection if they are logged in.
- User Authentication: Create an account, log in, and log out to personalize and save your card collection.

## Installation
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

## Technologies Used
- Django
- Python
- HTML/CSS
- SQL/SQLite


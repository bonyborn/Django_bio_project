# Django Bio App

A simple Django application that allows users to create and view a personal biography.

## Project Overview

This project is built using Django and demonstrates how to:
- Use Django's Model-View-Template (MVT) architecture.
- Create and render forms.
- Store and display user-submitted data using models.
- Render dynamic content in templates.

## Features

- Create a personal bio with:
  - Full Name
  - Age
  - Profession
  - Short Bio
  - Hobbies
- View the submitted bio.

## Installation

1. **Clone the Repository**
   git clone https://github.com/bonyborn/django_bio_app.git
   cd django_bio_app

2. **Setup Virtual Environment**
   python -m venv venv
   venv\Scripts\activate

3. **Install Dependencies**
   pip install django
   pip install -r requirements.txt

   Create a requirements.txt using:
   pip freeze > requirements.txt

4. **Run Migrations**
   python manage.py migrate

5. **Start Development Server**
   python manage.py runserver

## Access the App

- Create your bio: http://127.0.0.1:8000/bio/create/
- View your bio: http://127.0.0.1:8000/bio/view/

## Author

Boniface Muvea  
GitHub: bonyborn
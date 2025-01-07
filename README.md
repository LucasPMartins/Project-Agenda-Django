<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=1e81b0&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?font=JetBrains+Mono&color=1e81b0&size=45&center=true&vCenter=true&width=1000&lines=Project+Agenda)](https://git.io/typing-svg)

## Contact Management System

This is a Django-based web application for managing contacts. It allows users to create, update, delete, and search for contacts. Each contact can have a picture, and users can register, log in, and manage their profiles.

<img width=100% src="https://github.com/user-attachments/assets/b148c05e-d8c4-4d02-a847-a2684c68ec15" />

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Forms](#forms)
- [Templates](#templates)
- [Static Files](#static-files)
- [Tools](#-tools)
- [Languages](#-languages)

## Features

- User authentication (registration, login, logout)
- Create, update, delete, and view contacts
- Search contacts by name, email, or phone
- Pagination for contact list
- User profile management
- Upload and display contact pictures

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin site:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

- **Admin Site**: Access the admin site at `http://127.0.0.1:8000/admin` to manage users and contacts.
- **User Registration**: Register a new user at `http://127.0.0.1:8000/user/register`.
- **Login**: Log in at `http://127.0.0.1:8000/user/login`.
- **Create Contact**: Create a new contact at `http://127.0.0.1:8000/contact/create`.
- **View Contacts**: View the list of contacts at `http://127.0.0.1:8000`.
- **Search Contacts**: Search for contacts using the search bar on the homepage.

## Models

- **Category**: Represents a category for contacts.
- **Contact**: Represents a contact with fields for first name, last name, phone, email, description, picture, category, and owner.

## Forms

- **ContactForm**: Form for creating and updating contacts.
- **RegisterForm**: Form for user registration.
- **RegisterUpdateForm**: Form for updating user profile.

## Templates

- **base.html**: Base template for the application.
- **contact.html**: Template for viewing a single contact.
- **create.html**: Template for creating and updating contacts.
- **index.html**: Template for listing contacts.
- **login.html**: Template for user login.
- **register.html**: Template for user registration.
- **user_update.html**: Template for updating user profile.

## Static Files

- **style.css**: CSS file for styling the application.

## 🛠 Tools:
![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-0D1117?style=for-the-badge&logo=visual-studio-code&logoColor=007ACC&labelColor=0D1117)
![Git](https://img.shields.io/badge/-Git-0D1117?style=for-the-badge&logo=git&labelColor=0D1117)
![GitHub](https://img.shields.io/badge/-GitHub-0D1117?style=for-the-badge&logo=github&labelColor=0D1117)
![Windows](https://img.shields.io/badge/-Windows-0D1117?style=for-the-badge&logo=windows&logoColor=0a58ee)
![Django](https://img.shields.io/badge/Django-0D1117?style=for-the-badge&logo=django&logoColor=41CD52)
![SQLite](https://img.shields.io/badge/sqlite-0D1117?style=for-the-badge&logo=sqlite&logoColor=%2307405e)

## 👨‍💻 Languages
![Python](https://img.shields.io/badge/python-0D1117?style=for-the-badge&logo=python&logoColor=ffdd54)
![CSS3](https://img.shields.io/badge/css3-0D1117?style=for-the-badge&logo=css3&logoColor=%231572B6)
![HTML5](https://img.shields.io/badge/html5-0D1117?style=for-the-badge&logo=html5&logoColor=%23E34F26)

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=1e81b0&height=120&section=footer"/>

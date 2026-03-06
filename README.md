# Flask RESTful Users API

## About Project

This is a simple REST API project built using Flask and Flask-RESTful.
In this project I created APIs to perform CRUD operations on users.

The data is stored in an in-memory list (temporary data) just for learning REST API concepts.

This project helped me understand:

* REST API basics
* HTTP methods
* Flask-RESTful Resource classes
* Working with JSON data

---

## Technologies Used

* Python
* Flask
* Flask-RESTful

---

## Project Files

app.py → Main Flask application file
requirements.txt → Python dependencies
README.md → Project description

---

## How to Run the Project

1. Create virtual environment

```
python -m venv venv
```

2. Activate virtual environment

Windows

```
venv\Scripts\activate
```

3. Install required packages

```
pip install -r requirements.txt
```

4. Run the application

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## API Endpoints

Get all users

```
GET /users
```

Add new user

```
POST /users
```

Example JSON

```
{
"name": "Rahul",
"age": 23
}
```

Get single user

```
GET /users/<id>
```

Update user

```
PUT /users/<id>
```

Delete user

```
DELETE /users/<id>
```

---

## What I Learned

* How REST APIs work
* HTTP methods (GET, POST, PUT, DELETE)
* Creating APIs using Flask-RESTful
* Sending and receiving JSON data

---

## Author

Srikanth

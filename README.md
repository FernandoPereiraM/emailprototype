## Mail API - Introduction and How to Use

Welcome to Mail API! This API provides functionalities for managing users, emails, and folders within your system. Whether you're building a mailing system or need to integrate email management features into your application, Mail API offers the tools you need.

### Introduction

Mail API simplifies the process of managing email-related operations, including user management, sending and receiving emails, and organizing emails into folders. With a set of intuitive endpoints, developers can seamlessly integrate these features into their applications, enhancing user experience and productivity.

### Technologies Used

Mail API is built using the following technologies:

- **Python**: The core language used for development.
- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **Django REST Framework (DRF)**: A powerful toolkit for building Web APIs in Django.
- **JWT (JSON Web Tokens)**: Used for user authentication and authorization.
- **SQLite/PostgreSQL**: The default and recommended databases supported by Django for data storage.

### How to Use

Here's a summary of the API endpoints and their functionalities:

### Users

- **List Users and Create User**
  - `GET http://localhost:8000/users/`: Retrieves a list of users.
  - `POST http://localhost:8000/users/`: Creates a new user. Provide a JSON object with username and password.

- **Get, Update, and Delete User**
  - `GET http://localhost:8000/user/<user_id>/`: Retrieves user details by ID.
  - `PUT http://localhost:8000/user/<user_id>/`: Updates user details. Send a JSON object with username and password.
  - `DELETE http://localhost:8000/user/<user_id>/`: Deletes a user by ID.

- **User Login**
  - `POST http://localhost:8000/login/`: Allows users to log in. Provide a JSON object with username and password. The server returns a JWT token, which should be included in the Authorization header of subsequent requests as a Bearer token.

### Emails

- **List Emails and Create Email**
  - `GET http://127.0.0.1:8000/emails/`: Retrieves a list of emails.
  - `POST http://127.0.0.1:8000/emails/`: Creates a new email. Provide a JSON object with user, receiver, sender, subject, and body.

- **Get, Update, and Delete Email**
  - `GET http://127.0.0.1:8000/email/<email_id>/`: Retrieves email details by ID.
  - `PUT http://127.0.0.1:8000/email/<email_id>/`: Updates email details. Send a JSON object with user, receiver, sender, subject, and body.
  - `DELETE http://127.0.0.1:8000/email/<email_id>/`: Deletes an email by ID.

- **List User's Emails and Sent Emails**
  - `GET http://127.0.0.1:8000/mylist/<str:email>/`: Retrieves a list of emails received by a specific user (inbox). Provide the username (receiver) as a parameter.
  - `GET http://127.0.0.1:8000/sendlist/<str:email>/`: Retrieves a list of emails sent by a specific user. Provide the username (sender) as a parameter.

### Folders

- **List Folders, Create Folder, and Manage Folder**
  - `GET http://localhost:8000/folders/`: Retrieves a list of folders.
  - `POST http://localhost:8000/folders/`: Creates a new folder. Provide a JSON object with folder name and other details.
  - `GET http://localhost:8000/folders/<folder_id>/`: Retrieves folder details by ID.
  - `PUT http://localhost:8000/folders/<folder_id>/`: Updates folder details. Send a JSON object with folder name and other details.
  - `DELETE http://localhost:8000/folders/<folder_id>/`: Deletes a folder by ID.

These endpoints enable you to manage users, emails, and folders effectively, facilitating actions such as creation, retrieval, updating, and deletion of user accounts, emails, and folders. Additionally, you can list emails based on different criteria such as inbox and sent items.

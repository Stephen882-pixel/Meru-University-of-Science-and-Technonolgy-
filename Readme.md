

# Meru University Science Innovators Club API Documentation

## Introduction
The Meru University Science Innovators Club API provides a set of endpoints for managing events, subscribing to the newsletter, and contacting the club administrators. This API is designed to be used by the club's administrators and members.

## Authentication
To access certain protected endpoints, such as sending the newsletter, authentication is required. The API uses a JWT-based authentication system with access and refresh tokens.

### Obtaining Access and Refresh Tokens
To obtain an access and refresh token, make a POST request to the `/api/token/` endpoint with the following payload:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

The response will contain the access and refresh tokens:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

To use the access token, include it in the `Authorization` header of your requests as a Bearer token:

```
Authorization: Bearer <access_token>
```

If the access token expires, you can use the refresh token to obtain a new access token by making a POST request to the `/api/token/refresh/` endpoint with the following payload:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## Endpoints

### Events

#### Create an Event
**Endpoint**: `POST /events/`
**Request Body**:
```json
{
    "name": "Python Programming Workshop",
    "title": "Beginner's Guide to Python",
    "description": "Learn the fundamentals of Python programming in this hands-on workshop. Suitable for those new to coding.",
    "image": "base64_image_string_goes_here",
    "date": "2023-06-15T10:00:00Z",
    "location": "Online",
    "organizer": "John Doe",
    "contact_email": "info@example.com",
    "is_virtual": true,
    "registration_link": "https://example.com/python-workshop-registration"
}
```

#### List All Events
**Endpoint**: `GET /events/`

#### Update an Event
**Endpoint**: `PUT /events/{id}/`
**Request Body**:
```json
{
    "name": "AI Ethics Workshop",
    "title": "Navigating the Ethical Landscape of AI",
    "description": "Explore the key ethical considerations in the development and deployment of artificial intelligence systems.",
    "image": "base64_image_string_goes_here",
    "date": "2023-09-01T09:00:00Z",
    "location": "Hybrid (in-person and virtual)",
    "organizer": "Jane Smith",
    "contact_email": "jane@example.com",
    "is_virtual": true,
    "registration_link": "https://example.com/ai-ethics-workshop"
}
```

#### Partially Update an Event
**Endpoint**: `PATCH /events/{id}/`
**Request Body**:
```json
{
    "organizer": "Collins Munene",
    "contact_email": "collinsmunene9@gmail.com"
}
```

#### Delete an Event
**Endpoint**: `DELETE /events/{id}/`

### Newsletter

#### Subscribe to the Newsletter
**Endpoint**: `POST /subscribe/`
**Request Body**:
```json
{
    "email": "newtonwamiti0@gmail.com"
}
```

#### Send a Newsletter
**Endpoint**: `POST /newsletter/`
**Request Body**:
```json
{
    "subject": "Newsletter Title",
    "message": "Newsletter content goes here..."
}
```

### Contact Us
**Endpoint**: `POST /contact/`
**Request Body**:
```json
{
    "message_name": "Onyango Stephen Omondi",
    "message_email": "stephenondeyo0@gmail.com",
    "message": "Subject: Assistance Required for FileNotFoundError in Django Project\nDear Admin,\nI hope this message finds you well. I am reaching out regarding an issue I encountered while\nworking on my Django project, specifically related to file handling in my settings configuration.\nBest regards,\nStephen\n"
}
```


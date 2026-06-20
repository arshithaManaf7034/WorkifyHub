# WorkifyHub – Local Services Marketplace

## Overview

WorkifyHub is a full-stack Django-based service marketplace that connects buyers with skilled service providers. Users can register as Buyers or Sellers, post jobs, showcase skills, express interest in opportunities, communicate through chat, book appointments, and leave ratings and reviews.

The platform is inspired by modern service marketplaces such as Fiverr, Upwork, and Urban Company, with a focus on local service discovery and direct interaction between customers and workers.

---

## Features

### Authentication & User Management

* User Registration
* Login & Logout
* Buyer and Seller Roles
* Profile Management
* Role-Based Access Control

---

### Seller Features

* Create and manage professional profiles
* Add multiple skills
* Upload profile image
* Upload portfolio/work images
* Upload demo videos
* Add education and certifications
* Set pricing and experience details
* View jobs matching their skills
* Express interest in buyer-posted jobs
* Manage appointments
* Chat with buyers

---

### Buyer Features

* Browse available workers
* View detailed seller profiles
* Post jobs and service requests
* View interested sellers
* Chat with sellers
* Book appointments
* Rate and review completed services

---

### Job Marketplace

* Job Posting System
* Skill-Based Job Matching
* Seller Interest System
* Buyer Job Dashboard
* Interested Seller Tracking

Workflow:

Buyer Posts Job
↓
Matching Sellers View Job
↓
Seller Shows Interest
↓
Buyer Reviews Interested Sellers
↓
Buyer Initiates Chat
↓
Appointment Booking
↓
Service Completion
↓
Rating & Review

---

### Communication System

* Real-time style chat interface
* Buyer-Seller messaging
* Appointment coordination

---

### Appointment Management

* Appointment Requests
* Accept/Reject Workflow
* Appointment Tracking
* Status Updates

---

### Review & Rating System

* Star Ratings
* Written Reviews
* Seller Reputation Tracking

---

### Admin Dashboard

* User Management
* Skill Management
* Job Management
* Appointment Management
* Rating Management
* Job Interest Monitoring

---

## Technology Stack

### Backend

* Python
* Django

### Database

* SQLite (Development)
* PostgreSQL Ready

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Deployment

* GitHub
* Render

---

## Project Structure

```text
workifyhub/
│
├── config/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── media/
├── static/
├── manage.py
└── requirements.txt
```

---

## Core Models

### UserProfile

Stores seller and buyer information.

### Skill

Stores marketplace skills and categories.

### Job

Stores buyer job postings.

### JobInterest

Tracks seller interest in jobs.

### Appointment

Handles appointment bookings.

### Rating

Stores ratings and reviews.

### Message

Handles buyer-seller communication.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd workifyhub
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Start server:

```bash
python manage.py runserver
```

---

## Future Enhancements

* Google Maps Integration
* Geolocation-Based Job Matching
* Distance-Based Worker Search
* Payment Gateway Integration
* Buyer Verification
* Seller Verification
* Real-Time Notifications
* Advanced Analytics Dashboard
* Mobile Application

---

## Author

**Arshitha K M**

Python Developer | Django Developer | AI-Driven Python Developer

GitHub:
https://github.com/arshithaManaf7034

---

## License

This project is developed for educational and portfolio purposes.

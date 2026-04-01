# Charles Ozebo Portfolio

A backend-focused personal portfolio built with Flask.  
This project showcases my work, technical stack, social links, downloadable resume, and a contact form that sends messages directly to my email.

## Features

- Backend-focused portfolio homepage
- Responsive design for desktop and mobile
- Project showcase with GitHub and live links
- Resume download endpoint
- Contact form with email delivery
- Health check endpoint
- Simple Flask structure with clean template rendering

## Tech Stack

- Python
- Flask
- Flask-CORS
- HTML
- CSS
- JavaScript
- python-dotenv
- SMTP email integration

## Project Structure

```bash
portfolio/
├── app.py
├── .env.example
├── templates/
│   └── index.html
├── static/
│   ├── chigo.jpg
│   ├── css/
│   │   └── site.css
│   ├── js/
│   │   └── site.js
│   ├── resume/
│   │   └── Charles_Ozebo_Resume.pdf
│   └── project-thumbs/
└── .gitignore
```
Setup
1. Clone the repository
git clone https://github.com/Charles-DEV-1/<your-repo-name>.git
cd portfolio

3. Create a virtual environment
python -m venv venv

3. Activate the virtual environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

5. Install dependencies
pip install flask flask-cors python-dotenv

6. Create your environment file
Copy .env.example to .env and update it with your credentials:

env

EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
RECIPIENT_EMAIL=your-email@gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587


Run the Project
python app.py
The app runs at:
http://127.0.0.1:5000
Available Routes
Home Page
http GET /
Renders the portfolio homepage.

Download Resume
http GET /resume
Downloads the resume file from:
static/resume/Charles_Ozebo_Resume.pdf

Contact Form API
http POST /api/contact
Request Body
json

{
  "fullName": "Your Name",
  "email": "you@example.com",
  "message": "Hello Charles"
}

FEATURED PROJECTS
Authentication System
Learning Platform API
Event Management App
LogBook
Result Processing App

CONTACT
LinkedIn: https://www.linkedin.com/in/ozebo-charles-b88471343/
GitHub: https://github.com/Charles-DEV-1/
Instagram: https://www.instagram.com/charles_dev_1/
Notes
Make sure your email credentials are valid if you want the contact form to work.
For Gmail, use an App Password instead of your normal account password.
Keep .env private and never push it to GitHub.


License
This project is open for learning and personal inspiration.

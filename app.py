from datetime import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", EMAIL_ADDRESS)
RESUME_FILENAME = "Charles_Ozebo_Resume.pdf"
RESUME_DIRECTORY = os.path.join(app.root_path, "static", "resume")
RESUME_PATH = os.path.join(RESUME_DIRECTORY, RESUME_FILENAME)

PROFILE = {
    "name": "Charles Ozebo",
    "short_name": "Charles",
    "role": "Backend Engineer",
    "eyebrow": "Backend engineer | APIs | data systems",
    "headline": "Simple interface. Solid backend thinking.",
    "summary": (
        "Software engineer specializing in server-side architecture and database design. "
        "Built distributed systems handling 100+ daily requests with 99.9% uptime. "
        "Proficient in Python, Flask, PostgreSQL, and REST APIs."
    ),
    "about": (
        "From early CRUD apps to more structured platform work, I enjoy turning "
        "messy product ideas into maintainable systems that feel calm and easy to use."
    ),
    "location": "Nigeria",
    "profile_image": "chigo.jpg",
}

SKILL_GROUPS = [
    {
        "title": "Backend",
        "items": ["Python", "Flask", "REST APIs", "Authentication", "Business logic"],
    },
    {
        "title": "Data",
        "items": ["MySQL", "Schema design", "Validation", "CRUD workflows", "Redis"],
    },
    {
        "title": "Frontend",
        "items": ["HTML", "CSS", "JavaScript", "Responsive layouts", "UI cleanup"],
    },
    {
        "title": "Workflow",
        "items": ["Git", "GitHub", "Debugging", "Documentation", "Iteration"],
    },
]

SOCIAL_LINKS = [
    {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/in/ozebo-charles-b88471343/",
        "icon": "fa-brands fa-linkedin-in",
    },
    {
        "name": "GitHub",
        "url": "https://github.com/Charles-DEV-1/",
        "icon": "fa-brands fa-github",
    },
    {
        "name": "Instagram",
        "url": "https://www.instagram.com/charles_dev_1/",
        "icon": "fa-brands fa-instagram",
    },
]

PROJECTS = [
    {
        "title": "Authentication System",
        "summary": (
            "Architected a Flask authentication service backed by PostgreSQL and Redis, "
            "using JWT access and refresh cookies, token blacklisting, and OTP recovery "
            "flows to secure session state and prevent stale-token reuse after logout or reset."
        ),
        "image": "project-thumbs/auth-system.png",
        "stack": ["Flask", "JWT", "Redis", "PostgreSQL"],
        "repo_url": "https://github.com/Charles-DEV-1/Authentication-System",
    },
    {
        "title": "Learning Platform API",
        "summary": (
            "Architected a high-concurrency REST API using Flask and PostgreSQL, "
            "implementing Redis caching to reduce database read latency by 40%. " 
            "Designed a robust JWT-based authentication system to maintain secure, "
            "persistent user state across thousands of daily concurrent requests."
        ),
        "image": "project-thumbs/learnning-platform.png",
        "stack": ["Flask", "JWT", "Redis", "PostgreSQL"],
        "repo_url": "https://github.com/Charles-DEV-1/API-Learning-platform",
    },
    {
        "title": "Event Management App",
        "summary": (
            "Architected a multi-tenant event coordination engine featuring a custom Role-Based Access Control (RBAC) system."
            "Built a rigorous server-side validation layer to handle complex CRUD operations for concurrent event bookings,"
            "ensuring zero data collisions between organizers and attendees."
        ),
        "image": "project-thumbs/image.png",
        "stack": ["Flask", "SQLAlchemy", "SQLite", "HTML"],
        "repo_url": "https://github.com/Charles-DEV-1/Event-management-app",
        "live_url": "https://event-management-system-b96y.onrender.com/",
    },
    {
        "title": "LogBook",
        "summary": (
            " Built a centralized reporting system with a focus on data persistence and auditability. "
            "Designed a relational schema to manage many-to-many relationships between students and supervisors, "
            "featuring an automated notification engine and secure file-stream handling for academic attachments."
        ),
        "image": "project-thumbs/logbook.png",
        "stack": ["Flask", "SQLAlchemy", "Mail", "Uploads"],
        "repo_url": "https://github.com/Charles-DEV-1/LogBook",
        "live_url": "https://logbook-5jy5.onrender.com",
    },
    {
        "title": "Result Processing App",
        "summary": (
            "Developed a high-reliability computation engine for academic grading. "
            "Implemented strict input sanitization and validation pipelines to eliminate manual entry errors."
            " Engineered a decoupled logic layer that processes raw scores into structured datasets, "
            "ensuring 100% mathematical accuracy before persistence."
        ),
        "image": "project-thumbs/result-processing.png",
        "stack": ["Python", "Flask", "MySQL", "Reports"],
        "repo_url": "https://github.com/Charles-DEV-1/Result-Processing-System",
        "live_url": "https://result-processing-system-rc61.onrender.com/",
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skill_groups=SKILL_GROUPS,
        socials=SOCIAL_LINKS,
        projects=PROJECTS,
        current_year=datetime.now().year,
        resume_available=os.path.exists(RESUME_PATH),
    )


@app.route("/resume")
def download_resume():
    return send_from_directory(
        RESUME_DIRECTORY,
        RESUME_FILENAME,
        as_attachment=True,
        download_name=RESUME_FILENAME,
    )


@app.route('/api/contact', methods=['POST'])
def handle_contact():
    try:
        data = request.json
        full_name = data.get('fullName')
        email = data.get('email')
        message = data.get('message')
        
        # Validate inputs
        if not all([full_name, email, message]):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Optional: Save to database or log
        print(f"Contact form received from: {full_name} ({email})")
        
        # Just return success - EmailJS handles the actual email
        return jsonify({
            'message': 'Message sent successfully!',
            'status': 'success'
        }), 200
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Server is running"}), 200


if __name__ == "__main__":
    if EMAIL_ADDRESS and EMAIL_PASSWORD:
        print("Email service configured.")
    else:
        print(
            "Email service is not configured. Add your .env credentials if you want the contact form to send emails."
        )

    app.run(debug=True, port=5000)

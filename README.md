# Job Portal Web Application

A full-featured job portal built with Flask and PostgreSQL.

## Features

- User authentication (Job Seekers, Employers, Admin)
- Job posting and management
- Job search with filters
- Application system
- Responsive Bootstrap 5 UI

## Technologies

- Python
- Flask
- PostgreSQL
- Bootstrap 5
- Flask-Login
- Flask-WTF

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-portal.git
   cd job-portal
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env`:
   ```
   DATABASE_URL=postgresql://username:password@localhost/jobportal
   SECRET_KEY=your-secret-key-here
   ```

5. Initialize the database:
   ```bash
   flask init-db
   flask create-admin
   ```

6. Run the application:
   ```bash
   flask run
   ```

## License

MIT

from app import create_app
from app.models import db, User, Job, Application

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Initialize the database."""
    db.create_all()
    print("Database initialized.")

@app.cli.command("create-admin")
def create_admin():
    """Create an admin user."""
    admin = User(
        username="admin",
        email="admin@jobportal.com",
        role="admin"
    )
    admin.set_password("admin123")
    db.session.add(admin)
    db.session.commit()
    print("Admin user created.")

if __name__ == "__main__":
    app.run(debug=True)
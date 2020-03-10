from REST_API_SQLAlchemy.RESTAPI import app
from REST_API_SQLAlchemy.db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

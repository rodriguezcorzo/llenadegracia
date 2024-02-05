from flask import render_template
from . import app_routes

@app_routes.route('/')
def index():
    return render_template('index.html')

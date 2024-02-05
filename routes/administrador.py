from flask import render_template, redirect, url_for, request
from . import app_routes

@app_routes.route('/administrador')
def administrador():
    return redirect(url_for('administrador'))
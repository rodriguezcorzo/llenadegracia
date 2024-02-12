from flask import render_template, Blueprint, redirect, url_for, request

administrador_bp = Blueprint('administrador_bp', __name__)

@administrador_bp.route('/administrador')
def administrador():
    return render_template('administrador.html')
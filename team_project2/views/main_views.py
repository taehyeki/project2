
from flask import Blueprint, render_template
from .login_required import *
from team_project2 import client
bp = Blueprint('main', __name__, url_prefix='/')
db = client.team_project2

@bp.route('/cat')
@login_required
def cat():
    comments = list(db.comments.find({}).sort( [( "created_time", -1 )] ))
    return render_template('cat.html',comments=comments)
@bp.route('/dog')
@login_required
def dog():
    return render_template('dog.html')
@bp.route('/join')
@logout_required
def join_page():
    return render_template('join.html')

@bp.route('/login')
@logout_required
def login_page():
    return render_template('login.html')

@bp.route('/')
@login_required
def home_page():
    return render_template('index.html')


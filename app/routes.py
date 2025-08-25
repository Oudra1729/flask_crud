from flask import Blueprint, render_template, redirect, url_for, request
from .models import User
from . import db

# تعريف الـ Blueprint هنا فقط
main = Blueprint('main', __name__)

@main.route('/')
def index_page():
    users = User.query.all()
    return render_template("index.html", users=users)

@main.route('/add_user_page')
def add_user_page():
    return render_template("add_user.html")

@main.route('/add_user_form', methods=['POST'])
def add_user_form():
    name = request.form['name']
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('main.index_page'))

@main.route('/edit_user_page/<int:id>')
def edit_user_page(id):
    user = User.query.get_or_404(id)
    return render_template("edit_user.html", user=user)

@main.route('/edit_user_form/<int:id>', methods=['POST'])
def edit_user_form(id):
    user = User.query.get_or_404(id)
    user.name = request.form['name']
    db.session.commit()
    return redirect(url_for('main.index_page'))

@main.route('/delete_user/<int:id>')
def delete_user_page(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.index_page'))

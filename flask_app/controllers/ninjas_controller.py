from flask import render_template, request, redirect, session
from flask_app import app # needs the app to direct routes
from flask_app.models.ninja_model import Ninja #needs to import Ninja class to use class methods
from flask_app.models.dojo_model import Dojo

@app.route('/ninjas')
def new_ninja_form():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def add_ninja():
    Ninja.create(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')

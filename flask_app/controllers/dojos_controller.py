from flask import render_template, request, redirect, session
from flask_app import app # needs the app to direct routes
from flask_app.models.dojo_model import Dojo

#displays the@ wecome page to direct to the home
@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template("dojos_home.html", all_dojos=all_dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')


@app.route('/dojos/<int:id>')
def view_one_dojo(id):
    one_dojo = Dojo.get_one({'id':id})
    return render_template("dojo_show.html", one_dojo=one_dojo)
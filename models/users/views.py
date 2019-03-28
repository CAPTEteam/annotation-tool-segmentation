from flask import Blueprint, request, session, render_template, url_for
from werkzeug.utils import redirect


user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        password = request.form['password']
        project = request.form['project']
        if password == "happylabel":
            session['login_name'] = "guest"
            session['project'] = project
            return redirect(session['project'])
        else:
            return "wrong password"

    return render_template("users/login.html")






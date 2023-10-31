from flask import Blueprint, render_template

o_que_e_scrum_blueprint = Blueprint('oqueescrum', __name__)


@o_que_e_scrum_blueprint.route('/')
def index():
    return render_template("OQueEScrum.html")

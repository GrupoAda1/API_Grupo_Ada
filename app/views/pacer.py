from flask import Blueprint, render_template

pacer_blueprint = Blueprint('pacer', __name__)


@pacer_blueprint.route('/pacer')
def index():
    return render_template("Pacer.html")

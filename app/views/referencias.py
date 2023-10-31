from flask import Blueprint, render_template

referencias_blueprint = Blueprint('referencias', __name__)


@referencias_blueprint.route('/referencias')
def index():
    return render_template("Referencias.html")

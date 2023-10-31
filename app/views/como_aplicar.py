from flask import Blueprint, render_template

como_aplicar_blueprint = Blueprint('comoaplicar', __name__)


@como_aplicar_blueprint.route('/comoaplicar')
def index():
    return render_template("ComoAplicar.html")

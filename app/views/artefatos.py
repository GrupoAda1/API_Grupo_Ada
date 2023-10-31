from flask import Blueprint, render_template

artefatos_blueprint = Blueprint('artefatos', __name__)


@artefatos_blueprint.route('/artefatos')
def index():
    return render_template("Artefatos/BacklogProduto.html")

@artefatos_blueprint.route('/artefatos/backlogSprint')
def backlog_sprint():
    return render_template("Artefatos/BacklogSprint.html")

@artefatos_blueprint.route('/artefatos/entregaSprint')
def entrega_sprint():
    return render_template("Artefatos/EntregaSprint.html")


from flask import Blueprint, render_template

eventos_blueprint = Blueprint('eventos', __name__)


@eventos_blueprint.route('/eventos')
def index():
    return render_template("Eventos/Eventos.html")

@eventos_blueprint.route('/eventos/execucao')
def execucao_sprint():
    return render_template("Eventos/ExecucaoSprint.html")

@eventos_blueprint.route('/eventos/retrospectiva')
def retrospectiva_sprint():
    return render_template("Eventos/RetrospectivaSprint.html")

@eventos_blueprint.route('/eventos/reuniao')
def reuniao_diaria():
    return render_template("Eventos/ReuniaoDiaria.html")

@eventos_blueprint.route('/eventos/revisao')
def revisao_sprint():
    return render_template("Eventos/RevisaoSprint.html")

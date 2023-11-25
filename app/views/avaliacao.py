from flask import Blueprint, render_template
from app.components.pacer import pacer
from app.constrants.pacer import NOTAS

avaliacao_blueprint = Blueprint('avaliacao', __name__)


@avaliacao_blueprint.route('/avaliacao')
def index():
    return render_template("Avaliacao.html", po_pacer=pacer("po"), sm_pacer=pacer("sm"), dev_pacer=pacer("dev"), notas=NOTAS)

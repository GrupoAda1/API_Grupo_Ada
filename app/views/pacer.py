from flask import Blueprint, render_template
from app.components.pacer import pacer
from app.constrants.pacer import NOTAS

pacer_blueprint = Blueprint('pacer', __name__)


@pacer_blueprint.route('/pacer')
def index():
    return render_template("Pacer.html", po_pacer=pacer("po"), sm_pacer=pacer("sm"), dev_pacer=pacer("dev"), notas=NOTAS)

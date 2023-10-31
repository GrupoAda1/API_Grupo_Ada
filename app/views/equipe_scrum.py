from flask import Blueprint, render_template

equipe_scrum_blueprint = Blueprint('equipe_scrum', __name__)


@equipe_scrum_blueprint.route('/equipe')
def index():
    return render_template("EquipeScrum/DevTeam.html")

@equipe_scrum_blueprint.route('/equipe/productOwner')
def product_owner():
    return render_template("EquipeScrum/ProductOwner.html")

@equipe_scrum_blueprint.route('/equipe/scrumMaster')
def scrum_master():
    return render_template("EquipeScrum/ScrumMaster.html")


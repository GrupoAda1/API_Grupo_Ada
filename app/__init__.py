from flask import Flask
from config.config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config.from_object(app_config[config_name])

    from app.views.como_aplicar import como_aplicar_blueprint
    from app.views.referencias import referencias_blueprint
    from app.views.o_que_e_scrum import o_que_e_scrum_blueprint
    from app.views.eventos import eventos_blueprint
    from app.views.equipe_scrum import equipe_scrum_blueprint
    from app.views.artefatos import artefatos_blueprint
    from app.views.avaliacao import avaliacao_blueprint

    app.register_blueprint(como_aplicar_blueprint)
    app.register_blueprint(referencias_blueprint)
    app.register_blueprint(o_que_e_scrum_blueprint)
    app.register_blueprint(eventos_blueprint)
    app.register_blueprint(equipe_scrum_blueprint)
    app.register_blueprint(artefatos_blueprint)
    app.register_blueprint(avaliacao_blueprint)

    return app


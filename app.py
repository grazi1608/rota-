from flask import Flask, render_template 
from models import db

from controllers.motorista_controller import motorista_bp
from controllers.veiculo_controller import veiculo_bp
from controllers.corrida_controller import corrida_bp
from controllers.meta_controller import meta_bp


def create_app():
    # Ajustamos o Flask para saber que suas pastas ficam dentro de 'view'
    app = Flask(__name__, template_folder="view/templates", static_folder="view/static")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rotamais.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "rotamais"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registro dos Blueprints da API (JSON)
    app.register_blueprint(motorista_bp, url_prefix="/motoristas")
    app.register_blueprint(veiculo_bp, url_prefix="/veiculos")
    app.register_blueprint(corrida_bp, url_prefix="/corridas")
    app.register_blueprint(meta_bp, url_prefix="/metas")

    # --- ROTAS PARA ABRIR AS PÁGINAS NO NAVEGADOR ---
    
    @app.route("/")
    def index():
        # Redireciona a página inicial para a tela de motoristas
        return render_template("motoristas.html")

    @app.route("/tela/motoristas")
    def tela_motoristas():
        return render_template("motoristas.html")

    @app.route("/tela/veiculos")
    def tela_veiculos():
        return render_template("veiculos.html")

    @app.route("/tela/corridas")
    def tela_corridas():
        return render_template("corridas.html")

    @app.route("/tela/metas")
    def tela_metas():
        return render_template("meta.html")  # Abre o seu arquivo meta.html

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
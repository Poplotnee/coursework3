from flask import Blueprint, render_template

error_handlers_blueprint = Blueprint('errors', __name__, template_folder='templates')


@error_handlers_blueprint.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404


@error_handlers_blueprint.app_errorhandler(500)
def handle_500(err):
    return render_template('500.html'), 500

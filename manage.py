from gubr import app, db
from gubr.models import User# , Service

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Service': Service}
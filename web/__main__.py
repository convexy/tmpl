# controller

from flask import Flask
from web.views.menu import bp as bp_menu
from web.views.maintenance import bp as bp_maintenance

app = Flask(__name__)
app.secret_key = "**tmpl**"
app.register_blueprint(bp_menu)
app.register_blueprint(bp_maintenance)

if __name__ == "__main__":
    app.run(debug=True)
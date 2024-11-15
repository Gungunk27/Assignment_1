from flask import Flask
from routes.user_routes import user_routes
from routes.admin_routes import admin_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

# Register Blueprints
app.register_blueprint(user_routes, url_prefix="/user")
app.register_blueprint(admin_routes, url_prefix="/admin")

if __name__ == "__main__":
    app.run(debug=True)

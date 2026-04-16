from flask import Flask
from database import db
from routes import main
import os

app = Flask(__name__)

# 🔐 SECRET KEY (session fix)
app.secret_key = "super_secret_key_placement_ai"

# 📂 Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 🔗 Initialize DB
db.init_app(app)

# 🔗 Register Blueprint
app.register_blueprint(main)

# 📦 Create DB tables (first run)
with app.app_context():
    db.create_all()

# 🚀 Run App
if __name__ == "__main__":
    app.run(debug=True)
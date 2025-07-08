# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from model import db, Contact  # ⬅️ importing db and Contact from model.py
import os

app = Flask(__name__)
# CORS(app, origins=["http://localhost:3000"])
CORS(app, origins=["http://localhost:3000", "https://admirable-nasturtium-234bae.netlify.app"])

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@localhost:5432/contactform'
# postgresql://postgres:KDkgRATTYnCBkDTLFIckZhepgohBamsp@nozomi.proxy.rlwy.net:57850/railway
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/api/contact', methods=['POST'])
def save_contact():
    data = request.get_json()
    contact = Contact(
        name=data['name'],
        email=data['email'],
        description=data['description']
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message': 'Contact saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

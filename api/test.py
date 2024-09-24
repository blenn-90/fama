import sqlite3
from flask import Blueprint, Response, request, jsonify
from db_alchemy import db
from sqlalchemy import create_engine
from data.models import Review
from data.models import Influencer
import csv


test_bp = Blueprint('test', __name__)

# Ripulire il database
@test_bp.route("/test/reset", methods=['GET', 'POST'])
def reset_database():
    db.drop_all()
    return jsonify({"message": "Database reset"})

# Reinserire i dati
@test_bp.route("/test/insert", methods=['GET', 'POST'])
def insert_data():
    user = Influencer(
            'FedericoFrusciante',
            'Youtube',
            'Cinema',
            'https://www.youtube.com/@FedericoFrusciante'
        )
    db.session.add(user)
    db.session.commit()
    user = Influencer(
            'PeppeFilmico',
            'Instagram',
            'Cinema',
            'https://www.instagram.com/peppefilmico'
        )
    db.session.add(user)
    db.session.commit()

    with open('data/csv/frusciante_1kvoted.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        data = list(reader)
        i=0
        for row in data:
            if i == 0:
                i = 1
                continue
            name = row[6][9:]
            a,b,c = name.partition('- Minirece')
            review = Review(a, 'https://www.youtube.com/watch?v=' + row[0], 1, row[7], row[5] + '/5' )
            db.session.add(review)
            db.session.commit()
   
    return jsonify({"message": "Data inserted"})
import sqlite3
from flask import Blueprint, Response, request, jsonify
from db_alchemy import db
from data.models import Influencer
import json

influencer_bp = Blueprint('influencer', __name__)
@influencer_bp.route('/api/influencer')
def get_all():
    print('-> api request')
    print('--> /api/influencer api start')
    influencers = Influencer.query.all()
    influencers_dict = [Influencer.to_dict(influencer) for influencer in influencers]
    influencers_json = json.dumps(influencers_dict)
    print('--> /api/influencer api end')
    return influencers_json

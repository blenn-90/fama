from flask import Blueprint, request, jsonify
from data.models import Review
import json

review_bp = Blueprint('review', __name__)

@review_bp.route('/api/review')
def get_all():
    print('-> api request start')
    print('--> /api/review api start')

    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    offset = (page - 1) * per_page
    print("page " + str(page))
    reviews = Review.query.offset(offset).limit(per_page).all()
    reviews_dict = [Review.to_dict(review) for review in reviews]
    reviews_json = json.dumps(reviews_dict)
    print('--> /api/review api end')
    return reviews_json

@review_bp.route('/api/review/detail')
def get_detail():
    print('-> api request start')
    print('--> /api/review/detail api start')
    id = request.args.get('id')
    print('---> influencer id='+id)
    reviews = Review.query.filter_by(id_influencer=id)
    reviews_dict = [Review.to_dict(review) for review in reviews]
    reviews_json = json.dumps(reviews_dict)
    print('--> /api/review/detail api end')
    return reviews_json

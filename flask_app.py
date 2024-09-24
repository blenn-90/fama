from flask import Flask, render_template, request, Response, jsonify
from waitress import serve
from flask_paginate import Pagination, get_page_parameter
import sqlite3
from api.influencer import influencer_bp
from api.review import review_bp
from api.dashboard import dashboard_bp
from api.test import test_bp
from db_alchemy import db

print('-> initialize app')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
app.register_blueprint(influencer_bp)
app.register_blueprint(review_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(test_bp)

print('-> creating istance db')
with app.app_context():
    from data.models import Review
    from data.models import Influencer
    db.create_all()

#influencer
@app.route('/')
@app.route('/index')
@app.route('/influencers')
def influencers():
    print('-> page request')
    print('--> /influencers page start')
    heading = ("Name", "Platform", "Category", "Url")
    menu = [
            {'label':'Influencers','class':'active bg-gradient-primary', 'href':'/influencers', 'icon':'dashboard'}, 
            {'label':'Reviews','class':'', 'href':'/review', 'icon':'receipt_long'}
        ]
   
    print('--> /influencers page end')
    return render_template('influencer.html', 
                            title = "Influencers",
                            headings = heading, 
                            menu = menu
                            )
#position page
@app.route('/review')
def positions_def():
    print('-> page request')
    print('--> /review page start')
    heading = ("Influencer", "Vote", "Url")
    menu = [
            {'label':'Influencers','class':'', 'href':'/influencers', 'icon':'dashboard'}, 
            {'label':'Reviews','class':'active bg-gradient-primary', 'href':'/review','icon':'receipt_long'}
        ]
     
    print('--> /review page end')
    return render_template('review.html', 
                            title = "Reviews",
                            headings = heading, 
                            menu = menu
                            )


    
#influencer
@app.route('/influencers/detail')
def influencer():
    print('-> page request')
    print('--> /influencers/detail start')
    # Use the hidden input value of id from the form to get the rowid
    id = request.args.get('rowid')
    print('---> influencer id='+id)
    influencer = db.session.get(Influencer, id)
    heading = ("Influencer", "Vote", "Url")
    menu = [
            {'label':'Influencers','class':'active bg-gradient-primary', 'href':'/influencers', 'icon':'dashboard'}, 
            {'label':'Reviews','class':'', 'href':'/review','icon':'receipt_long'}
        ]
        
    print('--> /influencers/detail end')
    return render_template('influencer_detail.html', 
                            title = "Influencer Details",
                            influencer = influencer,
                            headings = heading, 
                            id = id,
                            menu = menu
                            )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
    print('->app started')


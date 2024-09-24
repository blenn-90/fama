from flask import Blueprint, Response, request, jsonify
from db_alchemy import db
from sqlalchemy import create_engine

# Ripulire il database
dashboard_bp = Blueprint('dashboard', __name__)

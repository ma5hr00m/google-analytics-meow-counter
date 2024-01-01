import re
from flask import Blueprint, request, jsonify
from app.utils.google_analytics_data import get_google_analytics_data

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.before_request
def validate_property_id():
    property_id = request.view_args.get('property_id')
    if property_id and not re.match(r'^\d{8,12}$', property_id):
        return jsonify({'message': 'invalid param'}), 400

@analytics_bp.route('/pv/<property_id>', methods=['GET'])
def get_page_views(property_id):
    metric_name = "screenPageViews"
    data = get_google_analytics_data(property_id, metric_name)
    print("Page Views:", data)
    return jsonify(data)

@analytics_bp.route('/uv/<property_id>', methods=['GET'])
def get_total_users(property_id):
    metric_name = "totalUsers"
    data = get_google_analytics_data(property_id, metric_name)
    print("Total Users:", data)
    return jsonify(data)
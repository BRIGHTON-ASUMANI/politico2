from flask import Blueprint
v1 = Blueprint('version1', __name__, url_prefix='/api/v1')


from app.api.version1.views import party_views
from app.api.version1.views import office_views
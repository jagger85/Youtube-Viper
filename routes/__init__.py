from .health_route import bp_health
from .speecher.speecher import bp_speecher
from .login_route import bp_login
from .sock_route import register_sock_routes

routes = [bp_health, bp_login, bp_speecher]

def register_routes(app):
    for route in routes:
        app.register_blueprint(route)
    
    # Register WebSocket routes
    register_sock_routes(app)


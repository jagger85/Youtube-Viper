from .health_route import bp_health
from .speecher_route import bp_speecher
from .sock_route import register_sock_routes
from .swagger_route import swaggerui_blueprint

routes = [bp_health, bp_speecher, swaggerui_blueprint]

def register_routes(app):
    for route in routes:
        app.register_blueprint(route)
    
    # Register WebSocket route
    register_sock_routes(app)

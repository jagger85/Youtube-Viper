from .health_route import bp_health

routes = [bp_health]

def register_routes(app):
    for route in routes:
        app.register_blueprint(route)


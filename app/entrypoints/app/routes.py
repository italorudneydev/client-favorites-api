def register_routes(app):
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"
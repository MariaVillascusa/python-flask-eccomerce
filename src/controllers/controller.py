from flask.views import MethodView

class IndexController(MethodView):
    def get(self):
        return 'BIENVENIDO'


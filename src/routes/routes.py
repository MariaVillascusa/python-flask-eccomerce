from src.controllers.controller import *
from src.controllers.errors import NotFoundController

routes = {
    'index_route': '/', 'index_controller': IndexController.as_view('index'),
    'not_found_route': 404, 'not_found_controller': NotFoundController.as_view('not_found')
}

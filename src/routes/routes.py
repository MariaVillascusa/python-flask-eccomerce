from src.controllers.controller import *
from src.controllers.errors import NotFoundController

routes = {
    'index_route': '/', 'index_controller': IndexController.as_view('index'),
    'delete_route': '/delete/product/<int:code>', 'delete_controller':DeleteProductController.as_view('delete'),
    'update_route': '/update/product/<int:code>', 'update_controller':UpdateProductController.as_view('update'),
    'categories_route': '/create/category', 'categories_controller': CreateCategoriesController.as_view('categories'),
    'show_categories_route': '/categories', 'show_categories_controller':ShowCategoriesController.as_view('show_categories'),
    'delete_category_route': '/delete/category/<int:id>', 'delete_category_controller':DeleteCategoryController.as_view('delete_category'),

    'not_found_route': 404, 'not_found_controller': NotFoundController.as_view('not_found')
}

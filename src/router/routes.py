
from ..views import LoginView


def get_routes(page):
    return {
        "/login": {
            "view": lambda: LoginView(page),
        },
    }

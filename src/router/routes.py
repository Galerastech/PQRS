from ..layouts import AuthLayout
from ..views import LoginView


def get_routes(page):
    return {
        "/login": {
            "view": lambda: LoginView(page),
            "layout": AuthLayout,
            "public": True,
        },
    }

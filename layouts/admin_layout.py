import flet as ft 

class AdminLayout:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return ft.Text("Admin Dashboard")
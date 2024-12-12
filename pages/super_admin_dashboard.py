import flet as ft

class SuperAdminDashboard:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return ft.Text("Super Admin Dashboard")
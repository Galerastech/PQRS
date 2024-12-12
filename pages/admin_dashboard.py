import flet as ft

class AdminDashboard:
    """
    This class implements the admin dashboard page.

    Attributes:
        page (ft.Page): The Flet page object that this class is associated with.
    """

    def __init__(self, page: ft.Page) -> None:
        """
        Initialize the AdminDashboard class.

        Args:
            page (ft.Page): The Flet page object that this class is associated with.
        """
        self.page = page

    def build(self) -> ft.Control:
        """
        Build the admin dashboard page.

        Returns:
            ft.Control: The Flet control that represents the admin dashboard page.
        """
        role = self.page.session.get("role")
        if role != "administrador":
            # If the user is not an administrator, clear the session and redirect to the login page
            self.page.session.clear()
            self.page.go("/login")
            return ft.Text("Acceso no autorizado")
            
        # If the user is an administrator, return the admin dashboard page
        return ft.Text("Dashboard")
from abc import abstractmethod
import flet as ft

class BaseLayout(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.content = None
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value
        if self.page:
            self.page.update()
    @abstractmethod
    def build(self):
        pass

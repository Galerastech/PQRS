from datetime import datetime, date
import flet as ft
from styles.text_colors import color as colores

class Fecha(ft.UserControl):
        def __init__(self, etiqueta: str, on_date_change=None):
            super().__init__()
            self.on_date_change = on_date_change
            self.datepicker = ft.DatePicker(
                first_date = date(2024, 10, 1),
                last_date = date(2028, 12, 31),
                on_change=self.change_date,
            )

            self.selected_date = None

            # Botón para abrir el DatePicker
            self.button = ft.ElevatedButton(
                etiqueta,
                color= colores.PRIMARY.value,
                icon_color= colores.PRIMARY.value,
                bgcolor= colores.SECONDARY.value,
                icon=ft.icons.CALENDAR_MONTH,
                on_click=self.open_date_picker,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            )

            self.controls = [self.button]

        def open_date_picker(self, e):
            self.datepicker.open = True
            self.update()

        def change_date(self, e):
            if self.datepicker.value:
                self.selected_date = self.datepicker.value.strftime("%d-%m-%y")
            if self.on_date_change:
                self.on_date_change(self.selected_date)
            self.update()

        def build(self):
            return ft.Column(
                [
                    self.button,
                    #self.selected_date,
                    self.datepicker,
                ]
            )
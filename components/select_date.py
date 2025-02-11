import datetime
import flet as ft
from styles.text_colors import color as colores

def seleccionar_date(etiqueta: str):
    class Fecha(ft.UserControl):
        def __init__(self):
            super().__init__()
            self.datepicker = ft.DatePicker(
                first_date=datetime.date(2024, 10, 1),
                last_date=datetime.date(2028, 12, 31),
                on_change=self.change_date,
            )

            self.selected_date = ft.Text()

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
            self.selected_date.value = self.datepicker.value
            self.update()

        def build(self):
            return ft.Column(
                [
                    self.button,
                    #self.selected_date,
                    self.datepicker,
                ]
            )

    return Fecha()

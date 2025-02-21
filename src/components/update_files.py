import flet as ft

def update_files_function(nombre_boton: str):
    class Subir_archivos(ft.Row):
        def __init__(self):
            super().__init__()
            self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
            self.selected_files = ft.Text()

            def pick_files(_):
                self.pick_files_dialog.pick_files(allow_multiple=True)

            self.controls = [
                ft.Container(
                    content= ft.Column(
                        controls= [
                            ft.ElevatedButton(
                            nombre_boton,
                            color= ft.colors.WHITE,
                            icon_color= ft.colors.WHITE,
                            bgcolor= "#094d3f",
                            width=200,
                            height=50,
                            icon=ft.icons.UPLOAD_FILE,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            on_click=pick_files,
                            ),
                            self.selected_files,
                            ]
                        ),
                    #margin= ft.margin.only(0,5,0,0)
                )
            ]

        def pick_files_result(self, e: ft.FilePickerResultEvent):
            self.selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelado!"
            )
            self.selected_files.update()

        def did_mount(self):
            self.page.overlay.append(self.pick_files_dialog)
            self.page.update()


        def will_unmount(self):
            self.page.overlay.remove(self.pick_files_dialog)
            self.page.update()
        
    return Subir_archivos()
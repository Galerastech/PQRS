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
                            color= ft.colors.BLACK,
                            icon_color= ft.colors.DEEP_PURPLE_500,
                            bgcolor= ft.colors.DEEP_PURPLE_100,
                            icon=ft.icons.UPLOAD_FILE,
                            on_click=pick_files,
                            ),
                            self.selected_files,
                            ]
                        ),
                    margin= ft.margin.only(50,0,0,0)
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
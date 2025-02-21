import flet as ft
from styles.text_colors import color as colores
from components.residente_components.ejemplo_peticiones import normas_convivencia


class ResponsiveNavBar(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.dlg_notificaciones = ft.AlertDialog(
            modal=True,
            content=ft.Container(
                content=ft.Column(
                    controls= [
                        ft.Text("Notificaciones", weight=ft.FontWeight.BOLD),
                        ft.Text("Aqui irian las fechas de radicacion"),
                        ft.Row(
                            controls=[
                                ft.Text("Aqui irian las notificaciones"),
                                ft.Checkbox()    
                            ]
                        ),
                    ],
                    spacing=10,
                    scroll="auto",
                )
            ), 
            actions=[
                ft.TextButton(
                    "Eliminar",
                    style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            bgcolor=colores.SECONDARY.value,
                            color=colores.PRIMARY.value
                        ),
                        #TODO: Hacer funcion para eliminar la notificacion
                        #on_click=lambda _: self.notificaciones.open = False
                        on_click = lambda e: self.close_dialog_notificaciones(e)
                    )
                ],
                actions_alignment=ft.MainAxisAlignment.END
        )

        self.indice_normas = ft.Text(
            value="",
            weight=ft.FontWeight.BOLD
        )

        self.titulo_normas = ft.Text(
            value="",
            weight=ft.FontWeight.BOLD
        )

        self.normas = ft.Text(
            value="",
        )

        self.residente = ft.TextField(
            label="Residente",
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.DEFAULT.value,
            multiline=True,
            width=400,
            autofocus=True
        )

        self.correo = ft.TextField(
            label="Correo Electronico",
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.DEFAULT.value,
            multiline=True,
            width=400,
            autofocus=True
            )

        self.contraseña = ft.TextField(
            label="Contraseña",
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.DEFAULT.value,
            password=True,
            can_reveal_password=True,
            multiline=True,
            width=400,
            autofocus=True
            )

        self.repetir_contraseña = ft.TextField(
            label="Confirmar Contraseña",
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.DEFAULT.value,
            password=True,
            can_reveal_password=True,
            multiline=True,
            width=400,
            autofocus=True
            )

        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
            )

        self.dlg_formulario = ft.AlertDialog(
            modal=True,
            content=ft.Container(
                content=ft.Column(
                    controls= [
                        ft.Text("Administración de Contraseñas",
                            weight=ft.FontWeight.BOLD,
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                            ),
                        self.residente,
                        self.correo,
                        self.contraseña,
                        self.repetir_contraseña,
                        ft.ElevatedButton(
                            text="Cambiar contraseña",
                            width=400,
                            height=50,
                            bgcolor=colores.SECONDARY.value,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            #TODO: add function for on_click=,
                            on_click = lambda e : self.close_dialog_formulario(e),
                            color=colores.PRIMARY.value
                        ),
                    ],
                    spacing=20,
                    scroll="auto",
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
        )

        self.dlg_normas = ft.AlertDialog(
            modal=True,
            content=ft.Container(
                content=ft.Column(
                    controls= [
                        ft.Text("Normas de Convivencia", weight=ft.FontWeight.BOLD, size=20),
                        ft.Row(
                            controls=[
                                self.normas,
                            ]
                        ),
                    ],
                    spacing=10,
                    scroll="auto",
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ), 
            actions=[
                ft.TextButton(
                "Cerrar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        bgcolor=ft.colors.RED_500,
                        color=colores.PRIMARY.value
                    ),
                    #TODO: Hacer funcion para eliminar la notificacion
                    on_click=lambda e: self.close_dialog_normas(e)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        self.componentenavbar = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.IconButton(ft.icons.HOME,
                        icon_color=colores.CONTENT.value,
                        icon_size=30,
                        tooltip="Home",
                        # on_click=lambda _: page.go("/home")
                        ),
                        width="50%",
                        alignment=ft.alignment.top_left
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Stack(
                                    controls=[
                                        ft.IconButton(ft.icons.NOTIFICATIONS, 
                                        icon_color=colores.CONTENT.value,
                                        icon_size=30,
                                        on_click=lambda e: self.open_notificaciones(e),
                                        ),
                                        ft.Container(
                                            width=10,
                                            height=10,
                                            bgcolor="red",
                                            border_radius=10,
                                            right=5,
                                            top=5,
                                            # visible=self.new_notifications,
                                        ),
                                    ],
                                ),
                                ft.IconButton(ft.icons.LIBRARY_BOOKS_ROUNDED,
                                icon_color=colores.CONTENT.value,
                                icon_size=30,
                                tooltip="Listado de Clientes",
                                on_click=lambda e: self.open_normas(e)
                                ),
                                ft.IconButton(ft.icons.PERSON,
                                icon_color=colores.CONTENT.value,
                                icon_size=30,
                                tooltip="Crear Registro",
                                on_click=lambda e: self.open_formulario(e)
                                ),
                            ],
                        ),
                        width="50%",
                        alignment=ft.alignment.top_right
                    ),
                ],
                width="100%",
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                #vertical_alignment=ft.CrossAxisAlignment.START
            ),
            width="100%",
            alignment=ft.alignment.top_left,
            bgcolor=colores.BACKGROUND.value,
            padding=10
        )
    
    def build(self):
        return self.componentenavbar

    def open_notificaciones(self, e):
        #TODO: Hacer funcion para recibir notificaciones y abrir la notificacion
        self.page.dialog = self.dlg_notificaciones
        self.dlg_notificaciones.open = True
        self.page.update()

    def open_normas(self, e):
        self.normas.value = ""
        for key, value in normas_convivencia.items():
            self.indice_normas.value = key
            self.normas.value += f"{key}. {value}\n"
            self.page.update()
        self.page.dialog = self.dlg_normas
        self.dlg_normas.open = True
        self.page.update()

    def open_formulario(self, e):
        self.page.dialog = self.dlg_formulario
        self.dlg_formulario.open = True
        self.page.update()

    def close_dialog_notificaciones(self, e):
        self.dlg_notificaciones.open = False
        self.page.update()

    def close_dialog_normas(self, e):
        self.dlg_normas.open = False
        self.page.update()

    def close_dialog_formulario(self, e):
        self.dlg_formulario.open = False
        self.page.update()
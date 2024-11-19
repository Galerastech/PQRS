import flet as ft


def main(page: ft.Page):
    page.title = "App PQRS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #Modal petición
    def handle_close(e):
        page.close(dlg_modal_p)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal_p = ft.AlertDialog(
        modal=True,
        title=ft.Text("Petición"),
        content=ft.Text("derecho que constitucionalmente tiene toda persona para presentar y solicitar, respetuosamente, una petición por motivos de interés general o particular. ¿Desea presentar una Petición?"),
        actions=[
            ft.TextButton("SI", on_click=handle_close),
            ft.TextButton("NO", on_click=handle_close),
        ]
    )

    #Modal Quejas
    def handle_close(e):
        page.close(dlg_modal_q)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal_q = ft.AlertDialog(
        modal=True,
        title=ft.Text("Queja"),
        content=ft.Text("Una Queja es una manifestación de insatisfacción con alguna de nuestras actuaciones/servicios. ¿Desea presentar una Queja?"),
        actions=[
            ft.TextButton("SI", on_click=handle_close),
            ft.TextButton("NO", on_click=handle_close),
        ]
    )

    #Modal Reclamos
    def handle_close(e):
        page.close(dlg_modal_r)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal_r = ft.AlertDialog(
        modal=True,
        title=ft.Text("Reclamo"),
        content=ft.Text("Un reclamo en servicio al cliente se define como una manifestación de disconformidad en relación a un producto, servicio u experiencia recibidos. ¿Desea presentar una Reclamo?"),
        actions=[
            ft.TextButton("SI", on_click=handle_close),
            ft.TextButton("NO", on_click=handle_close),
        ]
    )

    #Modal Sugerencias
    def handle_close(e):
        page.close(dlg_modal_s)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal_s = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sugerencia"),
        content=ft.Text("Una Sugerencia es la aportación de ideas, iniciativas o cualquier otro comentario relativo a nuestras actuaciones. ¿Desea presentar una Sugerencia?"),
        actions=[
            ft.TextButton("SI", on_click=handle_close),
            ft.TextButton("NO", on_click=handle_close),
        ]
    )

    #Modal Felicitaciones
    def handle_close(e):
        page.close(dlg_modal_f)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal_f = ft.AlertDialog(
        modal=True,
        title=ft.Text("Felicitación"),
        content=ft.Text("Una Felicitación es aquella expresión de satisfacción de un usuario del servicio, con relación a la prestación de un servicio. ¿Desea presentar una Felicitación?"),
        actions=[
            ft.TextButton("SI", on_click=handle_close),
            ft.TextButton("NO", on_click=handle_close),
        ]
    )


    page.add(
        ft.Text("¡ Elija el tipo de PQR !"),

        ft.ElevatedButton("PETISIÓN", width=150, bgcolor=ft.colors.BLUE_GREY_100, on_click=lambda e: page.open(dlg_modal_p)),
        ft.ElevatedButton("QUEJA", width=150, bgcolor=ft.colors.BLUE_GREY_100, on_click=lambda e: page.open(dlg_modal_q)),
        ft.ElevatedButton("RECLAMO", width=150, bgcolor=ft.colors.BLUE_GREY_100, on_click=lambda e: page.open(dlg_modal_r)),
        ft.ElevatedButton("SUGERENCIA", width=150, bgcolor=ft.colors.BLUE_GREY_100, on_click=lambda e: page.open(dlg_modal_s)),
        ft.ElevatedButton("FELICITACIÓN", width=150, bgcolor=ft.colors.BLUE_GREY_100, on_click=lambda e: page.open(dlg_modal_f)),
    )
<<<<<<< HEAD
    Niñoooooo
=======
>>>>>>> parent of 1398965 (add: first structure)


ft.app(main)
import flet as ft

class Formato_Menu(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        
        self.usuarios = create_card("U","USUARIOS",'Gestión de la base de datos de Usuarios que arriendan la app en modalidad de "software as a service"',ft.colors.WHITE,ft.colors.GREEN_800)
        
        self.clientes = create_card("C","CLIENTES","Gestión de los Contratos suscritos con los usuarios",ft.colors.WHITE,ft.colors.GREEN_800)
        
        self.dashboard = create_card("D","DASHBOARD","Métricas de uso de la app por parte de los usuarios",ft.colors.BLACK,ft.colors.AMBER_500)
        
        self.tools = create_card("T","TOOLS","Caja de herramientas para la gestión de la app",ft.colors.BLACK,ft.colors.AMBER_500)
        
        self.contenedor1 = ft.Container(
            col=6,
            content=[
                ft.Container(
                        content=[self.usuarios]
                    ),
                ]
            )
        
        self.contenedor2 = ft.Container(
            col=6,
            content=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=[self.clientes]
                            ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=[self.dashboard]
                                    ),
                                    ft.Container(
                                        content=[self.tools]
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            )
        
    
    def build(self):
        return ft.ResponsiveRow(
            controls=[
                self.contenedor1,
                self.contenedor2
            ]
        )
        
def create_card(inicial:str,titulo:str,descripcion:str,color_texto, color):
        return ft.Container(
            bgcolor = color,
            border_radius=10,
            padding=30,
            #expand= True,
            content=[
                ft.Stack(
                    controls=[
                        ft.Container(
                            content=ft.IconButton(ft.icons.RADIO_BUTTON_OFF,
                                                icon_size=35,
                                                icon_color= ft.colors.WHITE),
                            alignment=ft.alignment.top_right,
                            margin= 0
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(inicial, size=100, weight=ft.FontWeight.BOLD, color=color_texto),
                                ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color=color_texto),
                                ft.Text(descripcion, size=15, weight=ft.FontWeight.NORMAL, color= color_texto),
                            ],
                            spacing=10,
                            alignment= ft.MainAxisAlignment.START,
                            horizontal_alignment = ft.CrossAxisAlignment.START
                            )
                        ],
                    ),
                ],
                
        )
        
    #     self.usuarios = ft.Container(
    #         content=ft.Column(
    #             controls=[
    #                 ft.IconButton(ft.icons.RADIO_BUTTON_OFF,
    #                                 icon_size= 35, 
    #                                 icon_color=ft.colors.BLACK,           
    #                         ),
    #                 ft.Row(
    #                     controls=[
    #                         ft.Text("U", size= 100, weight = ft.FontWeight.BOLD),
    #                     ]
    #                 ),
    #             ft.Container(height="20"),
    #             ft.Text("USUARIOS",
    #                     size=20,
    #                     weight=ft.FontWeight.BOLD,
    #                     ),
    #             ft.Text('Gestión de la base de datos de Usuarios que arriendan la app en modalidad de "software as a service"', size= 12,),
    #         ],
    #             spacing=0,
    #             expand = True
    #         ),
    #             margin=5,
    #             padding=30,
    #             bgcolor=ft.colors.GREEN_800,
    #             border_radius=1,
    #             expand = True,
    #     )
        
    #     self.clientes = ft.Container(
    #         content=ft.Column(
    #             controls=[
    #                 ft.Row(
    #                     controls=[
    #                         ft.Text("C", size= 100, weight = ft.FontWeight.BOLD),
    #                         ft.IconButton(ft.icons.RADIO_BUTTON_OFF,
    #                                 icon_size= 35, 
    #                                 icon_color=ft.colors.WHITE,           
    #                         ),
    #                     ],
    #                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    #                 ),
    #             ft.Container(height="20"),
    #             ft.Text("CLIENTES",
    #                     size=20,
    #                     weight=ft.FontWeight.BOLD,
    #                     text_align= ft.TextAlign.LEFT
    #                     ),
    #             ft.Text("Gestión de los Contratos suscritos con los usuarios", size= 12,),
    #         ],
    #             spacing=0,
    #             expand = True
    #         ),
    #             margin=5,
    #             padding=30,
    #             bgcolor=ft.colors.GREEN_800,
    #             border_radius=1,
    #             expand = True,
    #     )
        
    #     self.dashboard = ft.Container(
    #         content=ft.Column(
    #             controls=[
    #                 ft.Row(
    #                     controls=[
    #                         ft.Text("D", size= 100, weight = ft.FontWeight.BOLD),
    #                         ft.IconButton(ft.icons.RADIO_BUTTON_OFF,
    #                                 icon_size= 35, 
    #                                 icon_color=ft.colors.BLACK,           
    #                         ),
    #                     ],
    #                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    #                 ),
    #             ft.Container(height="20"),
    #             ft.Text("DASHBOARD",
    #                     size=20,
    #                     weight=ft.FontWeight.BOLD,
    #                     text_align= ft.TextAlign.LEFT
    #                     ),
    #             ft.Text("Gestión de los Contratos suscritos con los usuarios", size= 12,),
    #         ],
    #             spacing=0,
    #             expand = True
    #         ),
    #             margin=5,
    #             padding=30,
    #             bgcolor=ft.colors.AMBER_500,
    #             border_radius=1,
    #             expand = True,
    #     )
        
    #     self.tools = ft.Container(
    #         content=ft.Column(
    #             controls=[
    #                 ft.Row(
    #                     controls=[
    #                         ft.Text("T", size= 100, weight = ft.FontWeight.BOLD),
    #                         ft.IconButton(ft.icons.RADIO_BUTTON_OFF,
    #                                 icon_size= 35, 
    #                                 icon_color=ft.colors.BLACK,           
    #                         ),
    #                     ],
    #                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        
    #                 ),
    #             ft.Container(height="20"),
    #             ft.Text("TOOLS",
    #                     size=20,
    #                     weight=ft.FontWeight.BOLD,
    #                     text_align= ft.TextAlign.LEFT
    #                     ),
    #             ft.Text("Gestión de los Contratos suscritos con los usuarios", size= 12,),
    #         ],
    #             spacing=0,
    #             expand = True
    #         ),
    #             margin=5,
    #             padding=30,
    #             bgcolor=ft.colors.AMBER_500,
    #             border_radius=1,
    #             expand = True,
    #     )
        
    # def build(self):
    #     return ft.Container(
    #         content= ft.Column(
    #             controls= [
    #                 ft.Text("MENU",
    #                         size=32,
    #                         weight=ft.FontWeight.BOLD,
    #                         text_align=ft.TextAlign.CENTER),
    #                 ft.ResponsiveRow(
    #                     controls= [
    #                         ft.Column(
    #                             col={"md":4},
    #                             controls=[
    #                                 self.usuarios,
    #                             ],
    #                             #expand= True  
    #                         ),
    #                         ft.Column(
    #                             col={"md":8},
    #                             controls=[
    #                                 self.clientes,
    #                                 ft.ResponsiveRow(
    #                                     controls=[
    #                                         ft.Column(
    #                                             col={"md":6},
    #                                             controls=[
    #                                                 self.dashboard,
    #                                             ]
    #                                         ),
    #                                         ft.Column(
    #                                             col={"md":6},
    #                                             controls=[
    #                                                 self.tools,
    #                                             ]
    #                                         ),
                                            
    #                                         ],
    #                                     #expand = True,
    #                                     )
    #    ,M                             ],
    #                             #expand = True,
    #                             ),
    #                     ],
    #                     #expand= True,
    #                     vertical_alignment = ft.CrossAxisAlignment.STRETCH
    #                 ),
                    
    #             ],  
    #             #expand=True,
    #         ),
    #     padding=10,
    #     #expand = True,   
    #     )
    
    # ----chat gpt
    
    # def create_card(letter,title,description,color):
    #         return ft.Container(
    #             content=ft.Stack(  # Permite superponer el icono sobre el texto
    #                 controls=[
    #                     ft.Container(  # Icono en la esquina superior izquierda
    #                         content=ft.IconButton(ft.icons.RADIO_BUTTON_OFF, 
    #                                               icon_size=35, 
    #                                               icon_color=ft.colors.BLACK),
    #                         alignment=ft.alignment.top_left,
    #                         margin=ft.Margin(10, 10, 0, 0)
    #                     ),
    #                     ft.Column(
    #                         controls=[
    #                             ft.Text(letter, size=100, weight=ft.FontWeight.BOLD),
    #                             ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
    #                             ft.Text(description, size=12)
    #                         ],
    #                         spacing=10,
    #                         alignment=ft.MainAxisAlignment.CENTER,
    #                         horizontal_alignment=ft.CrossAxisAlignment.CENTER
    #                     )
    #                 ]
    #             ),
    #             bgcolor=color,
    #             border_radius=10,
    #             padding=30
    #         )

    #     # Crear los cuadros con sus posiciones
    #     self.usuarios = create_card("U","USUARIOS","Gestión de usuarios en SaaS",ft.colors.GREEN_800)
        
    #     self.clientes = create_card("C","CLIENTES","Gestión de contratos",ft.colors.GREEN_800)
        
    #     self.dashboard = create_card("D","DASHBOARD","Gestión de informes",ft.colors.AMBER_500)
        
    #     self.tools = create_card("T","TOOLS","Herramientas del sistema",ft.colors.AMBER_500)

    # def build(self):
    #     return ft.Container(
    #         content=ft.GridView(  # Usamos GridView para simular el grid CSS
    #             runs_count=5,  # Simula las 5 columnas
    #             max_extent=250,  # Tamaño máximo de cada cuadro
    #             spacing=8,  # Simula el gap
    #             run_spacing=8,
    #             controls=[
    #                 ft.Container(content=[self.usuarios], expand=True, col_span=1, row_span=2),
    #                 ft.Container(content=[self.clientes], expand=True, col_span=2),
    #                 ft.Container(content=[self.dashboard], expand=True, col_start=2, row_start=2),
    #                 ft.Container(content=[self.tools], expand=True, col_start=3, row_start=2)
    #             ]
    #         ),
    #         expand=True,
    #         padding=ft.Padding(10, 10, 10, 10)
    #     )

#TEST PARA UI PRINCIPAL


import pytest
from unittest.mock import MagicMock
import flet as ft

import sys
sys.path.append('PQRS/main.py')
import main

def test_main_initialization():
    # Crear un mock para la página
    mock_page = MagicMock(spec=ft.Page)
    
    # Llamar a la función principal con la página simulada
    main(mock_page)
    
    # Verificar configuraciones iniciales de la página
    mock_page.title = "App PQRS"
    mock_page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    mock_page.vertical_alignment = ft.MainAxisAlignment.CENTER
    mock_page.theme_mode = ft.ThemeMode.LIGHT
    mock_page.window_icon = 'assets/icons/icon.png'

    # Verificar que la navegación inicial es a "/login"
    mock_page.go.assert_called_once_with("/login")

def test_router_navigation():
    from router import Router  # Importar la clase Router
    mock_page = MagicMock(spec=ft.Page)
    router = Router(mock_page)

    # Simular cambio de ruta
    mock_page.route = "/dashboard"
    mock_page.on_route_change = lambda e: router.navigate(mock_page.route)

    # Llamar al evento simulado
    mock_page.on_route_change(None)
    
    # Verificar que el método `navigate` fue llamado correctamente
    router.navigate.assert_called_once_with("/dashboard")

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def exportar_a_pdf(data, players_sorted, winners_by_month):
    # Crear el archivo PDF
    c = canvas.Canvas("informacion.pdf", pagesize=letter)

    # Agregar título al PDF
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Información de Jugadores")  # Ajusta las coordenadas según tu preferencia

    # Configurar el estilo del texto
    c.setFont("Helvetica", 12)

    # Diccionario auxiliar para mapear números de mes a nombres completos
    nombres_meses = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre"
    }

    # Espacio vertical necesario para cada bloque de contenido
    espacio_bloque = 180

    # Espacio vertical restante en la página actual
    espacio_restante = 700

    # Función para verificar si hay suficiente espacio en la página actual
    def verificar_espacio(espacio_necesario):
        nonlocal espacio_restante
        if espacio_restante < espacio_necesario:
            c.showPage()  # Crear una nueva página
            espacio_restante = 700

    # Escribir los datos de todos los jugadores en el PDF
    c.drawString(50, espacio_restante, "Datos de los Jugadores:")
    espacio_restante -= 20  # Espacio vertical entre títulos y contenido
    for player in data:
        verificar_espacio(espacio_bloque)
        c.drawString(50, espacio_restante, f"Username: {player['username']}")
        c.drawString(50, espacio_restante - 20, f"Email: {player['email']}")
        c.drawString(50, espacio_restante - 40, f"Wins: {player['wins']}")
        c.drawString(50, espacio_restante - 60, f"Num Movements: {player['num_movements']}")
        c.drawString(50, espacio_restante - 80, f"Last Num Movements: {player['last_num_movements']}")
        c.drawString(50, espacio_restante - 100, f"Creation Date: {player['creation_date']}")
        c.drawString(50, espacio_restante - 120, f"Dates: {', '.join(player['date'])}")
        c.drawString(50, espacio_restante - 150, "-" * 100)
        espacio_restante -= espacio_bloque

    # Crear una nueva página si no hay suficiente espacio para el título de los ganadores por mes
    verificar_espacio(40)

    # Escribir los ganadores por mes en el PDF
    c.drawString(50, espacio_restante, "Ganadores por Mes:")
    espacio_restante -= 20  # Espacio vertical entre títulos y contenido
    for mes, ganadores in winners_by_month.items():
        verificar_espacio(20)
        c.drawString(50, espacio_restante, f"{nombres_meses[mes]}: {', '.join(ganadores)}")
        espacio_restante -= 20  # Espacio vertical entre ganadores por mes

    # Crear una nueva página si no hay suficiente espacio para el título de los jugadores ordenados
    verificar_espacio(40)

    # Escribir los jugadores ordenados por número de movimientos en el PDF
    c.drawString(50, espacio_restante, "Jugadores Ordenados por Número de Movimientos:")
    espacio_restante -= 20  # Espacio vertical entre títulos y contenido
    for i, player in enumerate(players_sorted, start=1):
        verificar_espacio(20)
        c.drawString(50, espacio_restante, f"{i}. {player['username']}: {player['num_movements']} movimientos")
        espacio_restante -= 20  # Espacio vertical entre jugadores

    # Guardar el archivo PDF
    c.save()


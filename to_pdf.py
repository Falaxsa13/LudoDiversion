from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def export_to_pdf(data, players_sorted, winners_by_month):

    # Create the PDF file
    c = canvas.Canvas("information.pdf", pagesize=letter)

    # Add title to the PDF
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Información de Jugadores")  # Ajusta las coordenadas según tu preferencia

    # Set text style
    c.setFont("Helvetica", 12)

    # Auxiliary dictionary to map month numbers to full names
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

    # Vertical space required for each content block
    espacio_bloque = 180

    # Remaining vertical space on the current page
    espacio_restante = 700

    # Function to check if there is enough space on the current page
    def verificar_espacio(espacio_necesario):
        nonlocal espacio_restante
        if espacio_restante < espacio_necesario:
            c.showPage()  # Crear una nueva página
            espacio_restante = 700

    # Write data for all players in the PDF

    c.drawString(50, espacio_restante, "Datos de los Jugadores:")

    espacio_restante -= 20  # Vertical space between titles and content

    for player in data:

        month = player['creation_date'][:2]
        year = player['creation_date'][2:]
        verificar_espacio(espacio_bloque)
        c.drawString(50, espacio_restante, f"Username: {player['username']}")
        c.drawString(50, espacio_restante - 20, f"Email: {player['email']}")
        c.drawString(50, espacio_restante - 40, f"Wins: {player['wins']}")
        c.drawString(50, espacio_restante - 60, f"Num Movements: {player['num_movements']}")
        c.drawString(50, espacio_restante - 80, f"Last Num Movements: {player['last_num_movements']}")
        c.drawString(50, espacio_restante - 100, f"Creation Date: {month}/{year}")
        c.drawString(50, espacio_restante - 120, f"Dates: {', '.join(player['date'])}")
        c.drawString(50, espacio_restante - 150, "-" * 100)
        espacio_restante -= espacio_bloque

    # Create a new page if there is not enough space for the winners by month title
    verificar_espacio(40)

    # Write the winners by month in the PDF
    c.drawString(50, espacio_restante, "Ganadores por Mes:")
    espacio_restante -= 20  # Vertical space between titles and content
    for mes, ganadores in winners_by_month.items():
        verificar_espacio(20)
        c.drawString(50, espacio_restante, f"{nombres_meses[mes]}: {', '.join(ganadores)}")
        espacio_restante -= 20  # Vertical space between winners by month

    # Create a new page if there is not enough space for the sorted players title
    verificar_espacio(40)

    # Write the players sorted by number of movements in the PDF
    c.drawString(50, espacio_restante, "Jugadores Ordenados por Número de Movimientos:")
    espacio_restante -= 20  # Vertical space between titles and content
    for i, player in enumerate(players_sorted, start=1):
        verificar_espacio(20)
        c.drawString(50, espacio_restante, f"{i}. {player['username']}: {player['num_movements']} movimientos")
        espacio_restante -= 20  # Vertical space between players

    # Save the PDF file
    c.save()


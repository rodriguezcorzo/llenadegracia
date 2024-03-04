from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generar_lista_asistencia(evento, participantes):
    # Crear un buffer de bytes para almacenar el PDF
    buffer = BytesIO()

    # Crear documento PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Obtener la fecha de inicio del evento
    fecha_evento = evento.fecha.strftime("%Y-%m-%d %H:%M:%S")

    # Crear contenido para el PDF
    content = []

    # Título del evento
    content.append(Paragraph(evento.titulo, styles['Title']))

    # Fecha del evento
    content.append(Paragraph(f"Fecha del evento: {fecha_evento}", styles['Normal']))

    # Espacio
    content.append(Spacer(1, 12))

    # Lista de participantes
    data = []
    for participante in participantes:
        fila = [participante.persona.nombre, participante.persona.apellido,
                participante.persona.direccion, str(participante.persona.celular), ""]
        data.append(fila)

    # Encabezados de la tabla
    encabezados = ["Nombre", "Apellido", "Dirección", "Celular", "Firma"]

    # Crear tabla para la lista de participantes
    table = Table([encabezados] + data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Añadir tabla al contenido del PDF
    content.append(table)

    # Construir el PDF
    doc.build(content)

    # Obtener los datos del PDF como bytes
    pdf_data = buffer.getvalue()

    # Reiniciar el buffer
    buffer.seek(0)
    buffer.truncate()

    return pdf_data
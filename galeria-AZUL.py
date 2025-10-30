import flet as ft
import flet_video as fv  # Para reproducir los videos

def main(page: ft.Page):
    page.title = "Evolución de la CPU"
    page.bgcolor = "#0A192F"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.HIDDEN
    page.window_min_width = 1100

    # --- Datos ---
    videos = [
        {
            "titulo": "John Von Neumann",
            "descripcion": "Fui pionero en la arquitectura de von Neumann, un modelo que permitió a las computadoras almacenar instrucciones y datos en la misma memoria.",
            "extra": "John von Neumann también contribuyó a la teoría de juegos, la física cuántica y la bomba de hidrógeno.",
            "video": "https://github.com/ximSg1410/PIONEROS/raw/main/John_Von_Neuman_Matematico_Polimata_y_Sus_Contribuciones_Multidisciplinarias__10-22%2017_48.mp4",
        },
        {
            "titulo": "Unidad Aritmético Lógica (ALU)",
            "descripcion": "La ALU realiza operaciones matemáticas y lógicas esenciales. Es el núcleo del procesamiento de datos dentro de la CPU.",
            "extra": "Ejemplo: cuando una calculadora suma 4 + 7, la ALU es la responsable de esa operación dentro del procesador.",
            "video": "https://github.com/ximSg1410/PIONEROS/raw/main/Unidad_Aritmetico_Logica_Funcion_y_Diseno_en_Computadoras_Digitales__10-22%2018_30.mp4",
        },
        {
            "titulo": "Unidad de Control",
            "descripcion": "Dirige las operaciones dentro del procesador, asegurando que cada instrucción se ejecute en el orden correcto.",
            "extra": "Actúa como el 'director de orquesta' de la CPU, gestionando los flujos de datos y controlando los componentes.",
            "video": "https://github.com/ximSg1410/PIONEROS/raw/main/La_Unidad_de_Control_La_Mente_de_la_Maquina__10-22%2018_16.mp4",
        },
        {
            "titulo": "Registros",
            "descripcion": "Son pequeñas memorias internas que almacenan temporalmente los datos e instrucciones que se están procesando.",
            "extra": "Ejemplo: los registros ayudan a la CPU a recordar resultados intermedios sin tener que acceder a la memoria principal.",
            "video": "https://github.com/ximSg1410/PIONEROS/raw/main/Funcionamiento_y_Uso_de_los_Registros_en_la_Memoria_de_la_Maquina__10-22%2018_29.mp4",
        },
        {
            "titulo": "Diagrama Completo de la CPU",
            "descripcion": "Representa cómo se comunican la ALU, la Unidad de Control y los Registros para procesar información eficientemente.",
            "extra": "Este modelo explica cómo los datos se mueven desde la entrada hasta la salida, siguiendo el ciclo de instrucción.",
            "video": "https://github.com/Leonex657/Jonh-von/raw/main/WhatsApp%20Video%202025-10-22%20at%209.18.12%20PM.mp4",
        },
    ]

    imagenes = [
        "https://raw.githubusercontent.com/Leonex657/abp/main/alu.jpg",
        "https://raw.githubusercontent.com/Leonex657/abp/main/control.JPG",
        "https://raw.githubusercontent.com/Leonex657/abp/main/registros.JPG",
        "https://raw.githubusercontent.com/Leonex657/abp/main/completo.jpg",
    ]

    indice_actual = [0]
    contenedor_contenido = ft.Container(expand=True)

    # --- Botones ---
    boton_siguiente = ft.ElevatedButton(
        "Siguiente ▶",
        bgcolor="#2563EB",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
    )
    boton_anterior = ft.ElevatedButton(
        "◀ Anterior",
        bgcolor="#3B82F6",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25)),
    )

    # --- Función para mostrar contenido ---
    def mostrar_contenido():
        vid = videos[indice_actual[0]]

        # 🎥 Video (sin border_radius, pero dentro de un contenedor redondeado)
        video_player = ft.Container(
            content=fv.Video(
                playlist=[fv.VideoMedia(vid["video"])],
                width=360,
                height=260,
                autoplay=True,
                show_controls=True,
            ),
            bgcolor="#1E3A8A",
            padding=10,
            border_radius=15,
        )

        # 📘 Texto descriptivo
        texto_columna = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        vid["titulo"],
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color="#93C5FD",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        vid["descripcion"],
                        size=14,
                        color="#E0E7FF",
                        text_align=ft.TextAlign.JUSTIFY,
                    ),
                    ft.Text(
                        f"💡 {vid['extra']}",
                        size=13,
                        color="#BFDBFE",
                        italic=True,
                        text_align=ft.TextAlign.JUSTIFY,
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor="#1E40AF",
            padding=15,
            border_radius=15,
            width=360,
        )

        # 🖼 Imagen (solo a partir del segundo elemento)
        imagen = None
        if indice_actual[0] > 0:
            imagen = ft.Container(
                content=ft.Image(
                    src=imagenes[indice_actual[0] - 1],
                    width=360,
                    height=260,
                    fit=ft.ImageFit.CONTAIN,
                ),
                bgcolor="#1E3A8A",
                padding=10,
                border_radius=15,
            )

        # 🔹 Fila horizontal
        fila = ft.Row(
            controls=[video_player, texto_columna, imagen] if imagen else [video_player, texto_columna],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        # 🔹 Botones de navegación
        botones = ft.Row(
            [
                boton_anterior if indice_actual[0] > 0 else ft.Container(width=130),
                boton_siguiente if indice_actual[0] < len(videos) - 1 else ft.Container(width=130),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30,
        )

        contenedor_contenido.content = ft.Column(
            [
                fila,
                ft.Container(botones, margin=ft.margin.only(top=25)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        page.update()

    # --- Funciones de botones ---
    def siguiente_click(e):
        if indice_actual[0] < len(videos) - 1:
            indice_actual[0] += 1
        mostrar_contenido()

    def anterior_click(e):
        if indice_actual[0] > 0:
            indice_actual[0] -= 1
        mostrar_contenido()

    boton_siguiente.on_click = siguiente_click
    boton_anterior.on_click = anterior_click

    # --- Layout principal ---
    page.add(
        ft.Column(
            [
                ft.Text(
                    "💻 Evolución de la CPU y sus Componentes",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#60A5FA",
                    text_align=ft.TextAlign.CENTER,
                ),
                contenedor_contenido,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

    mostrar_contenido()

ft.app(main)

# Pokedex - Aplicación Flask

Una aplicación web de Pokedex construida con Flask.

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Crea un entorno virtual:
```bash
python -m venv venv
```

2. Activa el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## Estructura del Proyecto

```
Pokedex/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
├── .env               # Variables de entorno
├── templates/         # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   └── pokemon.html
├── static/            # Archivos estáticos
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── README.md
```

## Características

- Listado de Pokeneas
- Visualización de datos en JSON
- Frases filosóficas de Pokeneas
- Integración con Amazon S3
- Interfaz responsiva
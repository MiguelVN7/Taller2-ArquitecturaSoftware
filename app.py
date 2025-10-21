from flask import Flask, render_template, request, jsonify
import os
import random
import socket
import boto3
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'tu-clave-secreta-aqui')

# Configuración de AWS S3
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')

# Inicializar cliente de S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def get_s3_image_url(image_key):
    """Genera la URL pública de una imagen en S3"""
    return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{image_key}"

# Arreglo con los Pokeneas
POKENEAS = [
    {
        "id": 0,
        "nombre": "Pikachu",
        "altura": 0.4,
        "habilidad": "Pedir descuentos",
        "imagen": get_s3_image_url("pikachu.png"),
        "frase_filosofica": "Más sabe el diablo por viejo que por diablo."
    }, 
    {
        "id": 1,
        "nombre": "Bulbasaur",
        "altura": 0.7,
        "habilidad": "Plantar frijoles",
        "imagen": get_s3_image_url("bulbasaur.png"),
        "frase_filosofica": "El que mucho abarca, poco aprieta."
    },
    {
        "id": 2,
        "nombre": "Charmander",
        "altura": 0.6,
        "habilidad": "Calentar cafe",
        "imagen": get_s3_image_url("charmander.png"),
        "frase_filosofica": "El que mucho sirve, poco invita."
    },
    {
        "id": 3,
        "nombre": "Squirtle",
        "altura": 0.5,
        "habilidad": "Enfriar cafe",
        "imagen": get_s3_image_url("squirtle.png"),
        "frase_filosofica": "El que tiene tienda que la atienda."
    },
    {
        "id": 4,
        "nombre": "Nidoqueen",
        "altura": 1.3,
        "habilidad": "Montar en el metro sin caerse",
        "imagen": get_s3_image_url("Nidoqueen.png"),
        "frase_filosofica": "Cuentas claras y el chocolate espeso."
    },
    {
        "id": 5,
        "nombre": "Nidoking",
        "altura": 1.4,
        "habilidad": "Manejar sin demorarse 2 horas",
        "imagen": get_s3_image_url("Nidoking.png"),
        "frase_filosofica": "Con hambre, no hay pan duro."
    },
    {
        "id": 6,
        "nombre": "Primeape",
        "altura": 1.0,
        "habilidad": "No dejarse atracar",
        "imagen": get_s3_image_url("Primeape.png"),
        "frase_filosofica": "De eso tan bueno no dan tanto."
    },
    {
        "id": 7,
        "nombre": "Poliwrath",
        "altura": 1.3,
        "habilidad": "Nadar en el rio Medellin",
        "imagen": get_s3_image_url("Poliwrath.png"),
        "frase_filosofica": "Al que le van a dar, le guardan."
    },
    {
        "id": 8,
        "nombre": "Alakazam",
        "altura": 1.5,
        "habilidad": "Adivinar la mejor ruta para el bus",
        "imagen": get_s3_image_url("Alakazam.png"),
        "frase_filosofica": "Mugre que no mata, engorda."
    },
    {
        "id": 9,
        "nombre": "Machamp",
        "altura": 1.6,
        "habilidad": "Cocinar bandejas paisas",
        "imagen": get_s3_image_url("Machamp.png"),
        "frase_filosofica": "Barriga llena, corazón contento."
    },
]


def get_container_id():
    """Sirve para obtener el ID del contenedor (hostname)"""
    return socket.gethostname()


@app.route('/')
def index():
    """Página principal con la info. del taller 2"""
    return render_template('index.html', id_contenedor=get_container_id())


@app.route('/temas')
def temas():
    """Página para seleccionar temas de colores"""
    return render_template('temas.html')


@app.route('/pokenea/json')
def pokenea_json():
    """Muestra los JSON con los datos de un Pokenea random"""
    pokenea = random.choice(POKENEAS)

    respuesta = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "id_contenedor": get_container_id()
    }

    return jsonify(respuesta)


@app.route('/pokenea/filosofia')
def pokenea_filosofia():
    """Muestra imagen y frase filosofica de un Pokenea random"""
    pokenea = random.choice(POKENEAS)
    return render_template("filosofia.html", pokenea=pokenea, id_contenedor=get_container_id())


@app.route('/api/pokemon')
def api_pokemon_list():
    """API endpoint para listar todos los Pokeneas"""
    return jsonify({
        'pokeneas': POKENEAS,
        'total': len(POKENEAS),
        'container_id': get_container_id()
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

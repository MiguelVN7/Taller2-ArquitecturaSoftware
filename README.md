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

## Docker

Para construir y ejecutar la aplicación con Docker:

```bash
docker build -t pokedex-pokeneas .
docker run -p 5000:5000 --env-file .env pokedex-pokeneas
```

## AWS EC2

### Pokedex-leader
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvWIA+1r/nG3A/s1tfoGtrWWxPVX7HgImm4DrlIKBRRumyEq4
alexE/4dV8TYJ0972XuQfYW0c0CsIuNxuQEk5vuAfRMk38yX0k023qVIcUtKqlk/
6yoTTqkfjpt8Pebi2OHB/Eq+zasU+P7NOX2fqEiunUWz9Hon+gw294vWgB7IEv4x
Cz9zdOuTW16OijW8UuT/MvzZbfbk8HMwjPpo3UbF4+/g2Xe+0mjiT8FrIjnIVqz+
rvUlHf0v57o7m0De2ALEieIHzYCoUiI3/YIpbKQMBkdJd4kIqDR7jyBvKyZPcG6J
zp4hWHBneNF80HvieBQK5NvQ+DbKkvaoTP9dbwIDAQABAoIBAC3/ldl3Wsp15gB9
iPDHMpYBMzGApsO9Jf9zKsUhhaBxfOr9Kxm5PutqN1pQF2hE6AIE/y1dwlyUArte
nwqeeoYX5Dd85OHu4ZlU49TkNFpAPVxu3RWTXKkobt/GaEDoyYSAIQvUY8+0lB1+
Vf52wsavEKpmebURzo/vU5KAxpLLfA9LEhvr+hBbZtKCn2BcxJdkw95OFBakYySv
SwVQORAoa/zebAj7peDE1EnFMDHN+U/bx1Z26DaFfoectiF6YWnxFKMTqyuzDM7u
EGnIpptlF1sN5rtjV496+an1N+qI6DakKAciVfSDIBKPLC2BWzlg3bx0wPIVRrdW
TAPxjuECgYEA6PVwgWDO2OWzSHEWJgn4og5VWLnfvPfP9GgHFK7vB3WK1RPX+li1
A+IH9FfuZJIV2kT+MQRZS0K+Nghk5O5bb3xzAPWJtk8o5sajm+MKuSTkfgTIGpvJ
jPifGr3adjlD1o/sJ48FruV81taiZ4T0NAyFhHIEHT9UDACNjmbiOFkCgYEA0B02
sJ1hKjPIqWJ95nFP1uE/FtcA9eqdBSpdgsDBI1Io6a8FdJWsQ+wfGnFBSYvkUnVP
3Z3FZadu4oC/rf/4RO1TH7quOgX6eEYRnRpaWvRJDB8yaLPEEUV2i74WwahPd4BM
XkV5zwF9F6qnyTbbAjrbkwD4ncW3RuBtGZsECwcCgYBVObW3H1uNLjuwvO6FbBBx
+RxwIVAhKegCWix8/KKl7/KikWfqRpmymfafBaxJTsh/2c3E0Pp59ijwS5HdzvXU
i4rnRuzirYMhKnqghSdfJIgTMlyin2vVDv/mIJ7TsY+H549VyZUirwJE9rDjflh4
0jvmgG/Q42I0Id+nwSvxwQKBgCUhoTlfyw9Jj/rQzN/JxdHz/Fqp380AoCVkyqxi
kdMofI49IP8NGWBBB8ei/2AM6p7fuXE0Dh02A228RPbZncVGhrc5io5ltKuy7L+Y
DRj/Tu0vv8G4mTnvp9gFAXBqBEuxA28qfDI39Ma9NxSKigba04Rl/vW/ahTmQ/D2
nIEPAoGAEcUvr9SUti7TP3Y2lBNE+t51egsUA5dsQ5w2mX2i84V2C+AiDxy35WSD
VsrlyCVrtkS+6E4x2vylub293eO1r+sKxA8NhILbqCwRy9VjVG04lv5W56kLFUmH
X034KlNUpB9OzK5YbB5Zfwi8SyXEG4UlQBbYbsOu0k6w2I1EmRI=
-----END RSA PRIVATE KEY-----

### Pokedex-manager-1
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA2f8RAgdNMp9FYRseZK1jctbR93F39RANVDK+OWrZn/b2MVag
vhrBjHDqnAYdzLoTN6UVAHDwYj4X6xUNXLTZ0j0ETZ6kaG/hSlbZC1mnf0SYSdgT
k3bZd8EbFPgUA7SeouewhVl9+thKcpXctQn/zB5JXFURKluu1ESt8OutU3cdND4Y
e0d2+t3sgHzh+MIOkzxHLnLWfrE24qR5BYDaSd6ttty4TFWrseGfsad8RMntnGO/
zbVeOrd1VwvOYaBP2keapeXyrAQUtgCynW1T484JUxifqELVVYlkhzQ2vmbi2HJ9
KWgvqRxd7onDg5WIu/Q33OmjYvfS8LX+xuUt1QIDAQABAoIBACapZPPOJbPPqXdS
Xu6ODbAlRzGyTwsIYMTJBxGZ0KTdIMaZTYLJrf/hWsp3Dzvq2FOrFHFylj9mMcnA
fxEtBeCSb7vwYcof5X3Qr0ejC+C3YqbeCoLBtknV1p6+bJZHp0bO/nB38a7WQ0XV
LEJzVol16Z7Ve2jev7/nuk2bDq9ZgejWPU4PiYUGO7RvUe0XiQGDx9rZQ3uCxqZR
G/51oFbo/byii2I5FY8PC7rpvtbQlHEKsuJ7z9vliYXcgkJaPp7Q4+uyWB//0dJ4
ExHIZccMZ39kIv5e/LU56VUsSLFPu54qz85LxliJFBfUL1g1xKk7fo3dJWW+0bEl
2PVNUuECgYEA7uBqsXpaHDXaglTxHTt/5x7n1pbplq0NQdiCq9YlD4i25he3qrQf
bnqIDlEUfKLVAG3HZkcpa6j4xHKWPkE33BSO7XShbFVXupgejopQHk0u2AORexXD
K0mEznEQsmRNEMAkHpUyKI+XuZ0gFcTK81M4XdGfHNiAnBtXH1hNwfkCgYEA6Z96
ubO1v/xHvj96cty47zNhx2x/AA+Gna9qR6e2kAuX9l4ZDIU836CpWSAjxrqdqBjY
vqPCRsGkJCn+DRRCz8VKqn4QZRKjaecK636s49e5gDWzRehJomvnBBnY8Ttdv41F
4+rvEfOJhIP6DPlVA/Q9FC7YtxCjleU3iIRTAb0CgYAheKKakblUoJsojfxnCzJF
0UfNAsJiUYc9BbhxmYUB4zc1kHc03R5WXab40pWbTTmpYLiC9U+xfTC2XhP9Tygj
l2Hble8UffTX+X62nFzTkh8RN5bH92mshBWu05ryVCmUQkgNXPx1QIGTCZg4VKXX
aH7Kbpfr8845kX8orjffCQKBgQDgvVctL5Dm6EUH4j7kIisRiMdGNbwSjdz88hN2
bQM1nMGJ8kl8fuvpYL+oij+AXGNvor9W3Wf18y/4ziCj6lq/TtaeHnmdEYn8RZN+
qbSd1heQG5ii5mt3gP+SNV856NctfzS9pXJoPXSL8v3n3y8Gh7z+HnbB3JLRjtiW
Tl0frQKBgQC3pJUxiywvzMm1cg06ucc7YIoztN3HTm7hCdNgIaG4gFoUDEOrYUAl
WYfepHOqjTZhW4SYxvlTWB4tyLSSsOZGsqBLRirvFkoqqOkJs+qISd9GxptiSyxm
d3YVKIeh2jErmGpWUnxoCt/8J0S7m1bUOmEQ56iatZmBId7YRn409w==
-----END RSA PRIVATE KEY-----

### Pokedex-manager-2
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwfhhVfbOtKBLuci1CcYnqJ5+qFG0CyH2BtUjc9tyIOK6FJ60
wJO75nYj1gUiLLkhFKICcYGZdT2kQu2bfmi/r4vgpmJ4RcbUwOk8H88oFDYaQuej
yA0cE8prECxIoNdywbnaZQ+pkQ4ZaJB1NC3KpY5V3/bhXrn4L2m3Vp3PZk4R86WV
tLSzXAg4CIm4I3hvBr/AaSZRJV3LWnXIC5i7MM9QLGNa4E+WS9l88NFfQP1e36IJ
XTWO9QL/+SCZClin/i0sG6uboh6Wz2tP87ZXpw5yl90tI6GZ77ocfEyAS0OZufrC
v0+EBt1HqQxcynwSiRcVuXye5Ck7Y2UZixsldQIDAQABAoIBAF8Lhx5pVnYZiaGa
YGNOroYoS6XMiy1dUcGdVMbjg7PrhQSvk6A9g7f0sbCgSVOizzvd+taFi51wO/nz
ldrGFw88ujKtU4PVXtC8OJLZnijxLcMU4CMZkWV9LSL6oAf4KioVGJemqg8C2p5r
EpMj0QV4jkm1Hk+dTqhk48pUf5j/0eFtH9OS1YNHCnfVCjbcumWFs9dgHrnwqg7D
CoeK0od0cny/9bS7fQH2gqJ6w2zwMzNj9APVUM+4zb0jSLQQEXhygKhdNmnzBOxa
qvq5YY6otuFiRWE2iCNNELlikQ8vuUjkrrFriaqlvKpInWiozXHB/sT71/cktnAv
yvpULM0CgYEA/soOE/TChFefKeY5t+pjkjnA6gpHiIaFo4aU/5KNdA5B5SoXWvQp
CliQMkb+7GA6u0w7F+pUoQXKAO8Nkw2pD2OBXg2MWYDonaJLrKK1eiEN3s6buMD6
zpw85lxJg11NLopDWJWt1I9eSMgawVzmDreyRrosDKTKowBMvqOWy7MCgYEAwuRX
H8lAe4Oi/RllW2nq4XROzt5TEXd+AH/GNenoHQyjUzo1NmePrGyO00j1/vg7f8Lz
9kHps4hLDol/BPCiYevRGKw4ifBZEQJVfjx5Fie3jw7dWp/cL9gx4p3H/ia1Oqgl
v5aQqCe16URPhqStgdMShNnwFJZebmJcIWT8FjcCgYB5Rf9xbDzx9SrjLJwoeD4w
qaCzRXVK/Iy7iyF8jGsb5HVk+KXpOvIV5JWt+LD6HcuWvvAZsAXcJv9BdoeFiSkB
FCHNfLFjIMKX1Vojr8alfPo3JSxlwiUfFqq+EwtCpbRJBLKNhaEZ3avJBMYHZ4px
UupeU9sHoaB5+XiN/RuXlQKBgQCHKrDWRdEoGOMY4N0wKmSR2wWxafZ43cQQ+o1w
5Ppr81DvLyaqxeaacmwYU7jxDh7N/FsRRyObtYJA4dGrjm1Atrm9f+xylrRfHJxI
wg5E9GTVnjydVtPyhuIKRt3nAdedh/MuTnGjfm8nCo6RVnNT4B0u8KwWyzdRHXzC
WHSRvwKBgATldATti1/SvWnOvbBCnPmxmwKcBj1GcBAw9xMKhnaaIXgTz9V+gdX/
Wc3PniZ/PkwCwzkUnf9zhOqb9DaZUAmiSQDiiF2CTjcHLf9K1Zyh/deHCe9xEQAF
Sn4a73XzG7WRB73MQvcnZaAq6jsJHJBEu0YZe4e2KpwVvgh4uSpc
-----END RSA PRIVATE KEY-----

### Pokedex-manager-3
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA2MLyWgaFq8ZAp/q8OqyJ9P8zxvEvkWi9bGlZJHqQaBOcD99f
GBHTnH9H/GKXtWsBgjHhYOG+Q7c1mW7C5b2ugjvEd+GCHeqVIOhJ6sb4TDbmBID3
mLtEXbZppij+KyHJ+iCH6EPa8FlQv/JtVAwMTCv17yLQI+a7wPYXWIk9MWYrEBTB
Qnbps+w9p8do/fjh8VOIjnFnz2+UTGoJPyjZ93XgeqzDzuUdI201O6buLnw1z6M9
oz5/8+Y5H1ddLLcO5b88lPjZJDGbL87DMfst9rPJuYGF7dA8v5tKZax3iOidmlo0
FTh1rpy+3596txSzVKhg53swxQ0NmwFM2/p5eQIDAQABAoIBAFg5ME637Nv3OwWj
pczzwMq4vCgyrjuut7pSPnf8cp4JrTFApwGy77/4hiIRNtIeFWUaTDMUbk49WVFz
pVvAkjBrhxGL9VubyMq2AK/P/+t1RLV8kEnXnoHN5r48XQbNH9nwN6CvTYMZtyYI
07qrlK3EDrsgHjsehDiLcQEWCpP506JbzWl/wHaZIWZyigyEFDycyRN5JFgASW01
QhJGM6RwFrmrz6bB5SYtFNZ7062S5KxDzMHYgmpDH7sRZnS/u2dI9qzKnCAXGche
sdYglkrEndvxwzpfCJ/Uu0SUIOj4tpWDJ/coM9Qcvl9Tek+bj+ARuIJPikmZ06nL
ul6CyYkCgYEA8pak9NEMe3gL8ufIqZruoy2Yp4EmJq6To/0nUafCBmT0V+CeWizJ
IjoTbYl7XIFh9liUJim5bm56v9CAkYSUF3hFurh+b/gI+HkzEPj/jT3GDjONje7W
dfbi8ExM3FlfodNG3qPM4xNx+DCI1y9UiACP7eGggfY4wc0+xmV9sVsCgYEA5L7G
ARnRresqjm9DP7GGqHuCeAQUEkNYk1XRkjlJjih1LiOtY8rnBdUn2EjN0gq1rzSk
A4P86vOaGRBUhokAPeag0YWNWON+tLkZUtr2jm+dgwI0PZhDIRFXBi+4zxjK/5hg
lA2gD4+MfeWaVlZ/i6ubrZXt6QO6lQ3vBFvVhLsCgYEAnmScKjmAw/FbI+wRSiSe
Ii94WA5sgZ9FSTLXBGrbtd8e524DFu/dGBsBamj1Ai58byPg/5YIvEEopquV9u2w
4C4ooUUrUSKLgOlp3XAnM+qcsdMZXw4OO5HLFYlMOiek2H2h7WbYNYARzzKpdo8x
y2dKktDaQ2EoJ+pCTbogurcCgYAmuLyf9xTtkf+UOPVzVMPsxWuikV4scUYPOtnN
HPF8pRChDN0PJYvSCvFBxaFByxpSXGDfT3qC81XEpGUKmSp3UBEtJqR0xZ3vTd4h
jntqRS6uvLLHMn06ncrTe0SXmiTS+6JtrZjIyY4IydNEhkP1CsnBqr2pUj5FeSRa
4ojUfQKBgQDwxcG41TUtM7x3sDYfCgktiOokzi6C0P8fIJkUq3JZslKJmGQxsYGD
XCuYF2ApkdNjiTsJ81X66Tkw8UkbWxF3V3fYyc6BIhY3m6uSkfziisFN1YEbpcWP
CbGPck36e9hx8N9XEdtfJGiKNAScViBfEEHbg1yCTjAIXEOn8Z2e9Q==
-----END RSA PRIVATE KEY-----
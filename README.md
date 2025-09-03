# Dudo

Este proyecto implementa el juego de Dudo en Python.

Dudo es un juego de dados tradicional conocido también como "Dudo en Cacho" en Chile y algunos países. Es un juego de engaño, probabilidad 
y estrategia donde los jugadores intentan adivinar cuántos dados de cierto valor o  pintas (como se les suele llamar)  hay en total  entre 
todos los  participantes. En cada ronda , un  participante realiza  una apuesta sobre la cantidad y el valor de los dados, y los jugadores 
restantes tienen la  opción de subir  la apuesta, dudar  de que sea verdad o  "calzar" la apuesta. Si alguien duda o calza, se revelan los 
dados y se determina si fue correcto o no, lo que hace que los jugadores ganen o pierdan dados y se acerquen a la eliminación. El objetivo 
es ser el último jugador con dados en la mesa para ganar.

Las reglas que se usaron en esta adaptación fueron las de la siguiente web: https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho


## Requisitos

- Python 3.11 o superior
- Instalar las dependencias listadas en `requirements.txt`

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias ejecutando:

```
pip install -r requirements.txt
```

## EJecucion de Pruebas

Para ejecutar los tests, usando pytest:

```
pytest
o
python3 -m pytest
```

O para una informacion mas detallada:

```
pytest -v
o
python3 -m pytest -v
```

Tambien puedes ver el coverage de los test con:

```
pytest --cov=src --cov-report=term-missing 
o
python3 -m pytest --cov=src --cov-report=term-missing
```

## Estructura del proyecto

- `src/juego/`: Lógica principal del juego
- `src/servicios/`: Servicios auxiliares
- `tests/`: Pruebas unitarias
- `requirements.txt`: Dependencias

## Autores

- Felipe Tilleria
- Oliver Peñailillo

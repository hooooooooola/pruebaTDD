# Dudo

Este proyecto implementa el juego de Dudo en Python.

## Requisitos

- Python 3.11 o superior
- Instalar las dependencias listadas en `requirements.txt`

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias ejecutando:

```
pip install -r requirements.txt
```

## EJecucion Pruebas

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

# Proyecto Python CI/CD

Este es un pequeño proyecto en Python que incluye integración continua y despliegue continuo (CI/CD) usando GitHub Actions.

## Requisitos

- Python >= 3.10
- pip

## Instalación

```bash
pip install -r requirements.txt
```

## Levantar el proyecto

```bash
python app/main.py
```

## Ejecutar tests

```bash
pytest
```

## Construir imagen Docker

1. Asegúrate de tener Docker instalado.
2. Construye la imagen:

    ```bash
    docker build -t python-ci-cd-app .
    ```

3. Ejecuta el contenedor:

    ```bash
    docker run -p 5000:5000 python-ci-cd-app
    ```

## CI/CD con GitHub Actions

Este proyecto está integrado con GitHub Actions. Cada push o pull request ejecuta automáticamente los tests y puede desplegar la aplicación si los tests pasan.

El flujo de trabajo se encuentra en `.github/workflows/ci-cd.yml`.

---

¡Contribuciones y sugerencias son bienvenidas!

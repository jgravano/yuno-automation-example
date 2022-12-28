# Yuno Automation Example :robot:
Public Api automation

## Tecnologías utilizadas:
- python
- pytest

## :robot: instalación, ejecución de test y creación de reporte automático:
pre-condición: instalar Python (en mac, abrir terminal y pegar el siguiente comando: brew install python3)

1. git clone https://github.com/juangravano/yuno-automation-example
2. cd yuno-automation-example
3. pip3 install -r requirements.txt
4. python3 -m pytest test/ --html=report/report.html --self-contained-html

## :pushpin: estructura del proyecto:

  ## 📍src:
  - api: Este módulo contiene dos archivos: api_client.py que nos proveerá los métodos para las llamadas http y un archivo endpoints.py para almacenar constantes con los endpoints a utilizar en el proyecto.
  - requests: En este módulo se encontrarán todos los métodos que nos permitirán armar las ejecuciones para los distintos servicios.
  - schemas: En este módulo se encontrarán todos los json schemas necesarios para armar las ejecuciones de los distintos servicios.
  - helpers: Abstracción de lógica para los test.
  
  ## 📍 test:
  - Cada archivo es una suite de pruebas para un servicio en específico.
  
  ## 📍 report:
  - reporte html generado automáticamente en la ejecución.

  NOTA: el archivo .env lo subo a efectos de que puedan realizarse las prubeas. En un escenario real este file no debería subirse al repositorio.

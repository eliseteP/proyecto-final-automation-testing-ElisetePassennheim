import logging
import pathlib



def login_helper():
    print("codigo para el login")



# def verificar_algo()


def lectura_de_archivos(extension):


    # try:

    # except FileExistsError :
    #     print()
    try:
        print(f"Leyendo archivos con extensión: {extension}")
    except FileNotFoundError as error:
        logger.error("Error al encontrar el archivo: %s", error)

    
    



# 1) Carpeta donde se almacenarán los logs

audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

# 2) Configuración global

logging.basicConfig(
 filename=audit_dir / 'suite.log', # Ruta del archivo de log
 level=logging.INFO, # INFO y superiores
 format='%(asctime)s %(levelname)s %(name)s – %(message)s',
 datefmt='%H:%M:%S',
 force=True
)

# 3) Logger específico que usarán los tests
 
logger = logging.getLogger('talentolab')

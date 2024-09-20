import subprocess
import shlex

ruta_archivo = '/Users/brian/Documents/GitHub/Monitoria-Tecnicas-de-Programacion-I/Auto-qualifier-with-openAI/token.txt'
#classroom_id = '177469998' #ID del classroom,pero aún no implemento esto

def leer_token(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        token = archivo.read().strip()  # Elimina espacios en blanco y saltos de línea
    return token

# Leer y usar el token
token = leer_token(ruta_archivo)
#print(f"El token leído es: {token}") #Prueba de lectura token

# Proteger el token en caso de que tenga caracteres especiales
token_seguro = shlex.quote(token)

# Ejecutar bash con subprocess
bash_process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Lista de comandos que se van a ejecutar secuencialmente
comandos = [
    f'echo {token_seguro} | gh auth login --with-token',                                # Autenticación
    'cd /Users/brian/Documents',                                                        # Cambiar directorio
    'mkdir -p cloned_repositories',                                                     # Crear un directorio
    'cd cloned_repositories',                                                           # Cambiar directorio
    'echo "2024-2 Tecnicas 1 - Grupo 2" | gh classroom clone student-repos',            # TODO: Revisar como seleccionar el assigment
    #'gh classroom clone "2024-2 Tecnicas 1 - Grupo 2" --assignment "Calculadora Java"', # Primer intento fallido --asingment no sirve, hay que conseguir el assingment_ID
]

# Unir los comandos en un solo string, separados por nuevas líneas
comando_conjunto = '\n'.join(comandos)

# Ejecutar todos los comandos
stdout, stderr = bash_process.communicate(comando_conjunto)
    
# Imprimir salida y errores
if stdout:
    print(f"Salida: {stdout}")
if stderr:
    print(f"Errores: {stderr}")

# Cerrar el proceso bash
bash_process.stdin.close()
bash_process.wait()
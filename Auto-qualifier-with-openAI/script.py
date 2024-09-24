import subprocess
import shlex

#Se pueden generar 2 PAT, Classic o Fine-grained, el clasico puede ponerse sin límite de tiempo, el detallado tiene límite.
#Classic PAT Permissions => (repo), (read:org), (admin:org).
#Fine-grained PAT Permissions => n/a.
ruta_archivo = '/Users/brian/Documents/GitHub/Monitoria-Tecnicas-de-Programacion-I/Auto-qualifier-with-openAI/token.txt'

# Para obtener el classroom_id hay que ejecutar los siguientes comandos
# echo TU_PAT | gh auth login --with-token
# gh classroom list
classroom_id = '228739' #2024-2 Tecnicas 1 - Grupo 2 #TODO: Esta variable no se está usando.

# Para obtener el assignment_id hay que ejecutar el siguiente comando
# gh classroom assignments
assignment_id = '646591' #Calculadora Java

def leer_token(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        token = archivo.read().strip()  # Elimina espacios en blanco y saltos de línea
    return token

# Leer y usar el token
token = leer_token(ruta_archivo)

# Proteger el token en caso de que tenga caracteres especiales
token_seguro = shlex.quote(token)

# Ejecutar bash con subprocess
bash_process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Lista de comandos que se van a ejecutar secuencialmente
comandos = [
    f'echo {token_seguro} | gh auth login --with-token', # Autenticación
    'cd /Users/brian/Documents', # Cambiar directorio
    'rm -rf cloned_repositories', # Borra el directorio con antiguos repositorios clonados (optional)
    'mkdir -p cloned_repositories', #  Crea el nuevo directorio para clonar repositorios
    'cd cloned_repositories', # Cambiar directorio
    f'gh classroom clone student-repos -a {assignment_id}' #Clona los repositorios
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
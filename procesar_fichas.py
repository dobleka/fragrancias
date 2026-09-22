import os
import re

def generar_fichas_markdown(archivo_fuente, carpeta_salida="fichas_fragancias"):
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
        
    try:
        with open(archivo_fuente, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"No se encontró el archivo fuente: {archivo_fuente}")
        return

    # Expresión regular para capturar cada bloque de perfume que empiece con ####
    # y sus líneas de notas y acordes asociadas
    patron_perfume = re.compile(r'####\s+([^\n]+)\n((?:\*\s+\*\*[^\n]+\n?)*)', re.UNICODE)
    matches = patron_perfume.findall(contenido)
    
    contador = 0
    for nombre_perfume, bloques_notas in matches:
        # Limpiar nombre para crear un nombre de archivo válido
        nombre_archivo = re.sub(r'[^\w\-]', '_', nombre_perfume.strip()) + ".md"
        ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)
        
        # Estructurar el contenido de la ficha individual
        ficha_contenido = f"# {nombre_perfume.strip()}\n\n"
        ficha_contenido += bloques_notas.strip()
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f_out:
            f_out.write(ficha_contenido)
            
        contador += 1

    print(f"Proceso completado con éxito. Se han generado {contador} fichas en la carpeta '{carpeta_salida}'.")

# Uso: Coloca todo el texto de tus fuentes en un archivo llamado 'datos_github.txt' y ejecuta:
# generar_fichas_markdown('datos_github.txt')

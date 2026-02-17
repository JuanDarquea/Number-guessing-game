# **Juego de Adivinanza**
#### Este es un sencillo juego de adivinanza en Python donde el usuario tiene 10 intentos para adivinar un número secreto generado aleatoriamente entre 1 y 100.

## **Características**
- Número Secreto Aleatorio: El juego genera un número secreto diferente en cada partida.
- Límite de Intentos: Tienes un máximo de 10 intentos para adivinar el número.
- Pistas: El juego te da pistas después de cada intento, indicando si el número que ingresaste es "muy alto" o "muy bajo".
- Validación de Entrada: Maneja entradas no válidas (por ejemplo, texto en lugar de números) y números fuera del rango permitido.
- Menú Interactivo: Un menú simple para jugar de nuevo o salir del juego.

## **Requisitos**
El juego solo requiere una instalación estándar de Python. No necesitas instalar librerías adicionales.

## **Cómo Jugar**
- Asegúrate de tener Python instalado en tu sistema.
- Guarda el código en un archivo llamado *juego_adivinanza.py*.
- Ejecuta el archivo desde la terminal o línea de comandos:
     `python juego_adivinanza.py`
- El juego te dará la bienvenida y te pedirá que elijas una opción para jugar.
- Sigue las instrucciones en pantalla para adivinar el número secreto.

## **Estructura del Código**
El código está estructurado en varias funciones para mejorar la legibilidad y organización:
- mostrar_separador_lineas(): Imprime una línea separadora para el formato.
- espacio_en_blanco(): Imprime una línea en blanco.
- mostrar_caja_intento(intento, max_intentos): Muestra el intento actual y el límite de intentos en un formato de caja.
- jugar_adivinanza(): Contiene la lógica principal del juego: genera el número, maneja el bucle de intentos, valida la entrada del usuario y da pistas.
- main(): La función principal que muestra el menú, maneja las opciones del usuario y ejecuta el juego en un bucle.
- El bloque if __name__ == "__main__": asegura que la función main() se ejecute cuando el script es corrido directamente.

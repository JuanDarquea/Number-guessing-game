# -*- coding: utf-8 -*-
import random #import random module

def mostrar_separador_lineas(): #función para mostrar un separador de líneas
    print("=" * 30) #imprimir un separador de líneas de 30 caracteres
def espacio_en_blanco(): #función para mostrar un espacio en blanco
    print() #imprimir un espacio en blanco para mejorar la legibilidad
def mostrar_caja_intento(intento, max_intentos): #función para mostrar el número de intento actual en una caja
    print("+" + "-" * 21 + "+") # Línea superior
    print(f"|   INTENTO {intento} DE {max_intentos}   |")  # Línea del medio
    print("+" + "-" * 21 + "+") # Línea inferior

def jugar_adivinanza(): #función para jugar al juego de adivinanza
    print("=== JUEGO DE ADIVINANZA ===")
    print("Adivina el número del 1 al 100") 

    numero_secreto = random.randint(1, 100) #generar un número aleatorio entre 1 y 100
    #print(f"DEBUG: El número secreto es: {numero_secreto}")  # Comentado para producción
    intentos = 0 #contador de intentos
    max_intentos = 10 #máximo de intentos permitidos
    
    # Bucle principal del juego
    while intentos < max_intentos: #bucle hasta que se alcance el máximo de intentos
        intentos += 1 #incrementar el contador de intentos
        #print(f"\nIntento {intentos} de {max_intentos}") #mostrar el número de intento actual
        mostrar_caja_intento(intentos, max_intentos) #mostrar el número de intento actual en una caja

        try:
            adivinanza = int(input("Introduce tu número: ")) #pedir al usuario que introduzca un número
        except ValueError:
            print("Por favor, introduce un número válido.")
            intentos -= 1 #decrementar el contador si la entrada no es válida
            continue #volver al inicio del bucle
        
        #validar rango de la adivinanza
        if adivinanza < 1 or adivinanza > 100: #pedir al usuario que adivine un número entre 1 y 100
            print("\nEl número debe estar entre 1 y 100. Inténtalo de nuevo.") #pedir al usuario que adivine un número entre 1 y 100
            intentos -= 1 #decrementar el contador si la entrada no es válida
            continue
                # Comprobar si el usuario ha agotado los intentos
        if adivinanza == numero_secreto: #comprobar si la adivinanza es correcta
            print(f"¡CORRECTO! El número era {numero_secreto}") #mensaje de éxito
            print(f"\nLo adivinaste en {intentos} intentos") #mostrar el número de intentos
            return True  # Indica que ganó el juego
        elif adivinanza < numero_secreto: #comprobar si la adivinanza es menor que el número secreto
            print("\nMuy bajo, intenta con un número mayor")
            mostrar_separador_lineas() #mostrar un separador de líneas
            espacio_en_blanco() #espacio en blanco para mejorar la legibilidad
        else:  # adivinanza > numero_secreto
            print("\nMuy alto, intenta con un número menor")
            mostrar_separador_lineas() #mostrar un separador de líneas
            print() #espacio en blanco para mejorar la legibilidad
    print(f"\n?? ¡Se agotaron los intentos! El número era {numero_secreto}") #mensaje de error si se agotan los intentos
    
    return False  # Indica que perdió

def main(): #función principal del programa
    print("¡Bienvenido al Juego de Adivinanza!")
    
    while True: #bucle infinito para repetir el juego
        print("\n" + "="*30) #separador visual
        print("1. Jugar") #opción para jugar
        print("2. Salir") #opción para salir del juego
        
        opcion = input("Elige una opción: ") #pedir al usuario que elija una opción
        mostrar_separador_lineas() #mostrar un separador de líneas
        print() #espacio en blanco para mejorar la legibilidad
        
        if opcion == "1": #si el usuario elige jugar
            gano = jugar_adivinanza() #llamar a la función jugar_adivinanza
            if gano: #si el usuario gana
                print("¡Eres muy bueno adivinando!") #mensaje de éxito
            else:
                print("¡Mejor suerte la próxima vez!") #mensaje de error si el usuario pierde
        elif opcion == "2": #si el usuario elige salir
            print("¡Gracias por jugar!") #mensaje de despedida
            break #salir del bucle
        else: #si el usuario elige una opción inválida
            print("? Opción inválida") #mensaje de error si la opción no es válida

# Ejecutar el programa
if __name__ == "__main__": #verificar si el script se está ejecutando directamente
    main() #llamar a la función principal
    #juego de adivinanza de un número secreto
            

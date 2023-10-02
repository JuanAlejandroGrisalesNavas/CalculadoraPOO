from operacion import *
from convertir import *

while True:
    try:
        numero1 = float(input("Ingresa el primer número: "))
        while True:
            signo1 = input("Ingresa el signo del primer número (+ o -): ")
            if signo1 in ['+', '-']:
                break
            else:
                print("Error: Ingresa un signo válido (+ o -).")

        numero2 = float(input("Ingresa el segundo número: "))
        while True:
            signo2 = input("Ingresa el signo del segundo número (+ o -): ")
            if signo2 in ['+', '-']:
                break
            else:
                print("Error: Ingresa un signo válido (+ o -).")

        operacion = int(input("¿Qué operación deseas realizar?\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Máximo\n6. Mínimo\n7. Promedio\n8. Salir\n"))

        # Ajusta el signo del número según la entrada del usuario
        numero1 = numero1 if signo1 == '+' else -numero1
        numero2 = numero2 if signo2 == '+' else -numero2

        calculadora = CalculadoraNumeroTexto(numero1)

        if operacion == 1:
            resultado, texto, operacion_str = calculadora.sumar(numero2)
        elif operacion == 2:
            resultado, texto, operacion_str = calculadora.restar(numero2)
        elif operacion == 3:
            resultado, texto, operacion_str = calculadora.multiplicar(numero2)
        elif operacion == 4:
            if numero2 == 0:
                print("Error: División por cero")
            else:
                resultado, texto, operacion_str = calculadora.dividir(numero2)
        elif operacion == 5:
            resultado = calculadora.maximo(numero2)
            operacion_str = "máximo"
            texto = numero_a_letras(resultado)
        elif operacion == 6:
            resultado = calculadora.minimo(numero2)
            operacion_str = "mínimo"
            texto = numero_a_letras(resultado)
        elif operacion == 7:
            resultado, texto, operacion_str = calculadora.calcular_promedio(numero2)
        elif operacion == 8:
            print("Gracias por usar la calculadora")
            break
        else:
            print("Error: Ingresa un número válido.")

        print(f"El resultado de la {operacion_str} es: {resultado} y en texto es: {texto}")

    except ValueError:
        print("Error: Ingresa un número válido.")
    except OverflowError:
        print("Error: Número demasiado alto.")
    except KeyboardInterrupt:
        print("Gracias por usar la calculadora")
        break
    except Exception as e:
        print("Error:", e)
        

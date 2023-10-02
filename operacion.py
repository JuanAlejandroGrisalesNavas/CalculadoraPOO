from convertir import numero_a_letras

class CalculadoraNumeroTexto:
    def __init__(self, numero):
        self.numero = numero


    def sumar(self, otro_numero):
        resultado = self.numero + otro_numero
        texto = numero_a_letras(resultado)
        return resultado, texto, "suma"

    def restar(self, otro_numero):
        resultado = self.numero - otro_numero
        texto = numero_a_letras(resultado)
        return resultado, texto, "resta"

    def multiplicar(self, otro_numero):
        resultado = self.numero * otro_numero
        texto = numero_a_letras(resultado)
        return resultado, texto, "multiplicación"

    def dividir(self, otro_numero):
        if otro_numero == 0:
            return "Error: división por cero"
        resultado = self.numero / otro_numero
        texto = numero_a_letras(resultado)
        return resultado, texto, "división"

    def maximo(self, otro_numero):
        return self.numero if self.numero > otro_numero else otro_numero
    
    def minimo(self, otro_numero):
        return self.numero if self.numero < otro_numero else otro_numero

    def calcular_promedio(self, otro_numero):
        suma = self.numero + otro_numero
        promedio = suma / 2
        texto = numero_a_letras(promedio)
        return promedio, texto, "promedio"









#minimunn number
#average    



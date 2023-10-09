MAX_NUMERO = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999

UNIDADES = (
    'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve',
    'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve'
)

DECENAS = (
    '', '', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'
)

DIEZ_DIEZ = (
    '', '', 'veinti', 'treinta y ', 'cuarenta y ', 'cincuenta y ', 'sesenta y ', 'setenta y ', 'ochenta y ', 'noventa y '
)

CIENTOS = (
    '_', 'ciento', 'doscientos', 'trescientos', 'cuatroscientos', 'quinientos', 'seiscientos', 'setecientos',
    'ochocientos', 'novecientos'
)

MILES = (
    'mil', 'millón', 'billón', 'trillón', 'cuatrillón', 'quintillón', 'sextillón', 'septillón', 'octillón',
    'nonillón'
)


def numero_a_letras(numero):
    numero_entero = int(numero)
    if numero_entero > MAX_NUMERO:
        raise OverflowError('Número demasiado alto')
    if numero_entero < 0:
        return 'menos %s' % numero_a_letras(abs(numero))
    letras_decimal = ''
    parte_decimal = int(round((abs(numero) - abs(numero_entero)) * 100))
    if parte_decimal > 9:
        letras_decimal = 'punto %s' % numero_a_letras(parte_decimal)
    elif parte_decimal > 0:
        letras_decimal = 'punto cero %s' % numero_a_letras(parte_decimal)
    if (numero_entero <= 99):
        resultado = leer_decenas(numero_entero)
    elif (numero_entero <= 999):
        resultado = leer_centenas(numero_entero)
    elif (numero_entero <= 999999):
        resultado = leer_miles(numero_entero)
    elif (numero_entero <= 999999999):
        resultado = leer_millones(numero_entero)
    elif (numero_entero <= 999999999999):
        resultado = leer_miles(numero_entero)
    elif (numero_entero <= 999999999999999):
        resultado = leer_millones(numero_entero)
    elif (numero_entero <= 999999999999999999):
        resultado = leer_milMillones(numero_entero)
    elif (numero_entero <= 999999999999999999999):
        resultado = leer_billones(numero_entero)
    elif (numero_entero <= 999999999999999999999999):
        resultado = leer_trillones(numero_entero)
    elif (numero_entero <= 999999999999999999999999999):
        resultado = leer_cuatrillones(numero_entero)
    elif (numero_entero <= 999999999999999999999999999999):
        resultado = leer_quintillones(numero_entero)
    elif (numero_entero <= 999999999999999999999999999999999):
        resultado = leer_sextillones(numero_entero)
    elif (numero_entero <= 999999999999999999999999999999999999):
        resultado = leer_septillones(numero_entero)
    elif (numero_entero <= 999999999999999999999999999999999999999):
        resultado = leer_octillones(numero_entero)
    elif (numero_entero <= 999999999999999999999999999999999999999999):
        resultado = leer_nonillones(numero_entero)
    else:
        resultado = 'un googol'



    if parte_decimal > 0:
        resultado = '%s %s' % (resultado, letras_decimal)
    return resultado

def leer_decenas(numero):
    if numero < 10:
        return UNIDADES[numero]
    elif numero < 20:
        return UNIDADES[numero]
    else:
        decena, unidad = divmod(numero, 10)
        return DIEZ_DIEZ[decena] + UNIDADES[unidad]

def leer_centenas(numero):
    centena, decena = divmod(numero, 100)
    resultado = CIENTOS[centena]
    if decena > 0:
        resultado += ' ' + leer_decenas(decena)
    return resultado

def leer_miles(numero):
    millar, centena = divmod(numero, 1000)
    resultado = ''
    if millar == 1:
        resultado = ''
    elif millar == 100:
        resultado = 'cien'
    else:
        resultado = leer_centenas(millar)
    if centena > 0:
        resultado = '%s %s' % (resultado, leer_centenas(centena))
    return resultado

def leer_millones(numero):
    millon, millar = divmod(numero, 1000000)
    resultado = ''
    if millon == 1:
        resultado = 'un millón'
    elif millon > 1 and millon <= 999:
        resultado = leer_centenas(millon) + ' millones'
    elif millon > 999:
        resultado = 'Error: número demasiado grande para esta función'
    if millar > 0:
        resultado = '%s %s' % (resultado, leer_miles(millar))
    return resultado



def leer_milMillones(numero):
    milMillon, millon = divmod(numero, 1000000000)
    if milMillon == 1:
        resultado = 'mil millones'
    elif milMillon > 1:
        resultado = leer_centenas(milMillon) + ' mil millones'
    else:
        resultado = ''
    if millon > 0:
        resultado = '%s %s' % (resultado, leer_millones(millon))
    return resultado

def leer_billones(numero):
    billon, milMillon = divmod(numero, 1000000000000)
    if billon == 1:
        resultado = 'un billón'
    elif billon > 1:
        resultado = leer_centenas(billon) + ' billones'
    else:
        resultado = ''
    if milMillon > 0:
        resultado = '%s %s' % (resultado, leer_milMillones(milMillon))
    return resultado

def leer_trillones(numero):
    trillon, billon = divmod(numero, 1000000000000000)
    if trillon == 1:
        resultado = 'un trillón'
    elif trillon > 1:
        resultado = leer_centenas(trillon) + ' trillones'
    else:
        resultado = ''
    if billon > 0:
        resultado = '%s %s' % (resultado, leer_billones(billon))
    return resultado

def leer_cuatrillones(numero):
    cuatrillon, trillon = divmod(numero, 1000000000000000000)
    if cuatrillon == 1:
        resultado = 'un cuatrillón'
    elif cuatrillon > 1:
        resultado = leer_centenas(cuatrillon) + ' cuatrillones'
    else:
        resultado = ''
    if trillon > 0:
        resultado = '%s %s' % (resultado, leer_trillones(trillon))
    return resultado

def leer_quintillones(numero):
    quintillon, cuatrillon = divmod(numero, 1000000000000000000000)
    if quintillon == 1:
        resultado = 'un quintillón'
    elif quintillon > 1:
        resultado = leer_centenas(quintillon) + ' quintillones'
    else:
        resultado = ''
    if cuatrillon > 0:
        resultado = '%s %s' % (resultado, leer_cuatrillones(cuatrillon))
    return resultado

def leer_sextillones(numero):
    sextillon, quintillon = divmod(numero, 1000000000000000000000000)
    if sextillon == 1:
        resultado = 'un sextillón'
    elif sextillon > 1:
        resultado = leer_centenas(sextillon) + ' sextillones'
    else:
        resultado = ''
    if quintillon > 0:
        resultado = '%s %s' % (resultado, leer_quintillones(quintillon))
    return resultado

def leer_septillones(numero):
    septillon, sextillon = divmod(numero, 1000000000000000000000000000)
    if septillon == 1:
        resultado = 'un septillón'
    elif septillon > 1:
        resultado = leer_centenas(septillon) + ' septillones'
    else:
        resultado = ''
    if sextillon > 0:
        resultado = '%s %s' % (resultado, leer_sextillones(sextillon))
    return resultado

def leer_octillones(numero):
    octillon, septillon = divmod(numero, 1000000000000000000000000000000)
    if octillon == 1:
        resultado = 'un octillón'
    elif octillon > 1:
        resultado = leer_centenas(octillon) + ' octillones'
    else:
        resultado = ''
    if septillon > 0:
        resultado = '%s %s' % (resultado, leer_septillones(septillon))
    return resultado

def leer_nonillones(numero):
    nonillon, octillon = divmod(numero, 1000000000000000000000000000000000)
    if nonillon == 1:
        resultado = 'un nonillón'
    elif nonillon > 1:
        resultado = leer_centenas(nonillon) + ' nonillones'
    else:
        resultado = ''
    if octillon > 0:
        resultado = '%s %s' % (resultado, leer_octillones(octillon))
    return resultado



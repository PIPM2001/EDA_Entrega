import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy_financial as npf


def tabla_amortizacion_año(capital, tasa, plazo):
    if plazo - 12 >= 0:
        plazo_p = 12
    else:
        plazo_p = plazo

    cuota = round(npf.pmt(tasa/100, plazo, -capital, 0), 2)
    datos = []
    saldo = capital

    for i in range(1, plazo_p+1):
        pago_capital = npf.ppmt(tasa/100, i, plazo, -capital, 0)
        pago_int = cuota - pago_capital
        saldo -= pago_capital  
        linea = [i, round(cuota,2), tasa, round(pago_capital, 2), round(pago_int, 2), round(saldo, 2)]
        datos.append(linea)
    
    df = pd.DataFrame(data=datos, columns=["Mes", "Cuota", "Tipo", "Capital", "Intereses", "Saldo"])
    cap = df["Capital"].sum()
    int = df["Intereses"].sum()
    return [cap, int, cuota*12, plazo_p]


def tabla_amortizacion(capital, tasa, plazo):    
    cuota = round(npf.pmt(tasa/100, plazo, -capital, 0), 2)
    datos = []
    saldo = capital

    for i in range(1, plazo+1):
        pago_capital = npf.ppmt(tasa/100, i, plazo, -capital, 0)
        pago_int = cuota - pago_capital
        saldo -= pago_capital  
        linea = [i, round(cuota,2), round(pago_capital, 2), round(pago_int, 2), round(saldo, 2)]
        datos.append(linea)

    df = pd.DataFrame(data=datos, columns=["Mes", "Cuota", "Capital", "Intereses", "Saldo"])
    return df

def tabla_amortizacion_12(capital, tasa, plazo):
    if plazo - 12 >= 0:
        plazo_p = 12
    else:
        plazo_p = plazo

    cuota = round(npf.pmt(tasa/100, plazo, -capital, 0), 2)
    datos = []
    saldo = capital

    for i in range(1, plazo_p+1):
        pago_capital = npf.ppmt(tasa/100, i, plazo, -capital, 0)
        pago_int = cuota - pago_capital
        saldo -= pago_capital  
        linea = [i, round(cuota,2), tasa, round(pago_capital, 2), round(pago_int, 2), round(saldo, 2)]
        datos.append(linea)

    df = pd.DataFrame(data=datos, columns=["Mes", "Cuota", "Tipo", "Capital", "Intereses", "Saldo"])
    return df


def total_12(capital, tasa, plazo):
    if plazo - 12 >= 0:
        plazo_p = 12
    else:
        plazo_p = plazo

    cuota = round(npf.pmt(tasa/100, plazo, -capital, 0), 2)
    saldo = capital

    for i in range(1, plazo_p+1):
        pago_capital = npf.ppmt(tasa/100, i, plazo, -capital, 0)
        pago_int = cuota - pago_capital
        saldo -= pago_capital  
        
    cuota_12 = cuota * 12
    capital_12 = capital - saldo
    int_12 = cuota_12 - capital_12
   
    return [cuota_12, capital_12, int_12]



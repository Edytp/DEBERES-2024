print("Hello world")
print("UEA")
print('BIENVENIDOS')
ID = input("CEDULA:")
print("PRODUCTOS")
a=float(input("Arroz:"))
b=float(input("Aceite:"))
c=float(input("Azucar:"))
d=float(input("Cafe:"))
total1 = (a + b + c + d)

def calcular_descuento (subtotal,descuento):
    monto_descuento = (subtotal*descuento)/100
    return monto_descuento

valor_subtotal = total1
porcentaje_descuento= 0

valor_descuento = calcular_descuento(valor_subtotal, porcentaje_descuento)
valor_total= valor_subtotal - valor_descuento
print(f'Total= {valor_total}')


print('Valor con descuento')

valor_subtotal = total1
porcentaje_descuento= int(input("Porcentaje:"))

valor_descuento = calcular_descuento(valor_subtotal, porcentaje_descuento)
valor_total= valor_subtotal - valor_descuento
print(f'Total= {valor_total}.Descuento {valor_descuento}')


#                               ACTIVIDAD 2
# La nota del trimestre está basada en
# • Nota hito individual = 30 %
# • Nota hito grupal = 20 %
# • Nota examen = 50 %
#-----------------------------------------------------------------------------------------------#


def notas():
#Datos de entrada
    nota_hitoInd=float(input('Dime tu nota en el hito individual: '))
    #Convertimos la nota en porcentaje
    print(f'Su nota real es: {nota_hitoInd*0.3}')
    nota_hitoGrup=float(input('Dime tu nota en el hito grupal: '))
    #Convertimos la nota en porcentaje
    print(f'Su nota real es: {nota_hitoGrup*0.2}')
    nota_Examen=float(input('Dime tu nota en el examen: '))
    #Convertimos la nota en porcentaje
    print(f'Su nota real es: {nota_Examen*0.5}')
    #Sumamos todas las notas con su porcentaje aplicado
    notatrimestre=nota_hitoInd*0.3+nota_hitoGrup*0.2+nota_Examen*0.5
    #Mostramos la Nota Final del trimestre
    print(f'Su nota final es {notatrimestre}')
#Salida
#notas()
#                               ACTIVIDAD 3
# • Se pide calcular la nota de tu examen tipo test.
# • Serán 20 preguntas
# • Las preguntas correctas sumarán 0,5
# • Las preguntas incorrectas restarán 0,25
# • Las preguntas sin contestar tendrán 0
#-----------------------------------------------------------------------------------------------#

#Decoración del algoritmo
print('.............................................................')
print('WELCOME/BIENVENIDO/BEM-VINDO, A SUPERTEST')
print('.............................................................')

#ENTRADA
print('Este test consta de 20 preguntas')

A=int(input('¿Cuántos aciertos tuviste?: '))
E=int(input('¿Cuántos errores tuviste?: '))
B=int(input('¿Cuántos dejaste en blanco tuviste?: '))
#Datos
numPreguntas=A+E+B
calc=A*0.5
calc1=E*0.25
calc2=B*0

#Salida 
if numPreguntas==20:
    print(f'Su nota final es: {calc+calc2-calc1}')
else:
    print('La suma de preguntas debe ser igual a 20')


#                       ACTIVIDAD 4
#• Diseña un algoritmo y un diagrama de flujo para:
#• Con la base y la altura de un rectángulo, se nos pide calcular su perímetro y
# su área
#Entrada
def rectangulo():
    base=float(input('Dime la base del rectangulo: '))
    altura=float(input('Dime su altura del rectangulo: '))

    perimetro=base*2+altura*2
    base=base*altura

    print(f'El perimetro es {perimetro} y la base es {base}.')
rectangulo()



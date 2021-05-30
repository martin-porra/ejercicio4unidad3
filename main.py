from manejadorempleados import  manejador
def menu():
 print('1 - agregar horas de trabajo de un empleado contratado')
 print('2 - ver costo total de una tarea')
 print('3 - lista de todos empleados que recibiran la ayuda')
 print('4 - listar informacion y sueldo de todos los empleados')
if __name__ == '__main__':
 maneja = manejador()
 band = True
 while band == True:
  menu()
  op = input('ingresar opcion ')
  if op == '1':
   maneja.horas()
  elif op == '2':
   maneja.tarea()
  elif op == '3':
   maneja.ayuda()
  elif op == '4':
   maneja.listar()
  else:
   print('opcion incorrecta')
   band = False
  print('programa terminado')
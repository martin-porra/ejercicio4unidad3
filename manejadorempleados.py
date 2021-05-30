import numpy
from numpy import *
from datetime import datetime
from  empleadoplanta import  empplanta
from  empleadosexterno import  empexterno
from  empleadocontratado import  empcontratado
import csv
from  numpy import *
from arreglo import Arreglo
class manejador:

    def __init__(self):
         dim = int(input('indicar tamaño de arreglo '))
         self.arre = Arreglo(dim)
         self.añadir()

    def añadir(self):
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            objeto = empplanta(fila[0], fila[1], fila[2], fila[3], fila[4],fila[5])
            self.arre.agregar(objeto)
        archivo.close()
        archivo = open('contratados.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            objeto = empcontratado(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6])
            self.arre.agregar(objeto)
        archivo.close()
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter=(','))
        for fila in reader:
            objeto = empexterno(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5],fila[6],fila[7],fila[8],fila[9])
            self.arre.agregar(objeto)
        archivo.close()

    def mostrar(self):
     for x in range(0,self.arre.actual()):
      print(self.arre.a(x).dni())

    def horas(self):
        print('ingresar dni de la persona y cantidad de horas trabajadas')
        dni = input('dni ')
        for x in range(0,self.arre.actual()):
            if self.arre.a(x).dni() == dni:
                if self.arre.a(x).clase() == empcontratado:
                    horas = input('horas ')
                    self.arre.a(x).gethora(horas)
                    print('horas registradas ' + self.arre.a(x).horas())
                else:
                 print('tipo de empleado no contratado')
        print('tipo de empleado no contratado')
        print('------------------------------------------------')

    def tarea(self):
     print('tareas: carpinteria, electricidad, plomeria')
     ta = input()
     total = 0
     today = datetime.today()
     for x in range(self.arre.actual()):
         if self.arre.a(x).clase() == empexterno:
             if self.arre.a(x).tarea() == ta:
                 if today < self.arre.a(x).fecha():
                  total = total + int(self.arre.a(x).costoobra())
     print('costo total de obra ' + str(total))
     print('---------------------------------------------------')

    def ayuda(self):
      print('----------------ayuda solidaria----------------')
      for x in range(self.arre.actual()):
          if self.arre.a(x).sueldo() < 25000:
            print('-----------------------------------------')
            self.arre.a(x).lista()

    def listar(self):
        for x in range(self.arre.actual()):
            print('--------------------------------------')
            print(self.arre.a(x).nombre())
            print(self.arre.a(x).tele())
            print(self.arre.a(x).sueldo())



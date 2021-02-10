################ Librerías ################
import threading
import time

################ Crea números según el rango ################
def list1(ran):
	l1 = list()
	for i in range(ran):
		l1.append(i)
		time.sleep(0.01)
	print(l1)
	return

################ Crea números según el rango ################
def list2(ran):
	l2 = list()
	for i in range(ran):
		l2.append(i)
		time.sleep(0.01)
	print(l2)
	return

################ Menú ################
def MenuMetodos(arg1, arg2):
	###### Menú métodos ######
	print("\n----Seleccione el método----\n", "1: Prueba común.", "\n", "2: Prueba Multi-hilo.")
	mtd = int(input("Ingrese el número: "))

	###### Tiempo de inicio del proceso ######
	t0 = time.time()

	if mtd == 1:
		################ Prueba común ################
		list1(arg1)
		list2(arg2)
	elif mtd == 2:
		################ Prueba multihilo ################
		thread1 = threading.Thread(name="Tread1", target=list1, args=(arg1,))
		thread2 = threading.Thread(name="Tread2", target=list2, args=(arg2,))

		thread1.start()
		thread2.start()

		thread1.join()
		thread2.join()

	###### Tiempo de finalización del proceso ######
	tf = time.time() - t0
	print("Tiempo de ejecución:", tf)
	return

################ Entrada de parámetros ################
def Parameters():
	print("\n----Ingreso de datos----")
	###### Parámetros para las funciones ######
	arg1 = int(input("Ingrese rango 1: "))
	arg2 = int(input("Ingrese rango 2: "))
	return arg1, arg2

################ Inicio del programa ################
def Starting():
	arg1, arg2 = Parameters()
	MenuMetodos(arg1, arg2)
	out = True
	while out:
		print("\n----Menú----\n", "1: Volver al menú de métodos.", "\n", "2: Ingresar nuevos valores.", "\n", "~: Salir.")
		menu = int(input("Ingrese el número: "))

		if menu == 1:
			MenuMetodos(arg1, arg2)
		elif menu == 2:
			arg1, arg2 = Parameters()
			MenuMetodos(arg1, arg2)
		else:
			out = False

Starting()
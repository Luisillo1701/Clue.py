# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 17:26:54 2021

@author: Luis Zamora
"""
from colorama import Fore, init
import random


al = random.randrange(4)
print (Fore.RED+"Bienvenido, En algun lugar del mundo ocurrio un crimen en el transcurso de la noche, ¿descubriras que fue lo que paso?")

print(Fore.YELLOW+"Tenemos 5 sospechos, 5 objetos y 5 locaciones\n Comencemos!!")

if al == 0:
	optds= 0
	

	while optds< 10:
        
		print(Fore.GREEN + "\n El fallecido se encontro con heridas incompatibles con la vida\n ¿Sobre que te interesa saber?")
		print("\n 1.- Sospechosos\n 2.- Lugares\n 3.- Objetos")
		op = int(input())
		

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("\n En la hora del asesinato habia 5 personas mas en la casa ¿sobre quien quieres saber?\n 1.- Pedro, profesion comerciante\n 2.- Yasser, publicista\n 3.- Fernando, vigilante\n 4- Victor, deportista\n 5- jorge, medico\n")
            
			opcion_sus = int(input())
			
			if opcion_sus <= 0 or opcion_sus>5:
				print("Inalido pierdes una pregunta")
				optds= optds+1
			if opcion_sus == 1: 
				print("Pedro: (Yo me encontraba en la cocina lavando trastes sucios, escuche pasos en dormitorio)")
				optds= optds+1
			if opcion_sus == 2: 
				print("Yasser: (Estaba en la sala revisando algunos de mis asuntos laborales en trabajo, escuche que alguien lavaba los platos en la cocina)")
				optds= optds+1
			if opcion_sus == 3: 
				print("Fernando dijo (Yo me encontraba en la cocina preparando algo para comer, no escuche nada inusual)")
				optds= optds+1
			if opcion_sus == 4: 
				print("Victor (Estaba en el baño, a lo lejos vi a dos hombres platicando en el jardín)")
				optds= optds+1
			if opcion_sus == 5: 
				print("Jorge(tenia mucho sueño, me fui a dormir, no recuerdo nada fuera de lo normal antes de eso)")
				optds= optds+1

		if op == 2:
            
			print("¿Sobre que locacion te interesa saber? \n 1- Jardin\n 2- Sala\n 3- Cocina\n 4- Baño\n 5- Dormitorio\n \n El dormitorio y el baño se encuntran en la segunda planta de la casa, las demas locaciones se encuentran en la planta baja\n")
            
			opcion_lugar = int(input())
			
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_lugar == 1: 
				print("Jardin ( El jardín se encontraba en mantenimiento, el jardinero había macheteado arbustos cuando le surgió un imprevisto y tuvo que salir dejando todo en desorden)")
				optds= optds+1
			if opcion_lugar == 2: 
				print("Sala (Pedro cuenta que al entrar en la cocina vio a Yasser sentado en la sala)")
				optds= optds+1
			if opcion_lugar == 3: 
				print("Cocina (La cocina estaba limpia y todo en su lugar)")
				optds= optds+1
			if opcion_lugar == 4: 
				print("Baño (El suelo del baño tenia algo de tierra)")
				optds= optds+1
			if opcion_lugar == 5: 
				print("Dormitorio (El dormitorio muestra la cama destendida, nada fuera de lo común)")
				optds= optds+1

		if op == 3:
			print("En la casa existen 5 objetos potencialmente sospechosos\n 1- Almohada\n 2- Veneno para ratas\n 3-Machete\n 4- Destornillador\n 5- Arma de fuego\n")
        
			opcion_arma = int(input())
			
			if opcion_arma <= 0 or opcion_arma>5:
				print("Invalido")
				optds= optds+1
			if opcion_arma == 1: 
				print("La almohada se encontraba en el dormitorio ")
				optds= optds+1
			if opcion_arma == 2: 
				print("Se encontraron los frascos del veneno sellados ")
				optds= optds+1
			if opcion_arma == 3: 
				print("Machete (El machete se encontró limpio y almacenado )")
				optds= optds+1
			if opcion_arma == 4: 
				print("Ningún destornillador fue localizado fuera de su lugar")
				optds= optds+1
			if opcion_arma == 5: 
				print("Pistola (la pistola se encontró bajo llave empolvada en un cajón )")
				optds= optds+1

	
	print("Ya no cuentas con mas opotunidades de preguntar\n ¿Quien cometio el crimen?\n 1- Pedro\n 2- Yasser\n 3- Fernando\n 4- Victor\n 5- Jorge\n")
	as_ju = int(input())
	
	print("Bien, ¿con que objeto sospechas que se cometio el crimen?\n 1- Almohada\n 2- Veneno para ratas\n 3-Machete\n 4- Destornillador\n 5- Arma de fuego\n")
	arma_usuario = int(input())
	
	print("¿En que locacion supones que sucedio tan atroz acto?\n 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n")
	lugar_usuario = int(input())
    
	if as_ju == 3 and arma_usuario ==1 and lugar_usuario ==3:
		print("en algún momento de la noche, luis y Fernando se encontraron discutiendo en el jardín, la discusión subió de tono y en un momento de descontrol Fernando alcanzo el machete que se encontraba en el jardín, causo heridas graves al fallecido y trato de encubrir el arma limpiándola y dejandola almacenada en otro sitio.")
	else:
		print("Algunas de tus elecciones son erroneas")

elif al == 1:
	optds= 0
	

	while optds< 10:

		print("\n Al parecer Luis el fallecido se encontraba descansando, cuando lo revisaron se percataron que ya no contaba con vida\n ¿Sobre que deseas preguntar?")
		print("\n 1.- Sospechosos\n 2.- Lugares\n 3.- Objetos\n")
		op = int(input())
		

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("\n Elegiste preguntarle a los sospechosos que se encontraban haciendo en la presunta hora del fallecimiento\n ¿A quien le quieres preguntar?\n 1.- Fernando, profesion vigilante\n 2.- Yasser, publicista\n 3.- Pedro comerciante\n 4- Victor, deportista\n 5- jorge, medico\n")
			opcion_sus = int(input())
			
			if opcion_sus <= 0 or opcion_sus>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_sus == 1: 
				print("Fernando (Estuve toda la noche en la fiesta del jardín, no vi nada sospechoso, ya estábamos borrachos, no recuerdo mucho)")
				optds= optds+1
			if opcion_sus == 2: 
				print("Yasser (yo estaba en el jardín, revisando mis asuntos, todos se veían tranquilos)")
				optds= optds+1
			if opcion_sus == 3: 
				print("Pedro (Me encontraba charlando con todos en el jardín, No recuerdo mucho, creo que me pase de tragos, esas bebidas estaban buenas)")
				optds= optds+1
			if opcion_sus == 4: 
				print("Victor (Yo casi no bebo, yasser preparo unas bebidas que se veían buenas, así que tomamos bastante, después de eso solo recuerdo que platicamos casi toda la noche)")
				optds= optds+1
			if opcion_sus == 5: 
				print("Jorge (la reunión era agradable pero me tuve que al comenzar la noche, por cuestiones de mi trabajo, yo no estaba ahí, no podría decir quien cometió tal acto)")
				optds= optds+1

		if op == 2:
			print("¿Sobre que locacion te interesa saber? \n 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n \n El dormitorio y el baño se encuntran en la segunda planta de la casa, las demas locaciones se encuentran en la planta baja\n")
			opcion_lugar = int(input())
			
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_lugar == 1: 
				print("Jardín (En el jardín había una reunión, no parece nada fuera de su lugar)")
				optds= optds+1
			if opcion_lugar == 2: 
				print("Sala (No se tiene información del interior de la casa a la hora del fallecimiento)")
				optds= optds+1
			if opcion_lugar == 3: 
				print("Cocina (No se tiene información del interior de la casa a la hora del fallecimiento)")
				optds= optds+1
			if opcion_lugar == 4: 
				print("Baño (No se tiene información del interior de la casa a la hora del fallecimiento)")
				optds= optds+1
			if opcion_lugar == 5: 
				print("Dormitorio (No se tiene información del interior de la casa a la hora del fallecimiento)")
				optds= optds+1

		if op == 3:
			print("En la casa existen 5 objetos potencialmente sospechosos\n 1- Machete \n 2- Veneno para ratas\n 3-Almohada\n 4- Destornillador\n 5- Arma de fuego\n")
			opcion_arma = int(input())
			
			if opcion_arma <= 0 or opcion_arma>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_arma == 1: 
				print("Machete (el machete no muestra signos de haber sido utilizado recientemente)")
				optds= optds+1
			if opcion_arma == 2: 
				print("Veneno para ratas (El casero informa que compro veneno para ratas debido a que tenia un problema de plaga en la casa, comenta que de los frascos que compro solo abrió uno, no recuerda donde coloco el frasco)")
				optds= optds+1
			if opcion_arma == 3: 
				print("Almohada (la almohada no se encontró en el dormitorio)")
				optds= optds+1
			if opcion_arma == 4: 
				print("Destornillador (No fue posible localizar destornilladores en la casa a pesar de que el casero nos confirma que contaba con varios)")
				optds= optds+1
			if opcion_arma == 5: 
				print("El arma que se encontraba en la pared como parte de la decoración de la casa parece estar en su lugar ")
				optds= optds+1

	
	print("\n Ya no cuentas con mas opotunidades de preguntar\n ¿Quien cometio el crimen?\n 1- Fernando\n 2- Yasser\n 3- Pedro\n 4- Victor\n 5- Jorge\n")
	as_ju = int(input())
	
	print("\n Bien, ¿con que objeto sospechas que se cometio el crimen?\n 1- Machete\n 2- Veneno para ratas\n 3- Almohada\n 4- Destornillador\n 5- Arma de fuego\n")
	arma_usuario = int(input())
	
	print("\n ¿En que locacion supones que sucedio tan atroz acto?\n 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n")
	lugar_usuario = int(input())
	

	if as_ju == 2 and arma_usuario ==2 and lugar_usuario ==1:
		print("Por problemas que vienen arrastrando desde muy jóvenes parece que había una rivalidad entre Yasser y luis. Esta pareció ser la ocasión perfecta para Yasser, preparo bebidas y a una de ellas le agrego el veneno que termino con la vida del fallecido")
	else:
		print("Haz fallado en tus selecciones ")

elif al == 2:
	
	optds= 0
	

	while optds<10 :

		print("\n Se reporta que el fallecido fue localizado aparentemente descansando\n ¿sobre que deseas preguntar?\n")
		print("\n 1.- Sospechosos\n 2.- Lugares\n 3.- Objetos\n")
		op = int(input())
		

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("\n Elegiste preguntarle a los sospechosos que se encontraban haciendo en la presunta hora del fallecimiento\n ¿A quien le quieres preguntar?\n 1.- Fernando, profesion vigilante\n 2.- Yasser, publicista\n 3.- Pedro comerciante\n 4- Victor, deportista\n 5- jorge, medico\n")
			opcion_sus = int(input())
			
			if opcion_sus <= 0 or opcion_sus>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_sus == 1: 
				print("Fernando (Yo me estaba dando una ducha, no escuche nada fuera de lo normal, antes de ducharme recuerdo que escuche algunas voces en el pasillo)")
				optds= optds+1
			if opcion_sus == 2: 
				print("Yasser (Yo me encontraba en la sala, me senti mal y Jorge se ofreció a revisarme, estuvimos ahí un tiempo considerable)")
				optds= optds+1
			if opcion_sus == 3: 
				print("Pedro (Estaba en la sala, después fui al baño pero se encontraba ocupado, alguien se estaba duchando)")
				optds= optds+1
			if opcion_sus == 4: 
				print("Victor (Yo fui a descansar un rato al jardin después de preparme una bebida, solo recuero haber visto a Yasser recostado y a Jorge revisándolo)")
				optds= optds+1
			if opcion_sus == 5: 
				print("Jorge (había tenido un día pesado en el trabajo, solo recuerdo a dos personas y después me quede dormido junto a otro mas)")
				optds= optds+1

		if op == 2:
			print("¿Sobre que locacion te interesa saber?\n  1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n \n El dormitorio y el baño se encuntran en la segunda planta de la casa, las demas locaciones se encuentran en la planta baja\n")
			opcion_lugar = int(input())
			
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_lugar == 1: 
				print("Jardin ( una de las sillas del jardín parece que estuvo ocupada recientemente)")
				optds= optds+1
			if opcion_lugar == 2: 
				print("Sala (En la sala parece indicar que hubo almenos dos personas ahí esa noche )")
				optds= optds+1
			if opcion_lugar == 3: 
				print("Dormitorio (Parece ser que alguien escucho dos voces camino al dormitorio)")
				optds= optds+1
			if opcion_lugar == 4: 
				print("Baño (alguien argumenta que el baño se encontraba ocupado por un tiempo)")
				optds= optds+1
			if opcion_lugar == 5: 
				print("Cocina (Alguien parece haber preparado algo para cenar)")
				optds= optds+1

		if op == 3:
			print("\n En la casa existen 5 objetos potencialmente sospechosos\n 1- Machete\n 2- Veneno para ratas\n 3-Almohada\n 4- Destornillador\n 5- Arma de fuego\n")
			opcion_arma = int(input())
			
			if opcion_arma <= 0 or opcion_arma>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_arma == 1: 
				print("Machete, Todas las herramientas de trabajo están ordenadas y en su lugar.")
				optds= optds+1
			if opcion_arma == 2: 
				print("Veneno para ratas (Se encontró un frasco vacio, de este producto)")
				optds= optds+1
			if opcion_arma == 3: 
				print("Almohada (la almohada estaba en la cama)")
				optds= optds+1
			if opcion_arma == 4: 
				print("Destornillador Todas las herramientas de trabajo están ordenadas y en su lugar.")
				optds= optds+1
			if opcion_arma == 5: 
				print("Arma de fuego (el arma se encontró resguardada bajo llave, tiene indicios de haber sido manipulada recientemente)")
				optds= optds+1

	
	print("\n Ya no cuentas con mas opotunidades de preguntar\n ¿Quien cometio el crimen?\n 1- Fernando\n 2- Yasser\n 3- Pedro\n 4- Victor\n 5- Jorge\n")
	as_ju = int(input())
	
	print("\n Bien, ¿con que objeto sospechas que se cometio el crimen?\n 1- Machete\n 2- Veneno para ratas\n 3-Almohada\n 4- Destornillador\n 5- Arma de fuego\n")
	arma_usuario = int(input())
	
	print("\n ¿En que locacion supones que sucedio tan atroz acto?\n 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n")
	lugar_usuario = int(input())
	

	if as_ju == 3 and arma_usuario ==3 and lugar_usuario ==3:
		print("\n Pedro es el dueño de un comercio el cual tiene como único competidor a otro comercio propiedad de luis, parece ser que quiso ser el único en la zona. ")
	else:
		print("No has resuelto el caso :c")

	
elif al == 3:
	
	optds= 0
	

	while optds< 10:

		print("\n Alguien a cometido un terrible acto, Luis fue asesinado cruelmente\n ¿Sobre que deseas saber?")
		print("\n 1.- Sospechosos\n 2.- Lugares\n 3.- Objetos\n")
		op = int(input())
		

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("\n Elegiste preguntarle a los sospechosos que se encontraban haciendo en la presunta hora del fallecimiento\n ¿A quien le quieres preguntar?\n 1.- Fernando, profesion vigilante\n 2.- Yasser, publicista\n 3.- Pedro comerciante\n 4- Victor, deportista\n 5- jorge, medico\n")
			opcion_sus = int(input())
			
			if opcion_sus <= 0 or opcion_sus>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_sus == 1: 
				print("Fernando (Estaba muy cansado fui al dormitorio a dormir, no recuerdo mas)")
				optds= optds+1
			if opcion_sus == 2: 
				print("Yasser (Me quede a dormir en la sala, solo escuche algo que cayo pero no recuerdo si fue arriba o afuera, no vi nada ni a nadie mas)")
				optds= optds+1
			if opcion_sus == 3: 
				print("Pedro (acampe afuera, no supe nada mas)")
				optds= optds+1
			if opcion_sus == 4: 
				print("Victor (Estaba viendo la tele en la sala, veía una película de acción no escuche nada fuera de eso)")
				optds= optds+1
			if opcion_sus == 5: 
				print("Jorge (Preparaba  mi almuerzo para el día siguiente salir mas temprano por asuntos laborales)")
				optds= optds+1

		if op == 2:
			print("\n ¿Sobre que locacion te interesa saber? \n 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n \n El dormitorio y el baño se encuntran en la segunda planta de la casa, las demas locaciones se encuentran en la planta baja\n")
			opcion_lugar = int(input())
			
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_lugar == 1: 
				print("Jardín (En el jardin se encontro una casa de acampar, lo demás en su lugar)")
				optds= optds+1
			if opcion_lugar == 2: 
				print("Sala (Jorge recuerda haber visto a alguien dormido en la sala)")
				optds= optds+1
			if opcion_lugar == 3: 
				print("Dormitorio (El dormitorio parece haber sido ocupado recientemente )")
				optds= optds+1
			if opcion_lugar == 4: 
				print("Baño (El baño presentaba alguna fugas de rápida solucion)")
				optds= optds+1
			if opcion_lugar == 5: 
				print("Cocina (Los sartenes y quemadores aun estaban calientes en la revisión )")
				optds= optds+1

		if op == 3:
			print("En la casa existen 5 objetos potencialmente sospechosos\n 1- Machete\n 2- Veneno para ratas\n 3-Almohada\n 4- Destornillador\n 5- Arma de fuego\n")
			opcion_arma = int(input())
			
			if opcion_arma <= 0 or opcion_arma>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_arma == 1: 
				print("Machete (El machete no se encontro por ningún lado)")
				optds= optds+1
			if opcion_arma == 2: 
				print("Veneno para ratas (Todos los frascos de veneno estaban cerrados)")
				optds= optds+1
			if opcion_arma == 3: 
				print("Almohada (La almoada no se encontro en el dormitorio)")
				optds= optds+1
			if opcion_arma == 4: 
				print("Destornillador (El destornillador no se encontro en su almacen)")
				optds= optds+1
			if opcion_arma == 5: 
				print("Arma de fuego (el arma de fuego se encuentra colgada como parte de la ambientación de la casa, parace haber sido limpiada recientemente )")
				optds= optds+1

	
	print("\n Ya no cuentas con mas opotunidades de preguntar\n ¿Quien cometio el crimen?\n 1- Fernando\n 2- Yasser\n 3- Pedro\n 4- Victor\n 5- Jorge\n")
	as_ju = int(input())
	
	print("\n Bien, ¿con que objeto sospechas que se cometio el crimen?\n 1- Machete\n 2- Veneno para ratas\n 3-Almohada\n 4- Destornillador\n 5- Arma de fuego\n")
	arma_usuario = int(input())
	
	print("\n ¿En que locacion supones que sucedio tan atroz acto?\n 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n")
	lugar_usuario = int(input())

	if as_ju == 4 and arma_usuario ==4 and lugar_usuario ==4:
		print("\n Victor mato a luis con varias heridas de destornillador debido a una deuda pasional, victor es hombre de cuidado")
	else:
		print("Algunas de tus selecciones fueron erroneas")

elif al == 4:
	
	optds= 0
	

	while optds< 10:

		print("En la noche anterior ocurrio una muerte, tenemos que descubir que fue lo que paso")
		print("\n 1.- Sospechosos\n 2.- Lugares\n 3.- Objetos\n")
		op = int(input())
		

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("Elegiste preguntarle a los sospechosos que se encontraban haciendo en la presunta hora del fallecimiento\n ¿A quien le quieres preguntar?\n 1.- Fernando, profesion vigilante\n 2.- Yasser, publicista\n 3.- Pedro comerciante\n 4- Victor, deportista\n 5- jorge, medico\n")
			opcion_sus = int(input())
			
			if opcion_sus <= 0 or opcion_sus>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_sus == 1: 
				print("Fernando (dice haber estado en la sala cuando escucho una detonación de arma de fuego)")
				optds= optds+1
			if opcion_sus == 2: 
				print("Pedro (Menciona que se encontraba en la cocina cuando escucho un disparo)")
				optds= optds+1
			if opcion_sus == 3: 
				print("Yasser (dice que se encontraba en el jardín cuando escucho un disparo)")
				optds= optds+1
			if opcion_sus == 4: 
				print("Victor (Dice que estaba en el baño cuando escucho un disparo)")
				optds= optds+1
			if opcion_sus == 5: 
				print("Jorge (Se encontraba en la sala cuando escucho un disparo)")
				optds= optds+1

		if op == 2:
			print("¿Sobre que locacion te interesa saber? 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n \n El dormitorio y el baño se encuntran en la segunda planta de la casa, las demas locaciones se encuentran en la planta baja\n")
			opcion_lugar = int(input())
			
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_lugar == 1: 
				print("Jardín (Demasiado alboroto en el jardin)")
				optds= optds+1
			if opcion_lugar == 2: 
				print("Sala (se encuentra totalmente desordenada)")
				optds= optds+1
			if opcion_lugar == 3: 
				print("Dormitorio (En total desorden)")
				optds= optds+1
			if opcion_lugar == 4: 
				print("Baño (no parece nada fuera de lo normal)")
				optds= optds+1
			if opcion_lugar == 5: 
				print("Cocina (Algunos alimentos se quemaron, y otros mas se encontraban en el suelo)")
				optds= optds+1

		if op == 3:
			print("En la casa existen 5 objetos potencialmente sospechosos\n 1- Almohada\n 2- Veneno para ratas\n 3-Machete\n 4- Destornillador\n 5- Arma de fuego\n ¿Sobre cual deseas saber mas?")
			opcion_arma = int(input())
			
			if opcion_arma <= 0 or opcion_arma>5:
				print("Opcion invalida, pierdes una pregunta")
				optds= optds+1
			if opcion_arma == 1: 
				print("Machete (Tiene suciedad y no se encuentra en su lugar habitual)")
				optds= optds+1
			if opcion_arma == 2: 
				print("Veneno para ratas (No se localizo tal veneno en la zona del crimen)")
				optds= optds+1
			if opcion_arma == 3: 
				print("Almohada (Se encontraba muy maltratada)")
				optds= optds+1
			if opcion_arma == 4: 
				print("Destornillador (Tenia algo parecido a sangre seca el mango)")
				optds= optds+1
			if opcion_arma == 5: 
				print("Arma de fuego (Se encontro en el área del crimen)")
				optds= optds+1

	
	print("Ya no cuentas con mas opotunidades de preguntar\n ¿Quien cometio el crimen?\n \n 1- Pedro\n 2- Yasser\n 3- Fernando\n 4- Victor\n 5- Luis\n")
	as_ju = int(input())
	
	print("Bien, ¿con que objeto sospechas que se cometio el crimen?\n 1- Almohada\n 2- Veneno para ratas\n 3-Machete\n 4- Destornillador\n 5- Arma de fuego\n")
	arma_usuario = int(input())
	
	print("¿En que locacion supones que sucedio tan atroz acto?\n 1- Jardin\n 2- Sala\n 3- Dormitorio\n 4- Baño\n 5- Cocina\n")
	lugar_usuario = int(input())
	

	if as_ju == 5 and arma_usuario ==5 and lugar_usuario ==3:
		print("Al parecer, el fallecido habria caido en una depresion severa que lo orillo a quitarse la vida")
	else:
		print("Haz fallado ")

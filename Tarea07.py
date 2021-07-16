def menu():
    print("Bienvenido.!")
    print("")
    print("App Honduras,Departamentos,Cabeceras y Extencion Territorial")
    print("")
    print("1. Consultar todas las cabeceras departamentales de Honduras.")
    print("2. Consultar todas las extensiones territoriales de los 18 departamentos de Honduras.")
    print("")
    print("¿Que desea hacer?")
    print("1. Consultar cabecera departamental")
    print("2. Consultar extension territorial de un departamento")
    print("3. Salir")
    op = input ("Escriba la opcion:")
    op = int(op)
    if op==1: Consultar_Cabecera() 
    elif op==2: Consultar_Extension()
    else: exit()

def Consultar_Cabecera():
    print("Consulta de cabeceras departamentales de Honduras")
    print("")
    print('Lista de cabeceras')
    print("")
    print('1. Atlántida')	
    print('2. Colón	')
    print('3. Comayagua')	
    print('4. Copán	')
    print('5. Cortés')	
    print('6. Choluteca')	
    print('7. El Paraíso	')
    print('8. Francisco Morazán')
    print('9. Gracias a Dios')
    print('10. Intibucá	')
    print('11. Islas de la Bahía ')
    print('12. La Paz')
    print('13. Lempira')	
    print('14. Ocotepeque')	
    print('15. Olancho')	
    print('16. Santa Bárbara')
    print('17. Valle')
    print('18. Yoro	')

    Departamento = {'Atlántida':"La Ceiba",
    'Colón'	:"Trujillo",
    'Comayagua':"Comayagua",
    'Copán':"Santa Rosa de Copán",
    'Cortés':"San Pedro Sula",
    'Choluteca':"Choluteca",
    'El Paraíso':"Yuscarán",
    'Francisco Morazan': "Tegucigalpa",	
    'Gracias a Dios':"Puerto Lempira",
    'Intibucá':"La Esperanza",
    'Islas de la Bahia':"Roatán",
    'La Paz':"La Paz",
    'Lempira':"Gracias",	
    'Ocotepeque':"Nueva Ocotepeque",
    'Olancho':"Juticalpa",
    'Santa Bárbara':"Santa Bárbara",
    'Valle':"Nacaome",
    'Yoro':"Yoro",
    }
    Cabecera = input('Ingrese el nombre del departamento para consultar su cabecera:').title()


    if Cabecera in Departamento:
        print("")
        print("¡Bien hecho!")
        print("Nombre ingresado correctamente")
        print("")
        print("Por favor, espere...")
        print("")
        print( 'La cabecera departamental de:', Cabecera, 'es', Departamento[Cabecera],)
        print("")
    else:
        print("") 
        print("Lo siento, ha cometido un error, el nombre del departamento:", Cabecera, "fue escrito de manera incorrecta, por favor, intente de nuevo.")
        print("")
        print("Asegúrese de colocar tilde, en caso sea necesario")
        print("")
        menu()
    menu()

def Consultar_Extension():
    print("Consulta de extension territoral de cada departamento de Honduras")
    print("")
    print('Lista de cabeceras')
    print("")
    print('1. Atlántida')	
    print('2. Colón	')
    print('3. Comayagua')	
    print('4. Copán	')
    print('5. Cortés')	
    print('6. Choluteca')	
    print('7. El Paraíso	')
    print('8. Francisco Morazán')
    print('9. Gracias a Dios')
    print('10. Intibucá	')
    print('11. Islas de la Bahía ')
    print('12. La Paz')
    print('13. Lempira')	
    print('14. Ocotepeque')	
    print('15. Olancho')	
    print('16. Santa Bárbara')
    print('17. Valle')
    print('18. Yoro	')


    Departamento = {'Atlántida': '4 227 km²' ,
    'Colón'	:'8 276 km²',
    'Comayagua':'5 120 km²',
    'Copán':'3 239 km²',
    'Cortés':'3 911 km²',
    'Choluteca':'4 397 km²',
    'El Paraíso':'7 383 km²',
    'Francisco Morazan': '8 580 km²',	
    'Gracias a Dios':'15 876 km²',
    'Intibucá':'3 126 km²',
    'Islas de la Bahia':'229 km²',
    'La Paz':'2 534 km²',
    'Lempira':'4 285 km²',	
    'Ocotepeque':'1 636 km²',
    'Olancho':'24 038 km²',
    'Santa Bárbara':'5 013 km²',
    'Valle':'1 618 km²',
    'Yoro':'7 787 km²',
    }
    Extension = input('Ingrese el nombre del departamento para consultar su extension territoral:').title()


    if Extension in Departamento:
        print("")
        print("¡Bien hecho!")
        print("Nombre ingresado correctamente")
        print("")
        print("Por favor, espere...")
        print("")
        print( 'La extension territorial de:', Extension, 'es', Departamento[Extension],)
        print("")
        
    else: 
        print("")
        print("Lo siento, ha cometido un error, el nombre del departamento:", Extension, "fue escrito de manera incorrecta, por favor, intentelo de nuevo.")
        print("")
        print("Asegúrese de colocar tilde, en caso sea necesario")
        print("")
        menu()
    menu()
menu()
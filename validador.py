
def validate(opciones:list, eleccion:str):
    # Definir validación de eleccion
    ##########################################################################
    if eleccion not in opciones:
        print(f'Opción no válida, ingrese una de las opciones válidas: {opciones}')
        new_select = input("Ingrese una nueva opción: ")
        return validate(opciones, new_select)
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
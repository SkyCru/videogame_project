#importando recursos
import random



def run():
    #Total de intentos que tendrá el usuario
    lifes = 5
    print('Hola! Este es un juego donde tendrás que adivinar un número (entre 1 y 100) que se ha seleccionado aleatoriamente.')
    print('Tienes ' + str(lifes) + ' intentos.')
    #Número aleatorio
    al_num = random.randint(1, 100)
    #Solicitud de valor al usuario
    num_choice = int(input('ADIVINA EL NÚMERO ENTRE 1 Y 100: '))
    #Bucle
    while num_choice != al_num:
        if lifes == 1:
            print('HAS PERDIDO')
            break
        if num_choice < al_num:
            lifes = lifes - 1
            print('ELIGE UN NÚMERO MÁS GRANDE')
        else:
            print('ELIGE UN NÚMERO MÁS PEQUEÑO')
            lifes = lifes - 1
        print('Tienes ' + str((lifes)) + ' intentos más')
        num_choice = int(input('ADIVINA EL NÚMERO: '))
    if num_choice == al_num:
        print('¡GANASTE!')


#Instrucción para iniciar programa
if __name__ == '__main__':
    run()
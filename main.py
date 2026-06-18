import sys
from generator.password_generator import generator_password

def main():

    if len(sys.argv) < 2:
        print("Uso: python main.py <longitud>")
        return 
    
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Error: la longitud debe ser un número")
        return  

    if length < 4:
        print("Error: la longitud debe ser de 4 o más caracteres.")
        return

    password = generator_password(length)

    print("Contraseña:", password)

if __name__ == "__main__":
    main()
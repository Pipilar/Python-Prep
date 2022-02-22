import sys
if len(sys.argv) == 4:
    print('el primer argumento es', sys.argv[1])
    print('el segundo argumento es', sys.argv[2])
    print('el tercer argumento es', sys.argv[3])
else:
    print('ERROR: este script resiste solo 3 argumentos')
    print('Ejemplo: clase09_ej1mio.py 1 2 3')

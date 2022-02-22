import sys
if len(sys.argv)==4:
    import datetime
    import os # esta libreria es la que me permite usar 
    #los comandos open, write y close. 
    marcatiempo = datetime.datetime.now()
    marcatiempo = datetime.datetime.timestamp(marcatiempo)

    grados = sys.argv[1]
    humedad = sys.argv[2]
    lluvia = sys.argv[3]
    #de esta manera capturamos los parametros
    linea = str(marcatiempo) + ',' + grados + ',' + humedad + ',' + lluvia
    #creamos esta linea, porque es la variable que vamos a agregar al archivo
    #.csv, o sea la creamos para que se guarden aca los datos ingresados
    #y poder despues directamente agregar la variable 'linea'
    #al archivo .csv con los siguientes comandos:

    logs_lluvia = open('clase09_ej2.csv', 'a')
    logs_lluvia.write(linea + '\n')
    logs_lluvia.close()

else:
    print('ERROR: se esperaban 3 parametros')
    print('por ejemplo: clase09_ej2mio.py <temperatura> <humedad> <True o False> (si llovió o no)')



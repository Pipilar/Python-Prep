class Tools:
    def __init__(self,listado):
        self.lista = listado

    def es_primo(self):
        for i in self.lista:
            if self.__es_primo(i):
                print(i, 'es primo')
            else:
                print(i, 'no es primo')

    def climix(self,origen,destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__climix(i,origen,destino), 'grados', destino)

    def fachi(self):
        for i in self.lista:
            print('el factorial de', i, 'es', self.__fachi(i))


    def __es_primo(self,numero):
        primo = True
        if numero == 1 or numero == 2 or numero == 3 or numero == 5 or numero == 7:
            primo = True
        elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
            primo = False
        else:
            primo = True
        return primo

    def __climix(self,valor,origen,destino):
        valor_destino = ''
        if origen == 'Celcius':
            if destino == 'Celcius':
                valor_destino = valor
            elif destino == 'Farenheit':
                valor_destino = valor*9/5 + 32
            elif destino == 'Kelvin':
                valor_destino = valor + 273.15
        elif origen == 'Farenheit':
            if destino == 'Celcius':
                valor_destino = (valor - 32) * 5/9
            elif destino == 'Farenheit':
                valor_destino=valor
            elif destino == 'Kelvin':
                valor_destino = (valor - 32) * 5/9 + 273.15
        elif origen == 'Kelvin':
            if destino == 'Celcius':
                valor_destino = valor - 273.15
            elif destino == 'Farenheit':
                valor_destino = ((valor - 273.15)*9/5)+32
            elif destino == 'Kelvin':
                valor_destino=valor
        return valor_destino

    def __fachi(self,nro):
        fact = ''
        if type(nro) != int:
            return('ingrese un numero entero')
        if nro > 0:
            factorial = 1
            for a in range(0,nro):
                factorial = factorial * nro
                nro -= 1
            fact = factorial
        if nro < 0:
            return('ingrese un numero positivo')
        return fact
class Tools:
    def __init__(self,listado):
        if type(listado) != list:
            self.lista = [0]
            raise ValueError('Se esperaba una lista de numeros enteros') 
        self.lista = listado

    def es_primo(self):
        lista_prim = []
        for i in self.lista:            
            if self.__es_primo(i):
                lista_prim.append(True)
            else:
                lista_prim.append(False)
        return lista_prim

    def climix(self,origen,destino):
        parametros_esperados = ['Celcius','Farenheit','Kelvin']
        if str(origen) not in parametros_esperados:
            print('Los parametros esperados para origen son', parametros_esperados)
        if str(destino) not in parametros_esperados:
            print('Los parametros esperados para destino son', parametros_esperados)
        else:
            lista_conversiones = []
            for i in self.lista:
                lista_conversiones.append(self.__climix(i,origen,destino))
            return lista_conversiones
              
        
    def fachi(self):
        lista_fachi = []
        for i in self.lista:
            if type(i) == int:
                lista_fachi.append(self.__fachi(i))
            else:
                print('dentro de la lista debe haber numeros enteros')
        return lista_fachi


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
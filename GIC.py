class Pila:
    def __init__(self):
        self.items=[]
    
    def push(self, x):
        self.items.append(x)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def isEmpty(self):
        return self.items == []
    
    def lastItem(self):
        try:
            t = self.items.pop()
            self.items.append(t)
            return t
        except IndexError:
            raise ValueError("La pila está vacía")

    def clean(self):
        self.items =[]

abecedario_min = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
abecedario_may = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
operaciones = ['+', '-', '*', '/', '%']
p = Pila()


def iniciar():
    p.clean()
    p.push('Z')
    cadena = input('Ingrese una cadena: \n')
    #cadena = cadena.replace(" ", "") eliminar espacios de la cadena
    #print(p.items) imprime el contenido de la pila
    q0(cadena, 0)
    opcion = input('¿Desea ingresar otra cadena?\n1.- Si\n2.- No\n')
    while(opcion!='1' or opcion!='2'):
        if(opcion == '1'):
            iniciar()
            return
        elif(opcion == '2'):
            return
        else:
            print('Opcion invalida\n')
            opcion = input('¿Desea ingresar otra cadena?\n1.- Si\n2.- No\n')


def q0(cadena, i):
    if(i >= len(cadena)):
        print('La cadena es inválida')
        return
    elif (cadena[i] in abecedario_may and p.lastItem() == 'Z'):
        q1(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'Z'):
        q1(cadena, i+1)
    else: 
        print('La cadena es inválida')
        return

def q1(cadena, i):
    if (i >= len(cadena)):
        print('La cadena es inválida')
        return
    elif (cadena[i] in abecedario_may and p.lastItem() == 'Z'):
        q1(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'Z'):
        q1(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'Z'):
        q1(cadena, i+1)
    elif(cadena[i] == '=' and p.lastItem() == 'Z'):
        q2(cadena, i+1)
    else:
        print('La cadena es inválida')
        return

def q2(cadena, i):
    if (i >= len(cadena)):
        print('La cadena es inválida')
        return
    elif (cadena[i] == '(' and p.lastItem() == 'Z'):
        p.push('A')
        q2(cadena, i+1)
    elif (cadena[i] == '(' and p.lastItem() == 'A'):
        p.push('A')
        q2(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'Z'):
        q8(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'A'):
        q8(cadena, i+1)
    elif (cadena[i] in abecedario_may and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_may and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'A'):
        q3(cadena, i+1)
    else:
        print('La cadena es inválida')
        return

def q3(cadena, i):
    if (i >= len(cadena)):
        print('La cadena es inválida')
        return
    elif (cadena[i] in numeros and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_may and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_may and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] == ')' and p.lastItem() == 'A'):
        p.pop()
        q3(cadena, i+1)
    elif (cadena[i] == ';' and p.lastItem() == 'Z'):
        q4(cadena, i+1)
    elif (cadena[i] in operaciones and p.lastItem() == 'Z'):
        q5(cadena, i+1)
    elif (cadena[i] in operaciones and p.lastItem() == 'A'):
        q5(cadena, i+1)
    else:
        print('La cadena es inválida')
        return

def q4(cadena, i):
    if(len(cadena) == i):
        print('Cadena valida')
    else:
        print('Cadena invalida')

def q5(cadena, i):
    if (i >= len(cadena)):
        print('La cadena es inválida')
        return
    elif (cadena[i] in abecedario_may and p.lastItem() == 'Z'):
        q6(cadena, i+1)
    elif (cadena[i] in abecedario_may and p.lastItem() == 'A'):
        q6(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'Z'):
        q6(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'A'):
        q6(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] == '(' and p.lastItem() == 'Z'):
        p.push('A')
        q5(cadena, i+1)
    elif (cadena[i] == '(' and p.lastItem() == 'A'):
        p.push('A')
        q5(cadena, i+1)
    else:
        print('La cadena es inválida')
        return

def q6(cadena, i):
    if (i >= len(cadena)):
        print('La cadena es inválida')
        return
    elif (cadena[i] in numeros and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_may and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_may and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'Z'):
        q3(cadena, i+1)
    elif (cadena[i] in abecedario_min and p.lastItem() == 'A'):
        q3(cadena, i+1)
    elif (cadena[i] == ')' and p.lastItem() == 'A'):
        p.pop()
        q3(cadena, i+1)
    elif (cadena[i] in operaciones and p.lastItem() == 'Z'):
        q5(cadena, i+1)
    elif (cadena[i] in operaciones and p.lastItem() == 'A'):
        q5(cadena, i+1)
    else:
        print('La cadena es inválida')
        return

def q8(cadena, i):
    if (i >= len(cadena)):
        print('La cadena es inválida')
        return
    elif (cadena[i] in numeros and p.lastItem() == 'Z'):
        q8(cadena, i+1)
    elif (cadena[i] in numeros and p.lastItem() == 'A'):
        q8(cadena, i+1)
    elif (cadena[i] == ')' and p.lastItem() == 'A'):
        p.pop()
        q8(cadena, i+1)
    elif (cadena[i] in operaciones and p.lastItem() == 'Z'):
        q5(cadena, i+1)
    elif (cadena[i] in operaciones and p.lastItem() == 'A'):
        q5(cadena, i+1)
    elif (cadena[i] == ';' and p.lastItem() == 'Z'):
        q4(cadena, i+1)
    else:
        print('La cadena es inválida')
        return

if __name__== '__main__':
    iniciar()
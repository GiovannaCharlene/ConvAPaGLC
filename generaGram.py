import sys

	#OBTENCION DE DATOS DEL AUTOMATA DE PILA
#Funcion que convierte los strings a listas para generar las reglas
def ConvierteaLista(string):
	list1=[]
	list1[:0]=string
	return list1

#Se lee el archivo txt que contiene los datos del automata de pila, y se #guardan en sus variables string, Ss, Fs, i, Ts..
with open(sys.argv[1],'r') as f:
	contents= f.read()
	indiceDS1=contents.find('S=[')
	indiceDS2=contents.find(']',indiceDS1+3)
	Ss=contents[indiceDS1+3:indiceDS2].replace(',','')

	indiceDF1=contents.find('F=[',indiceDS2+1)
	indiceDF2=contents.find(']',indiceDS2+1)
	Fs=contents[indiceDF1+3:indiceDF2].replace(',','')

	indiceDi=contents.find('i=')
	i=contents[indiceDi+2]

	tam=len(contents)
	Ts=''
	indiceDT2=0
	indiceDT1=contents.find('T=[')
	while indiceDT2<tam-2:
		indiceDT1=contents.find('[',indiceDT1+1)
		indiceDT2=contents.find(']',indiceDT1+1)
		Ts=Ts+contents[indiceDT1+1:indiceDT2].replace(',','')	

#Convirtiendo Ts (T string) a lista para obtener las reglas
T=[]
noTrans=int(len(Ts)/5)
for j in range(noTrans):
	k=5*j
	Tp=ConvierteaLista(Ts[k:k+5])
	T.append(Tp)
#Se convierte Ss a lista
S=ConvierteaLista(Ss)
#Se convierte Fs a lista
F=ConvierteaLista(Fs)


	#GENERACION DE REGLAS 

#Funcion para obtener los simbolos de la pila
def obtenerSimbolos(str):       
	# Indice para la lista modificada
	index = 0
	# Lista a llenar de los simbolos
	simbolos=[]
	n=len(str)
      
	for i in range(0, n): 
          
		# Revisa si str[i] ha estado antes
		for j in range(0, i + 1): 
			if (str[i] == str[j]): 
				break
                  
		# si no esta presente, agregarlo al resultado 
		if (j == i): 
			str[index]=str[i]
			index += 1
	simbolos=str[:index]    
	return simbolos

    #PASO 1
#Para cada estado de aceptacion (colocado en la variable F), se forma la regla de reescritura S -> <i,/,F[j]>  
#donde / es lambda, i el estado inicial, F[j] son cada uno de los estados de aceptacion

#Cantidad de reglas en paso 1
tamReg1=len(F)
#La primera coleccion de reglas tiene que tener el tamaño igual a la cantidad de estados de aceptacion F
reglas1=[]
datos='Paso 1:\n'

for estadoA in range(tamReg1):
	reglas1.append([i,'/',F[estadoA]])
	#Se escriben las reglas1 en los datos que se ingresaran al txt
	datos=datos+'S=><'+i+',/,'+F[estadoA]+'>\n'
    
	#PASO 2
#Para cada estado en el automata de pila, se forma la regla <S[j],/,S[j]> -> /

#Cantidad de reglas en paso 2
tamReg2=len(S)
#La segunda coleccion de reglas tiene que tener el tamaño igual a la cantidad de estados en el automata de pila
reglas2=[]
datos=datos+'\nPaso 2: \n'

for estado in range(tamReg2):
	reglas2.append([S[estado],'/',S[estado]])
	#Se escriben las reglas2 en los datos
	datos=datos+'<'+S[estado]+',/,'+S[estado]+'>=>/'+'\n'

	#PASO 3
#Para cada transicion (p,x,y;q,z) con y!=/  y diferente de lambda
#donde p es desde donde va la transicion, x es la entrada, y es que se saca de la pila; q es a donde se va, z es que se mete a la pila
#Se generan reglas de la forma <p, y, r> -> x <q,z,r> donde r es cada estado del automata

    #PASO 4
#Para cada transicion (p,x,/;q,z), se generan las reglas de la forma <p, w, r> -> x <q, z, k> <k, w, r>
#donde w es un simbolo de la pila (o puede ser lambda /), k y r son estados de la pila, pueden ser iguales

#Se lee T que son las transiciones, T[j][2] es y, si T[j][2]!='/', esa transicion pertenece a las reglas3
reglas3=[]
reglas3c=''
reglas4=[]
reglas4c=''
#Para obtener la lista de simbolos en la pila
simb=[x[2] for x in T]
simbolos=obtenerSimbolos(simb)

for transicion in range(len(T)):
    #Por cada estado se genera una regla, dependiendo de y, es si pertenece a reglas3 o a reglas4
        #Si y es diferente de lambda, entonces se escribe la regla en reglas3 
	if T[transicion][2] != '/':
		for estado in range(tamReg2):
			var=[ T[transicion][0], T[transicion][2], S[estado], T[transicion][1], T[transicion][3], T[transicion][4], S[estado] ]
			reglas3.append(var)

			reglas3c=reglas3c+'<'+T[transicion][0]+','+T[transicion][2]+','+S[estado]+'>=>'+T[transicion][1]+'<'+T[transicion][3]+','+T[transicion][4]+','+S[estado]+'>\n'
        #Si y es lambda, entonces pertenece a las reglas del paso 4, o sea reglas4
	else:
            #Se itera para cada simbolo de la pila, esto para escribir w
		for sim in range(len(simbolos)):
			#Se itera para cada estado de la pila, esto para escribir r
			for estador in range(tamReg2):
			#Se itera para cada estado de la pila, esto para escribir k
				for estadok in range(tamReg2):
					var=[ T[transicion][0], simbolos[sim], S[estador], T[transicion][1], T[transicion][3], T[transicion][4], S[estadok], S[estadok], simbolos[sim], S[estador]]
					reglas4.append(var)
					reglas4c=reglas4c+'<'+T[transicion][0]+','+simbolos[sim]+','+S[estador]+'>=>'+T[transicion][1]+'<'+T[transicion][3]+','+T[transicion][4]+','+S[estadok]+'><'+S[estadok]+','+simbolos[sim]+','+S[estador]+'>\n'

datos=datos+'\nPaso 3: \n'
datos=datos+reglas3c
datos=datos+'\nPaso 4:\n'
datos=datos+reglas4c
print(datos)


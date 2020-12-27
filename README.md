# ConvAPaGLC
Convertidor de un Autómata de Pila a Gramática Libre de Contexto. 
 Este es un programa que genera las reglas de la gramática libre de contexto apartir de un autómata de pila.
 Se puede ejecutar a través de la terminal de Linux siguiendo el siguiente formato: 
$ python generaGram.py uno.txt>rglc.txt 
 Donde "uno.txt" es el archivo que contiene la información del autómata de pila (el archivo puede tener el nombre que sea siempre y cuando contenga la información requerida) y "rglc.txt" es el archivo de salida que genera el programa en el cual se encuentran las reglas obtenidas. 
Dentro del repositorio, se encuentran ejemplos de autómata de pila de entrada: uno.txt, dos.txt y tres.txt.
 uno.txt acepta el lenguaje correspondiente a L={c b^n c},
 dos.txt acepta el lenguaje correspondiente a L={x^n y^n},
 tres.txt acepta el lenguaje correspondiente a L={palíndromos de longitud par}.

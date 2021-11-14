

def turing_M(state=None,  
             blank=None,  
             rules=[],  
             tape=[], 
             final=None,  
             pos=0):  

    st = state
    if not tape:
        tape = [blank]
    if pos < 0:
        pos += len(tape)
    if pos >= len(tape) or pos < 0:
        raise print("Se inicializa mal la posicion")

    rules = dict(((s0, v0), (v1, dr, s1))
                 for (s0, v0, v1, dr, s1) in rules)  # Diccionario de datos
    """
Estado	  Simbolo lei­do	    Si­mbolo escrito	     Mov. 	Estado sig.
  p(s0)	       1(v0)	         x(v1)                R(dr)	         p(s1)
"""
    while True:
        print(st, '\t', end=" ")
        for i, v in enumerate(tape):
            if i == pos:
                print("[%s]" % (v,), end=" ")
            else:
                print(v, end=" ")
        print()

        if st == final:
            break
        if (st, tape[pos]) not in rules:
            break

        (v1, dr, s1) = rules[(st, tape[pos])]
        tape[pos] = v1  # rescribe el simbolo de la cinta

    # movimiento del cabezal
        if dr == 'left':
            if pos > 0:
                pos -= 1
            else:
                tape.insert(0, blank)
        if dr == 'right':
            pos += 1
            if pos >= len(tape):
                tape.append(blank)
        st = s1


print("Maquina de turing Test")


while True:

    print("Seleccione una opcion")
    print("1. Expresion (10)*")
    print("2. Expresion a*b")
    print("3. Expresion a*bc")
    print("4. Expresion ab*cd*")
    print("5. Calculadora de dos Numero, presione la cantidad de unos + otra cantidad de unos")
    print("6. Ejercicio de Examen")
    print("7. Salir")
    print("")


    op = int(input("Seleccione: "))
    if op == 1:

        turing_M(state='q0',  # estado inicial de la maquina de turing
             blank='z',  # simbolo blanco de el alfabeto dela cinta
             # inserta los elementos en la cinta
             tape=list(input("Digite la cadena: ")),
             final='q1',  # estado valido y/o final
             rules=map(tuple,  # reglas de transicion
                       [
                           "q0 1 x right q0".split(),
                           "q0 0 0 right q0".split(),
                           "q0 z z right q1".split(),
                       ]
                       )
             )

        print("")     

    elif op == 2:

        turing_M(state='q0',  
             blank='z',  
             tape=list(input("Digite la cadena: ")),
             final='q2', 
             rules=map(tuple,  
                       [
                           "q0 a a right q0".split(),
                           "q0 b b right q1".split(),
                           "q1 z z right q2".split(),
                       ]
                       )
             )
        print("")

    elif op == 3:

        turing_M(state='q0',  
             blank='z',  
             tape=list(input("Digite la cadena: ")),
             final='q3', 
             rules=map(tuple,  
                       [
                           "q0 a a right q0".split(),
                           "q0 b b right q1".split(),
                           "q1 c c right q2".split(),
                           "q2 z z right q3".split(),
                       ]
                       )
             )
        print("")

    elif op == 4:

        turing_M(state='q0',  
             blank='z', 
             tape=list(input("Digite la cadena: ")),
             final='q3',  
             rules=map(tuple,  
                       [
                           "q0 a a right q1".split(),
                           "q1 b b right q1".split(),
                           "q1 c c right q2".split(),
                           "q2 d d right q2".split(),
                           "q2 z z right q3".split(),
                       ]
                       )
             )
        print("")

    elif op == 5:

        turing_M(state='q0', 
             blank='z',        
             tape=list(input("Digite la cadena: ")),
             final='q4', 
             rules=map(tuple,  
                       [
                           "q0 1 1 right q1".split(),
                           "q1 1 1 right q1".split(),
                           "q1 + 1 right q2".split(),
                           "q2 1 1 right q2".split(),
                           "q2 z z left q3".split(),
                           "q3 1 z right q4".split(),
                       ]

                       )
             )
        print("")     
        
        
    elif op == 6:

        turing_M(state='q0', 
             blank='z',        
             tape=list(input("Digite la cadena: ")),
             final='q3', 
             rules=map(tuple,  
                       [
                           "q0 0 0 right q0".split(),
                           "q0 1 1 right q1".split(),
                           "q1 z z right q2".split(),
                        ]

                       )
             )
        print("")    




    elif op == 7:
        if op > 6:
            break    

    else:
        print("Seleccione un valor correcto")

    
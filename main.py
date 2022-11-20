matrix = []
diagonal_principal = []
graus = []
arestas = 0
lacos = False
aresta_multipla = False
completo = True
regular = True
bipartido = True

x = [0]
y = []

print("""\nIntegrantes do grupo:
Caio de Souza Conceição (RA: 22.122.033-8)
Samir Oliveira da Costa (RA: 22.122.030-4)
Lucas Rebouças Silva (RA: 22.122.048-6) \n""")
with open ("A.txt", "r") as file:
    file = file.readlines()
    for i in file:
        i = i.split(" ")
        i[-1] = i[-1].strip("\n")
        matrix.append(i) #Tirar o \n
    print("Matriz lida: ")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("")

    for i in range(len(matrix)):
        graus.append(0)
        for j in range(len(matrix[i])):

            element = int(matrix[i][j])
            graus[i]+=element
            
            if j > i:
                if element == 0:
                    completo = False
                arestas+=element
                if element > 1:
                    aresta_multipla = True
                    print("\nArestas múltiplas entre: ", end="")
                    print("V%d e V%d" %(i+1, j+1))

            if i == j:
                arestas+=element
                graus[i]+=element
                diagonal_principal.append(element)
                if element > 0:
                    lacos = True

            if i in x and element != 0 and j not in y:
                if j in x:
                    bipartido = False
                else:
                    y.append(j)
            elif i in y and element != 0 and j not in x:
                if j in y:
                    bipartido = False
                else:
                    x.append(j)

if aresta_multipla and lacos:
    print("\nO grafo não é simples, pois existem arestas múltiplas e laços.")
    print("\nHá laço(s) no(s) vértice(s):", end=" ")
elif aresta_multipla:
    print("\nO grafo não é simples, pois existem arestas múltiplas.")
elif lacos:
    print("\nO grafo não é simples, pois existem laços")
    print("\nHá laço(s) no(s) vértice(s):", end=" ")
else:
    print("\nO grafo é simples, pois não apresenta arestas múltiplas ou laços.")

for i in diagonal_principal:
    if i != 0:
        print("V%d" %(diagonal_principal.index(i)+1), end=" ")

print("\n\nGraus dos vértices: ")
count = 0
for i in graus:
    count+=1
    print("gr(v%d) = %d" %(count, i))

print("\nNúmero de arestas: %d" %arestas)

if completo: 
    print("O grafo é completo, pois apresenta seu número máximo de arestas possíveis.")
else:
    print("\nO grafo não é completo, pois não apresenta seu número máximo de arestas possíveis.")

for i in graus:
    if i != graus[0]:
        regular = False
if regular:    
    print("\nO grafo é regular, pois os vértices tem o mesmo número de adjacências.")
else:
    print("\nO grafo não é regular, pois os vértices não tem o mesmo número de adjacências.")
        
if bipartido:
	print("\nO grafo é bipartido, pois é possivel dividir os vértices em dois conjuntos disjuntos U e V tais que toda aresta conecta um vértice em U a um vértice em V.")

if bipartido:
    print("\nBipartição: ")
    print("X={", end="")
    for i in x:
        if i==x[-1]:
            print("v{0}".format(i+1),end="}\n")
        else:
            print("v{0}".format(i+1),end=", ")
    print("Y={", end="")
    for i in y:
        if i==y[-1]:
            print("v{0}".format(i+1),end="}\n")
        else:
            print("v{0}".format(i+1),end=", ")
else:	
	print("\nO grafo não é bipartido, pois não é possível dividir os vértices em dois conjuntos disjuntos U e V tais que toda aresta conecta um vértice em U a um vértice em V.")

if aresta_multipla or lacos:
    print("\nNão é bipartido completo, pois não é simples.")
elif bipartido==True:
    print("\nÉ bipartido completo, visto que ao dividir seus vértices em dois conjuntos, cada vértice de um conjunto se conecta com todos os vértices do outro conjunto.")
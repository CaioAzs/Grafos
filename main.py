matrix = []
diagonal_principal = []
graus = []
arestas = 0
lacos = False
aresta_multipla = False
completo = True
regular = True
bipartido = True

bolinha = [0]
quadrado = []

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
            bolinha.append()
            graus[i]+=element
            
            if j > i:
                if element == 0:
                    completo = False
                arestas+=element
                if element > 1:
                    aresta_multipla = True
                    print("\nAresta múltipla entre: ", end="")
                    print("V%d e V%d" %(i+1, j+1))
            if i == j:
            
                arestas+=element
                graus[i]+=element
                diagonal_principal.append(element)
                if element > 0:
                    lacos = True
                    bipartido = False

if aresta_multipla and lacos:
    print("\nO grafo não é simples, pois existem arestas múltiplas e laços.")
elif aresta_multipla:
    print("\nO grafo não é simples, pois existem arestas múltiplas.")
elif lacos:
    print("\nO grafo não é simples, pois existem laços")
else:
    print("O grafo é simples")
print("\nHá laço(s) no(s) vértice(s):", end=" ")
for i in diagonal_principal:
    if i != 0:
        print("V%d" %(diagonal_principal.index(i)+1), end=" ")
print("\n")
print("Graus dos vértices: ")
count = 0
for i in graus:
    count+=1
    print("gr(v%d) = %d" %(count, i))

print("\nNúmero de arestas: %d" %arestas)

if completo: 
    print("O grafo é completo")
else:
    print("\nO grafo não é completo, pois não há arestas entre CADA par de seus vértices.")

for i in graus:
    if i != graus[0]:
        regular = False
if regular:    
    print("O grafo é regular, pois os vértices tem o mesmo número de adjacências.")
else:
    print("O grafo não é regular, pois os vértices não tem o mesmo número de adjacências.")
        
if bipartido:
    print("O grafo é bipartido.")
else:
    print("O grafo não é bipartido.")
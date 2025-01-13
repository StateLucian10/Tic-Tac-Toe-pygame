def pion_joc():
    jucator = input("Alege (X sau 0) :")
    return jucator

def init():
    L = 9 * ['.']
    return L


def alegere_jucator(joc):
    sum1 = 0
    sum2 = 0

    for i in range(9):
        if joc[i] == 'X':
            sum1 += 1
        elif joc[i] == 'O':
            sum2 += 1
    
    if pion == 'X':
        if sum1 == sum2:
            return pion  #randul omului
        else:
            return 'O'      #Randul Calculatorului
    else:
        if sum1 == sum2:
            return pion        #Randul omului
        else:
            return 'X'   #Randul calculatorului

def lista_mutari(joc):
    L = []

    for i in range(9):
        if joc[i] == '.':
            L.append(i)

    return L

def castig(joc):
    lista1 = ['X','X','X']
    lista2 = ['O', 'O', 'O']

    if joc[0:3] == lista1 or joc[3:6] == lista1 or joc[6:9] == lista1 or \
        [joc[0], joc[3],joc[6]] == lista1 or [joc[1], joc[4],joc[7]] == lista1 or \
        [joc[2], joc[5],joc[8]] == lista1 or [joc[0], joc[4],joc[8]] == lista1 or \
        [joc[2], joc[4], joc[6]] == lista1:
            return 1
    
    elif joc[0:3] == lista2 or joc[3:6] == lista2 or joc[6:9] == lista2 or \
        [joc[0], joc[3],joc[6]] == lista2 or [joc[1], joc[4],joc[7]] == lista2 or \
        [joc[2], joc[5],joc[8]] == lista2 or [joc[0], joc[4],joc[8]] == lista2 or \
        [joc[2], joc[4], joc[6]] == lista2:
            return -1
    else:
         return 0 

def joaca_mutare(joc, mutare):
   import copy 

   joc2 = copy.copy(joc)

   piesa = alegere_jucator(joc)
   if mutare in lista_mutari(joc):
    joc2[mutare] = piesa

    return joc2

def valMax(joc, alfa, beta, adancime):
    mutari = lista_mutari(joc)

    if len(mutari) == 0 or castig(joc) !=0 or adancime == 0:
        return castig(joc), -1

    else:
        calculmax = -2
        ind_cel_mai_bun = -1

        for mutare in mutari:
            joc2 = joaca_mutare(joc, mutare)
            calcul, _ = valMin(joc2, alfa, beta, adancime-1)
            if calcul > calculmax:
                calculmax = calcul
                ind_cel_mai_bun = mutare
            alfa = max(calculmax, calcul)
            if beta <= alfa:
                break

        return calculmax, ind_cel_mai_bun  

def valMin(joc, alfa, beta, adancime):
    mutari = lista_mutari(joc)

    if len(mutari) == 0 or castig(joc) !=0 or adancime == 0:
        return castig(joc), -1

    else:
        calculmin = 2
        ind_cel_mai_bun = -1

        for mutare in mutari:
            joc2 = joaca_mutare(joc, mutare)
            calcul, _ = valMax(joc2, alfa, beta, adancime-1)
            if calcul < calculmin:
                calculmin = calcul
                ind_cel_mai_bun = mutare
            beta = min(calcul, calculmin)
            if beta <= alfa:
                break

        return calculmin, ind_cel_mai_bun    
    
def restart():
    global pion, joc
    pion = ''
    joc = init()

    
pion = ''
joc = init()
            
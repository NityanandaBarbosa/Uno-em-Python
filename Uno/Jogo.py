import random
import os
from time import sleep

x = 0
c = 0
cartas=[]
nomes=[]
njogadores=0
MatDoJogadores=[]

def lendocartas (n):
    arquivo = open('Cartas','r')
    for i in arquivo:
        i= i.split(',')
        for j in i:
            if j== "\n":
                a=0
            else:
                cartas.append(j)
    arquivo.close()
    c=qjogadores(x)
    deckJogadores(c)
    partida(c)

def qjogadores(n):
    global njogadores
    njogadores = int(input("Quantos pessoas irão jogar ?\nObs: Min: 2 jogadores.\nMax: 10 jogadores.\n"))
    while(njogadores<2 or njogadores>10):
        njogadores = int(input("Quantos pessoas irão jogar ?\nObs: Min: 2 jogadores.\nMax: 10 jogadores.\n"))
    for i in range(njogadores):
        nomedeles = input(f'Qual nome dos jogador {i+1} :\n')
        nomes.append(nomedeles)
    return  njogadores

def deckJogadores(n):
    for i in range(n):
        deck=[]
        for j in range(7):
            x = random.choice(cartas)
            cartas.remove(x)
            deck.append(x)
        MatDoJogadores.append(deck)

def partida (x):
    global MatDoJogadores
    cartasUsadas = []
    cartapassada = []
    enquantomais = False
    contEnqMais = 0
    jogoganho = False
    reverso = False
    pula = False
    c = 0
    while(jogoganho==False):
        print(f'Cartas do Jogador {c+1}: {MatDoJogadores[c]}')
        if (cartapassada == []):
            a=vazio(cartasUsadas)
            cartapassada=a
        elif (cartapassada != []):
            a,b,d,enquantomais,contEnqMais=rodada2(cartapassada,cartasUsadas,c,reverso,pula,enquantomais,contEnqMais)
            cartapassada = a
            reverso = b
            pula = d
        if(len(MatDoJogadores[c])==0):
            jogoganho=True
            print(f'\nO jogador vencedor foi {nomes[c]}!!\n')
        if(jogoganho!=True):
            if reverso == True:
                if pula==True:
                    c+= -2
                    if c<0:
                        c=x-2
                    pula=False
                else:
                    c+= -1
                    if c < 0:
                        c = x-1
            else:
                if pula==True:
                    c+= +2
                    if c>x:
                        c=1
                    pula=False
                else:
                    c+=1
                    if c == x:
                        c=0
            if(c+1>len(MatDoJogadores)):
                c=0
        sleep(2)
        os.system('clear')
def vazio(n2):
    global MatDoJogadores,c
    escolha = 99
    print(f'{nomes[c]} pode jogar qualque carta.\nObs:Cartas de efeito não funcionaram.')
    while(escolha > len(MatDoJogadores[c])):
        escolha = int(input(f"Qual carta será jogada, {nomes[c]}\n"))
    escolha1=MatDoJogadores[c][escolha - 1].split(' ')
    n2.append(escolha1)
    del MatDoJogadores[c][escolha-1]
    return escolha1

def rodada2(n1,n2,n3,n4,n5,n6,n7):
    global MatDoJogadores
    cores=['vermelho','verde','amarelo','azul']
    zero=0
    escolha= 99
    cor = 99
    confirme = False
    esc1=0
    while(confirme == False):
        while(escolha > len(MatDoJogadores[n3])):
            print(f'A carta passada passada : {n1}')
            escolha = int(input(f"Qual carta será jogada, {nomes[n3]}\nObs: 0 para pegar carta e 0 denovo para pular\n"))
            if (escolha == 0):
                escolha,zero,confirme,n2=pegacartapula(escolha,zero,n3,confirme,n2)
                if(confirme==True):
                    escolha1=['amarelo','9']
                    esc1,n6, n7, n2 = maiscarta(escolha1, n6, n7, n3, n2,escolha)
        if escolha > 0:
            escolha1 = MatDoJogadores[n3][escolha - 1].split(' ')
            if(escolha1 == n1):
                confirme = True
                n4,n5=pulareverso(escolha1,n4,n5)
                esc1,n6,n7,n2=maiscarta(escolha1,n6,n7,n3,n2,escolha)
            elif(escolha1[0] in n1):
                confirme = True
                n4,n5=pulareverso(escolha1, n4, n5)
                esc1,n6,n7,n2=maiscarta(escolha1, n6, n7, n3, n2,escolha)
            elif(escolha1[1] in n1):
                if(escolha1[1]==n1[1]):
                    print(f"A cor foi trocada para : {escolha1[0]}")
                    n4, n5 = pulareverso(escolha1, n4, n5)
                    esc1,n6,n7,n2=maiscarta(escolha1, n6, n7, n3, n2,escolha)
                confirme = True
            elif(escolha1[0] == 'coringa'):
                cor=0
                print(f'Escolha um nova cor de {cores}')
                esc1,n6,n7,n2=maiscarta(escolha1, n6, n7, n3, n2,escolha)
                while (cor > 4 or cor < 1):
                    cor = int(input("De acordo com ordem das cores escolha :\n"))
                print(f"A cor foi trocada para {cores[cor-1]}")
                escolha1[0] = cores[cor-1]
                confirme = True
            elif(n1[1]in['+2','+4'] and escolha1[1]in['+2','+4']):
                esc1,n6, n7, n2 = maiscarta(escolha1, n6, n7, n3, n2,escolha)
                confirme = True
    if(escolha!=0):
        n2.append(escolha1)
        del MatDoJogadores[n3][escolha - 1]
    else:
        escolha1 = n1
    return escolha1,n4,n5,n6,n7

def pegacartapula(esc,n2,n3,n4,n5):
    global cartas
    esc = 99
    if(len(cartas)!=0):
        ncarta=cartas
    else:
        ncarta=n5
    if (n2 == 0):
        n2 += 1
        novacarta = random.choice(ncarta)
        MatDoJogadores[n3].append(novacarta)
        print(f'As carta : {MatDoJogadores[n3]}')
        ncarta.remove(novacarta)
        if (len(cartas) != 0):
            cartas = ncarta
        else:
            n5 = ncarta
    elif (n2 > 0):
        esc = 0
        n4 = True
    return esc,n2,n4,n5

def pulareverso(esc,rev,pul):
    if(esc[1] == 'reverso'):
        if (rev == False):
            rev = True
        else:
            rev = False
    elif(esc[1]=='cancela'):
        pul = True
    return rev,pul

def maiscarta(esc,enqtmais,contEmais,contador,cartUsad,escolha):
    global cartas
    if (esc[1] not in ['+2', '+4'] or escolha == 0):
        if (enqtmais == True):
            if (len(cartas) != 0):
                ncarta = cartas
            else:
                ncarta = cartUsad
            print(f'{nomes[contador]} terá de pegar {contEmais} de cartas.\n')
            for i in range(contEmais):
                novacarta = random.choice(ncarta)
                MatDoJogadores[contador].append(novacarta)
                ncarta.remove(novacarta)
                if (len(cartas) != 0):
                    cartas = ncarta
                else:
                    cartUsad = ncarta
            contEmais = 0
            enqtmais = False
    elif(esc[1] in ['+2','+4']):
        if (enqtmais == False):
            enqtmais = True
            if(esc[1]=='+2'):
                contEmais += 2
            else:
                contEmais+=4
        else:
            if (esc[1] == '+2'):
                contEmais += 2
            else:
                contEmais += 4

    return esc,enqtmais,contEmais,cartUsad

lendocartas(x)

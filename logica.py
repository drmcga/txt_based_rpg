import random
import math

def inputl(letra:str):
    return letra[0]



class Mapa:

    #funcoes mais gerais, talvez nao permanecam aqui

    #funcao que retorna uma lista com as direcoes de uma celula
    def dires(self):
        dire = [[-1, -1],  [-1, 0], [-1, 1], [0,  -1],  [0,  0], [0,  1], [1,  -1],  [1,  0], [1,  1] ]
        return dire
    
    #calcula distancias de 2 pontos
    def map_dist(self,cor_y1, cor_x1, cor_y2, cor_x2):
        return int(math.sqrt( abs(cor_y1-cor_y2)**2 + abs(cor_x1-cor_x2)**2 ))

    #printa todo tipo de matriz, nao so mapas!
    def map_print(self):
        for i in range(self.tam):
            for j in range(self.tam):
                print(f"{self.mapa[i][j]} ", end="")
            print("\b")
    


    #inicio das funcoes de mapa
    def __init__(self, tam:int):
        self.tam = tam
        self.mapa = []
        for i in range(tam):
            self.mapa.append([])
            for j in range(tam):
                self.mapa[i].append(0)
        self.popular_mapa()
        

    #funcao que transforma as bordas de uma funcao em bordas finais
    def bordas(self):
        for i in range(self.tam):
            for j in range(self.tam):
                if i == 0 or i == self.tam-1:
                    self.mapa[i][j]=9
                elif j ==0 or j ==self.tam - 1:
                    self.mapa[i][j]=9
    
    #funcao que devolve todos os arredores de uma celula em uma funcao
    def olhar_celula(self, cor_y:int, cor_x:int):
        
        dire = self.dires()
        entorno = ""

        for i in range(9):
            try:
                entorno += str(self.mapa[cor_y+dire[i][0]][cor_x+dire[i][1]]) 
                
            except:
                entorno += "0"
        return entorno

    #voce insere uma localizacao, retorna um local aleatorio nos pontos cardinais, se estiver livre
    def minhoca_mapa(self, cor_y:int, cor_x:int, comp:int, n_tok, obj:int):
        cointoss = 0
        for _ in range(comp):
            dires= self.dires()
            buscando = True
            
            if cointoss == 2 and self.mapa[cor_y][cor_x] not in n_tok:
                buscando = False
            while buscando == True:
                saida = random.choice([1, 3, 5, 7])
                if self.mapa[cor_y+dires[saida][0]][cor_x + dires[saida][1]] not in n_tok:
                    buscando = False

            cointoss = random.randint(1,3)
            
            cor_y += dires[saida][0]
            cor_x += dires[saida][1]

            self.mapa[cor_y][cor_x]= obj
        self.mapa[cor_y][cor_x] = 8

    

    #pontos de interesse podem ser varios: saida, loja, sala secreta, tesouro...
    def interesses_mapa(self):
        pass
    
    #funcao que efetivamente cria os mapas
    def popular_mapa(self):
        self.mapa[self.tam//2][self.tam//2] = 1
        self.bordas()
        
        self.minhoca_mapa(self.tam//2, self.tam//2, 7, [2, 1, 8, 9], 2)
        self.minhoca_mapa(self.tam//2, self.tam//2, 4, [2, 1, 8, 9], 2)

        
    

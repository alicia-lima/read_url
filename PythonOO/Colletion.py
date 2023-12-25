from functools import total_ordering
#biblioteca de compração / precisa implementar __lt__ e __eq__

from collections import defaultdict
#biblioteca com valor padrão em 0
from collections import Counter

idades = [] #list
idades.extend([39,30,27,18,19]) #adiciona multiplos objetos
idades.extend([26,24])

idades_ano_que_vem = [idade+1 for idade in idades]

@total_ordering
class ContaSalario:

    def __init__ (self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other): #igualdade
        if not type(other) == ContaSalario:
            return False
        return  self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other): #Suporte de ordenação para mesma Class
        if not self._saldo == other._saldo:
            return self._saldo < other._saldo

        return self._saldo < other._saldo

    def deposita (self, valor):
        self._saldo +=valor

    def __str__(self):
        return f'Código: {self._codigo} Saldo: {self._saldo}'

conta_do_gui = ContaSalario(37)
conta_do_gui.deposita(500)
conta_da_dani = ContaSalario(37)
conta_da_dani.deposita(1000)

contas = [conta_da_dani, conta_do_gui]

usuarios = [("Guilherme", 37, 1981), ("Daniela", 31, 1987), ("Paulo", 39, 1979)] #tuplas em list
usuarios.extend([("Alicia", 26, 1997)])
#for nome, idade, nascimento in usuarios:
    #print(f'Nome: {nome} Idade:{idade}', )

#for usuario in sorted(usuarios):
    #print(usuario)

#soma de list
usuarios_data_science = [15,23,43,56] #list
usuarios_machine_learning = [13,23,56,42] #list
assistiram = usuarios_data_science.copy() #copia raza da list
assistiram.extend(usuarios_machine_learning)

#soma de conjuntos
usuarios_data_science2 = {15,23,43,56} #conjunto
usuarios_machine_learning2 = {13,23,56,42} #conjunto
assistiram2 = usuarios_data_science2 | usuarios_machine_learning2
#(No conjunto a ordem não importa) exclui repetição

#adiciona objeto no conjunto
usuarios_data_science2.add(26)

#congela o conjunto
usuarios2 = frozenset(usuarios)
#diferenciação de conjuntos / quem fez os dois
assistiram_ambas = usuarios_machine_learning2 &  usuarios_data_science2

#diferenciação de conjuntos/ quem fez apenas um deles
assistiram_data_science = usuarios_data_science2 - usuarios_machine_learning2

#diferenciação exclusiva
assistiram_apenas_um = usuarios_data_science2 ^ usuarios_machine_learning2

#print(set(assistiram)) #list exibido como conjunto (set)


#Dicionário (Mapa, etc)

aparicoes = {"Guilherme": 1, "gato": 2, "nome": 2, "vindo":1}
aparicoes["Carlos"] = 2 #adiciona elemento

del aparicoes["Carlos"] #deleta elemento

"Cachorro" in aparicoes # se elemento está dentro do dicionario

#print(aparicoes.get("Guilherme", 0)) # Chave - valor

#for elemento in aparicoes.keys(): Para as chaves
#for elemento in aparicoes.values():  Para os valores
#for elemento in aparicoes.items(): Para ambos / em forma de tupla
#['palavra {chave}' for chave in aparicoes.keys()] Adiciona uma palavra antes das chaves


meu_texto = "Bem vindo meu nome é Alicia eu gosto muito de nomes e tenho a minha gata e gosto muito de gatos"
meu_texto = meu_texto.lower()
meu_texto.split() #split () quebra a string nos espaços em branco

#sem valor defaultdict
#for palavra in meu_texto.split():
    #ate_agora = aparicoes.get(palavra, 0)
    #aparicoes[palavra] = ate_agora + 1

#com valor defaultdict
#aparicoes = defaultdict(int)
#for palavra in meu_texto.split():
    #aparicoes[palavra] += 1

#com Counter
aparicoes = Counter(meu_texto.split())
print(aparicoes)

#frequencia das letras em um texto 
aparicoes = Counter(meu_texto.lower())
total_de_caracteres = sum(aparicoes.values())
proporcoes = [(letra,frequencia/ total_de_caracteres) for letra, frequencia in aparicoes.items()]
proporcoes = Counter(dict(proporcoes)) #Ordem de tamanha dos valores

mais_comuns = proporcoes.most_common(10)
for caractere, proporcao in mais_comuns:
    print(f"{caractere} => {proporcao*100:.2f}%")

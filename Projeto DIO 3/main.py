# Olá, seja bem-vindo(a) ao meu Projeto DIO.
# Aqui terão informações a mais do que pedidas no projeto para adicionar um toque de criatividade.

# Informações do criador do script.
print("Script feito por Luis!")

# CLASSE criada para representar um herói (ou usuário).
class Heroi:
    # FUNÇÃO criada para definir as VARIÁVEIS de nome, idade e tipo.
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    # FUNÇÃO criada para definir que ataque deve ser usada para cada tipo de herói
    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'ataque indefinido'
        # Mensagem de saída do script.
        print(f"o {self.tipo} {self.nome} atacou o monstro usando {ataque}, o ataque foi tão forte que derrotou o monstro, e salvou a cidade!")

# Função para caso o usuário queira repetir o script. Melhor do que uma mega aventura são DUAS megas aventuras!
def script():

    # LORE! hehehehe
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        "Agora você, após fazer dois relatórios para no QG de heróis de Farland City, finalmente você foi chamado para uma missão!"
        "\n\"Um monstro está atacando a cidade, e você precisa atacar ele para salvar Farland City!\n"
        "Para isso, nós precisamos de seu..."   
    )

    # Variáveis usadas para o usuário responder.
    nome = input("nome,\n>>>\t")
    idade = int(input("idade,\n>>>\t"))
    tipo = input("e o tipo de herói!\" (mago, guerreiro, monge, ninja)\n>>>\t")

    heroi = Heroi(nome, idade, tipo)
    heroi.atacar()
    
    # Variável que pergunta se o usuário quer repetir o script, para ter uma segunda aventura, ou para fechar o programa.
    repetir = input("\nBravo guerreiro! Parabéns pela sua conquista, agora que você venceu esse desafio, deseja embarcar em outro? (S|N)\n>>>\t")
    if repetir == "S" or repetir == "s":
        script()
    else:
        exit()
script()

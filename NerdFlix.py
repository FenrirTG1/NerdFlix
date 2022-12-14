from datetime import date, datetime

#PROJETO NERDFLIX

#produtos
class product:
    def __init__(self, nome, codigo, preco, tipo, disponivel ):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

#listas para utilidades
detalhes = []
codigo_comprado = []
nome_comprado = []
preco_comprado = []
tipo_comprado = []
lista_de_verif = []
lista_de_confirm = []
product.codigo = 0
#mostra o produto com todos os dados
def verificacao():
    verificar = input("Produto à ser verificado: ")
    while True: 
        try:
            verificar = int(verificar)
            break
        except:
            verificar = input("Formato inválido, tente novamente: ")

    for i in range(len(detalhes)):
        verificar = str(verificar)
        if detalhes[i].codigo == verificar:
            print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
        
        verificar = int(verificar)
        if i == verificar:
            while detalhes[i].codigo != verificar:
                verificar = input("Produto inexistente, tente novamente: ")
    iniciar()
#cadastrar produtos
def cadastro():
    print("Cadastro de produtos:")
    while True:
        product.nome = input("\nNome: ")
        if product.nome == '':
            break

        product.preco = input("Preço: ")
        while True:    
            try:
                product.preco = float(product.preco)
                product.preco > 0
                break
            except:
                product.preco = input("Formato inválido, digite o preço novamente: ")

        product.tipo = input("Tipo: ")
        while product.tipo != "1" and product.tipo != "2" and product.tipo != "3":
            product.tipo = input("Formato inválido, digite o tipo novamente: ")
        product.tipo = int(product.tipo)

        product.disponivel = input("Disponível(s/n): ")
        while product.disponivel != "s" and product.disponivel != "n":
            product.disponivel = input("Formato inválido, digite novamente(s/n): ")

        #tratamento de strings
        product.codigo += 1
        if product.tipo == 1:
            product.tipo = "Série"
        elif product.tipo == 2:
            product.tipo = "Filme"
        elif product.tipo == 3:
            product.tipo = "Documentário" 
        if product.disponivel == "s":
            product.disponivel = "Disponível"
        elif product.disponivel == "n":
            product.disponivel = "Indisponível"

        #detail recebe a classe e detalhes adiciona os parâmetros na lista
        detail = product(product.nome, str(product.codigo), product.preco, product.tipo, product.disponivel)
        detalhes.append(detail)
        
        print(f"{detail.codigo}, {detail.nome}, R${detail.preco}, {detail.tipo}, {detail.disponivel}")
    iniciar()

#atualiza produtos    
def atualizar():
    #pede os novos parâmetros
    verificar = input("Produto à ser verificado: ")
    while True: 
        try:
            verificar = int(verificar)
            break
        except:
            verificar = input("Formato inválido, tente novamente: ")

        #verificação de existência       
    for i in range(len(detalhes)):
        if detalhes[i].codigo == verificar:
            print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
        if i == verificar:
            while detalhes[i].codigo != verificar:
                verificar = input("Produto inexistente, tente novamente: ")

#método de atualização
    print("1 - Atualizar nome\n2 - Atualizar preço\n3 - Atualizar Tipo\n4 - Atualizar disponibilidade")
    methodat = input("Método de atualização: ")
    while methodat != "1" and methodat != "2" and methodat != "3" and methodat != "4": 
        methodat = input("Método inválido, digite novamente: ")

#confirmar
    confirmacao = input("\nConfirmação(s/n): ")
    if confirmacao != "s" and confirmacao != "n":
        confirmacao = input("Formato inválido, digite a confirmação novamente: ")
    
    if confirmacao == "n":
        atualizar()
    
    while confirmacao != 's' and confirmacao != 'n':
        confirmacao = input("Método inválido, digite novamente: ")

    if methodat == "1" and confirmacao == "s":
        product.nome = input("\nNome: ")

        for i in range(len(detalhes)):
            detalhes[i].nome = product.nome
         
    elif methodat == "2" and confirmacao == "s":
        product.preco = input("Preço: ")
        
        while True:    
            try:
                product.preco = float(product.preco)
                product.preco > 0
                break
            except:
                product.preco = input("Formato inválido, digite o preço novamente: ")

        for i in range(len(detalhes)):
            detalhes[i].preco = product.preco

    elif methodat == "3" and confirmacao == "s":
        product.tipo = input("Tipo: ")

        while product.tipo != "1" and product.tipo != "2" and product.tipo != "3":
            product.tipo = input("Formato inválido, digite o tipo novamente: ")

        for i in range(len(detalhes)):
            detalhes[i].tipo = product.tipo

    elif methodat == "4" and confirmacao == "s":
        product.disponivel = input("Disponibilidade(s/n): ")

        while product.disponivel != "s" and product.disponivel != "n":
            product.tipo = input("Formato inválido, digite novamente(s/n): ")

        if product.disponivel == "s":
            product.disponivel = "Disponível"
        elif product.disponivel == "n":
            product.disponivel = "Indisponível"
        
        for i in range(len(detalhes)):
            detalhes[i].disponivel = product.disponivel
    iniciar()

#registra compra
def registrar_compra():
    global login
    login = input("Insira seu login: ")
    while login == '':
        login = input("Insira seu login: ")
    while True:          
        cod_conf = input("Digite o código do produto: ")
        if cod_conf == '':
            break
        for i in range(product.codigo):
            cod_conf = int(cod_conf)
            if i+1 == cod_conf:
                #verificação de existência
                if detalhes[i].disponivel == "Indisponível":
                    print("Código inválido")
                    if cod_conf == '':
                        break
                else:
                    print("\n1 - Confirmar\n2 - Cancelar")
                    confirmar_compra = input("Método: ")
                    while confirmar_compra != '1' and confirmar_compra != '2':
                        confirmar_compra = input("Método inválido, digite novamente: ") 
                    #adiciona os elementos em suas respectivas listas para impressão
                    codigo_comprado.append(cod_conf)
                    nome_comprado.append(detalhes[i].nome)
                    preco_comprado.append(detalhes[i].preco)
                    tipo_comprado.append(detalhes[i].tipo)
                    print(f"Comprado:{codigo_comprado} {nome_comprado} R${preco_comprado} {tipo_comprado}\n")
                    time()
                    break

    iniciar()

#relatório de produtos
def relatorio_produtos():
    print("\n0 - Todos os produtos\n1 - Somente filmes\n2 - Séries\n3 - Documentários\n4 - Todos os produtos disponíveis\n5 - Todos os produtos indisponíveis")
    opcao = input("\nFiltro: ")
    while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        opcao = input("Filtro inválido, tente novamente: ")
 
 #métodos e filtros
    if opcao == '0':
        for i in range(len(detalhes)):
            print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
            
    elif opcao == '1':
        for i in range(len(detalhes)):
            if detalhes[i].tipo == "Filme":
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")

    elif opcao == '2':
        for i in range(len(detalhes)):
            if detalhes[i].tipo == "Série":
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
            
    elif opcao == '3':
        for i in range(len(detalhes)):
            if detalhes[i].tipo == "Documentário":
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")

    elif opcao == '4':
        for i in range(len(detalhes)):
            if detalhes[i].disponivel == "Disponível":
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
            
    elif opcao == '5':
        for i in range(len(detalhes)):
            if detalhes[i].disponivel == "Indisponível":
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
    
    print("\nA consulta foi concluída")
    iniciar()

#relatório de compras
def relatorio_compras():

    print(login, data)
    print("\nCódigo  Nome  Preço  Tipo")
    for i in range(len(codigo_comprado)):
        print(f"{codigo_comprado[i]}, {nome_comprado[i]}, R${preco_comprado[i]}, {tipo_comprado[i]}")
    time()
    iniciar()

#data e hora:
def time():
    global data
    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y %H:%M:%S")
    print(data)

#inicia o programa:
def iniciar():

    #mensagem inicial e encaminhamento de funções 

    print("\n1 - Cadastrar\n2 - Consultar\n3 - Atualizar\n4 - Registrar Compra\n5 - Relatório de produtos\n6 - Relatório de compras")
    method = input("\nDigite sua ação: ")
    while method != '1' and method != '2' and method != '3' and method != '4' and method != '5' and method != '6':
        method = input("\nMétodo inválido, digite sua ação novamente: ")

    if method == "1":
        cadastro()
    elif method == "2":
        verificacao()
    elif method == "3":
        atualizar()
    elif method == "4":
        registrar_compra()
    elif method == "5":
        relatorio_produtos()
    elif method == "6":
        relatorio_compras()

iniciar()

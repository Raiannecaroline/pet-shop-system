# Oi fofs, uma explicação breve sobre o sistema, bebi altas cervejas para fazer ele

# O sistema do pet shop basea-se na venda de produtos para animais de estimação.
# O sistema deve permitir o cadastro de produtos e clientes, além de permitir a venda de produtos.
# O sistema vai pegar os dados de um json, guardar dados e listar estes dados pelo terminal.
# O sistema vai pegar os dados Json e manipular os dados, como adicionar, remover, atualizar e pesquisar.

import json
import os

# Dicionário de produtos
produtos = {}

# Lista de clientes
clientes = []

# Lista para armazenar os pedidos
pedidos = []


# Funções da parte dos produtos
def adicionarProdutos(nome, quantidade, preco):
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    produtos[nome] = produto
    salvarDadosJson()


def removerProdutos(nome):
    produtos.pop(nome)
    salvarDadosJson()


def atualizarProdutos(nome, quantidade):
    produtos[nome]["quantidade"] = quantidade
    salvarDadosJson()


def pesquisarProdutos(nome):
    return produtos.get(nome)


# Funções da parte dos clientes
def adicionarClientes(nome, cpf, email, telefone):
    cliente = {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone}
    clientes.append(cliente)
    salvarDadosJson()


def removerClientes(nome):
    for cliente in clientes:
        if cliente["nome"] == nome:
            clientes.remove(cliente)
            salvarDadosJson()
            break


def atualizarClientes(nome, cpf, email, telefone):
    for cliente in clientes:
        if cliente["nome"] == nome:
            cliente["cpf"] = cpf
            cliente["email"] = email
            cliente["telefone"] = telefone
            salvarDadosJson()
            break


def pesquisarClientes(nome):
    for cliente in clientes:
        if cliente["nome"] == nome:
            return cliente


# Funções da parte dos pedidos
def adicionarPedidos(idPedido, cliente, produto, quantidade):
    pedido = {
        "id": idPedido,
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade,
    }
    pedidos.append(pedido)
    salvarDadosJson()
    infoProdutos = pesquisarProdutos(produto)
    if infoProdutos:
        valorPedidos = infoProdutos["preco"] * quantidade
        valorTotalPedido += valorPedidos
    return valorTotalPedido


def removerPedido(idPedido):
    for pedido in pedidos:
        if pedido["id"] == idPedido:
            infoProdutos = pesquisarProdutos(pedido["produto"])
            if infoProdutos:
                valorPedidos = infoProdutos["preco"] * pedido["quantidade"]
                valorTotalPedido -= valorPedidos
            pedidos.remove(pedido)
            salvarDadosJson()
        return valorTotalPedido


def atualizarPedido(idPedido, cliente, produto, quantidade):
    for pedido in pedidos:
        if pedido["id"] == idPedido:
            infoProdutos = pesquisarProdutos(produto)
            if infoProdutos:
                valorPedidosAntigos = infoProdutos["preco"] * pedido["quantidade"]
                valorProdutosNovos = infoProdutos["preco"] * quantidade
                valorTotalPedido += valorProdutosNovos - valorPedidosAntigos
                if pedido["id"] == idPedido:
                    pedido["cliente"] = cliente
                    pedido["produto"] = produto
                    pedido["quantidade"] = quantidade
                    salvarDadosJson()
                    return valorTotalPedido
    return valorTotalPedido


def pesquisarPedido(idPedido):
    for pedido in pedidos:
        if pedido["id"] == idPedido:
            return pedido

 # Função para calcular o valor total dos pedidos       
def calcularValorTotalPedido(pedidos):
    total = 0
    for pedido in pedidos:
        infoProdutos = pesquisarProdutos(pedido["produto"])
        if infoProdutos:
            total += infoProdutos["preco"] * pedido["quantidade"]
    return total                


# Função para carregar os dados de um arquivo json
def carregarDadoJson():
    if os.path.exists("produtos.json"):
        with open("produtos.json", "r") as file:
            produto_json = json.load(file)
        produtos.clear()
        for produto in produto_json["produtos"]:
            produtos[produto["nome"]] = produto

    if os.path.exists("clientes.json"):
        with open("clientes.json", "r") as file:
            cliente_json = json.load(file)
        clientes.clear()
        clientes.extend(cliente_json["clientes"])

    if os.path.exists("pedidos.json"):
        with open("pedidos.json", "r") as file:
            pedido_json = json.load(file)
        pedidos.clear()
        pedidos.extend(pedido_json["pedidos"])


# Função para salvar os dados em um arquivo json
def salvarDadosJson():
    produto_json = {"produtos": list(produtos.values())}
    with open("produtos.json", "w") as file:
        json.dump(produto_json, file)

    cliente_json = {"clientes": clientes}
    with open("clientes.json", "w") as file:
        json.dump(cliente_json, file)

    pedido_json = {"pedidos": pedidos}
    with open("pedidos.json", "w") as file:
        json.dump(pedido_json, file)


# Função para mostrar o menu
def menu():
    valorTotalPedido = 0.0
    while True:
        print("*** Bem vindo ao Pet Shop ***")
        print("1 - Listar os Produtos")
        print("2 - Pesquisar Produto")
        print("3 - Listar Clientes")
        print("4 - Pesquisar Cliente")
        print("5 - Listar Pedidos")
        print("6 - Calcular Pedido")
        print("7 - Adicionar Produto")
        print("8 - Atualizar Produto")
        print("9 - Adicionar Cliente")
        print("10 - Atualizar Cliente")
        print("11 - Adicionar Pedido")
        print("12 - Atualizar Pedido")
        print("13 - Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            for produto in produtos.values():
                print(produto)

        elif opcao == 2:
            pesquisarProdutos()

        elif opcao == 3:
            for cliente in clientes:
                print(cliente)

        elif opcao == 4:
            pesquisarClientes()

        elif opcao == 5:
            for pedido in pedidos:
                print(pedido)

        elif opcao == 6:
            print("O valor total dos pedidos é {:.2f}".format(calcularValorTotalPedido(pedidos)))

        elif opcao == 7:
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            preco = float(input("Digite o preço do produto: "))
            adicionarProdutos(nome, quantidade, preco)
            print("Produto adicionado com sucesso")

        elif opcao == 8:
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            atualizarProdutos(nome, quantidade)
            print("Produto atualizado com sucesso")

        elif opcao == 9:
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o cpf do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionarClientes(nome, cpf, email, telefone)
            print("Cliente adicionado com sucesso")

        elif opcao == 10:
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o cpf do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            atualizarClientes(nome, cpf, email, telefone)
            print("Cliente atualizado com sucesso")

        elif opcao == 11:
            idPedido = int(input("Digite o id do pedido: "))
            cliente = input("Digite o nome do cliente: ")
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            adicionarPedidos(idPedido, cliente, produto, quantidade)
            print("Pedido adicionado com sucesso")

        elif opcao == 12:
            idPedido = int(input("Digite o id do pedido: "))
            cliente = input("Digite o nome do cliente: ")
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            atualizarPedido(idPedido, cliente, produto, quantidade)
            print("Pedido atualizado com sucesso")

        elif opcao == 13:
            salvarDadosJson()
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    carregarDadoJson()
    menu()

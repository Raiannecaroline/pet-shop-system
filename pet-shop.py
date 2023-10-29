# O sistema do pet shop basea-se na venda de produtos para animais de estimação.
# O sistema deve permitir o cadastro de produtos e clientes, além de permitir a venda de produtos.
# O sistema vai pegar os dados de um json, guardar dados e listar estes dados pelo terminal.

import json
import os

# Dicionário de produtos
produtos = {}

# Lista de clientes
clientes = []

# Lista para armazenar os pedidos
pedidos = []

valorTotalPedido = 0.0


# Funções da parte dos produtos
def adicionarProdutos(nome, quantidade, preco):
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    produtos[nome] = produto
    adicionarProdutoAoJSON(produto)


def removerProdutos(nome):
    produtos.pop(nome)
    atualizarProdutoNoJSON()


def atualizarProdutos(nome, quantidade):
    produtos[nome]["quantidade"] = quantidade
    atualizarProdutoNoJSON()


def pesquisarProdutos(nome):
    return produtos.get(nome)


def adicionarProdutoAoJSON(produtos):
    produto_json = {"produtos": list(produtos.values())}
    with open("produtos.json", "w") as file:
        json.dump(produto_json, file)


def atualizarProdutoNoJSON():
    adicionarProdutoAoJSON()


# Funções da parte dos clientes
def adicionarClientes(nome, cpf, email, telefone):
    cliente = {"nome": nome, "cpf": cpf, "email": email, "telefone": telefone}
    clientes.append(cliente)
    adicionarProdutoAoJSON(cliente)


def removerClientes(nome):
    for cliente in clientes:
        if cliente["nome"] == nome:
            clientes.remove(cliente)
            atualizarClienteNoJSON()
            break


def atualizarClientes(nome, cpf, email, telefone):
    for cliente in clientes:
        if cliente["nome"] == nome:
            cliente["cpf"] = cpf
            cliente["email"] = email
            cliente["telefone"] = telefone
            atualizarClienteNoJSON()
            break


def pesquisarClientes(nome):
    for cliente in clientes:
        if cliente["nome"] == nome:
            return cliente


def adicionarClienteAoJSON(clientes):
    cliente_json = {"clientes": clientes}
    with open("clientes.json", "w") as file:
        json.dump(cliente_json, file)


def atualizarClienteNoJSON():
    adicionarClienteAoJSON()

# Funções da parte dos pedidos
def adicionarPedidos(idPedido, cliente, produto, quantidade, valorTotalPedido):
    pedido = {
        "id": idPedido,
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade,
    }
    pedidos.append(pedido)
    adicionarProdutoAoJSON(pedido)
    infoProdutos = pesquisarProdutos(produto)
    if infoProdutos:
        valorPedidos = infoProdutos["preco"] * quantidade
        valorTotalPedido += valorPedidos


def removerPedido(idPedido, valorTotalPedido):
    for pedido in pedidos:
        if pedido["id"] == idPedido:
            infoProdutos = pesquisarProdutos(pedido["produto"])
            if infoProdutos:
                valorPedidos = infoProdutos["preco"] * pedido["quantidade"]
                valorTotalPedido -= valorPedidos
            pedidos.remove(pedido)
            break


def atualizarPedido(idPedido, cliente, produto, quantidade, valorTotalPedido):
    for pedido in pedidos:
        if pedido["id"] == idPedido:
            infoProdutos = pesquisarProdutos(pedido["produto"])
            if infoProdutos:
                valorPedidosAntigos = infoProdutos["preco"] * pedido["quantidade"]
                valorProdutosNovos = infoProdutos["preco"] * quantidade
                valorTotalPedido += valorProdutosNovos - valorPedidosAntigos
                if pedido["id"] == idPedido:
                    pedido["cliente"] = cliente
                    pedido["produto"] = produto
                    pedido["quantidade"] = quantidade
                    break


def pesquisarPedido(idPedido):
    for pedido in pedidos:
        if pedido["id"] == idPedido:
            return pedido


def adicionarPedidoAoJSON(pedidos):
    pedido_json = {"pedidos": pedidos}
    with open("pedidos.json", "w") as file:
        json.dump(pedido_json, file)


def atualizarPedidoNoJSON():
    pedido_json = {"pedidos": pedidos}
    with open("pedidos.json", "w") as file:
        json.dump(pedido_json, file)


# Função para carregar os dados de um arquivo json
def carregarDadoJson():
    with open("produtos.json", "r") as file:
        produto_json = json.load(file)

        for produto in produto_json["produtos"]:
          adicionarProdutos(produto["nome"], produto["quantidade"], produto["preco"])

    with open("clientes.json", "r") as file:
        cliente_json = json.load(file)

        for cliente in cliente_json["clientes"]:
            adicionarClientes(
                cliente["nome"], cliente["cpf"], cliente["email"], cliente["telefone"]
            )

    with open("pedidos.json", "r") as file:
        pedido_json = json.load(file)

        for pedido in pedido_json["pedidos"]:
            adicionarPedidos(
                pedido["id"],
                pedido["cliente"],
                pedido["produto"],
                pedido["quantidade"],
                valorTotalPedido,
            )


# Função para pesquisar produtos e clientes
def pesquisarProduto():
    nomeProduto = input("Digite o nome do produto desejado: ")
    produto = pesquisarProdutos(nomeProduto)
    if produto:
        print(produto)
    else:
        print("Produto não encontrado")


def pesquisarCliente():
    nomeCliente = input("Digite o nome do cliente desejado: ")
    cliente = pesquisarClientes(nomeCliente)
    if cliente:
        print(cliente)
    else:
        print("Cliente não encontrado")


# Função para salvar os dados em um arquivo json
def salvarDadosJson():
    produto_json = {"produtos": list(produtos.values())}
    with open("produtos.json", "w") as file:
        json.dump(produto_json, file)
        adicionarClienteAoJSON(produto_json)

    cliente_json = {"clientes": clientes}
    with open("clientes.json", "w") as file:
        json.dump(cliente_json, file)
        adicionarClienteAoJSON(cliente_json)

    pedido_json = {"pedidos": pedidos}
    with open("pedidos.json", "w") as file:
        json.dump(pedido_json, file)
        adicionarClienteAoJSON(pedido_json)


# Função para mostrar o menu
def menu():
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
            pesquisarProduto()

        elif opcao == 3:
            for cliente in clientes:
                print(cliente)

        elif opcao == 4:
            pesquisarCliente()

        elif opcao == 5:
            for pedido in pedidos:
                print(pedido)

        elif opcao == 6:
            print("O valor total dos pedidos é {:.2f}: ".format(valorTotalPedido))

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
            adicionarPedidos(idPedido, cliente, produto, quantidade, valorTotalPedido)
            print("Pedido adicionado com sucesso")      

        elif opcao == 12:
            idPedido = int(input("Digite o id do pedido: "))
            cliente = input("Digite o nome do cliente: ")
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            atualizarPedido(idPedido, cliente, produto, quantidade, valorTotalPedido)
            print("Pedido atualizado com sucesso")      

        elif opcao == 13:
            salvarDadosJson()
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    carregarDadoJson()
    menu()

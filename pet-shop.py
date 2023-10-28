# O sistema do pet shop basea-se na venda de produtos para animais de estimação.
# O sistema deve permitir o cadastro de produtos e clientes, além de permitir a venda de produtos.
# O sistema vai pegar os dados de um json, guardar dados e listar estes dados pelo terminal.

import json

# Dicionário de produtos
produtos = {}

# Lista de clientes
clientes = []

# Lista para armazenar os pedidos
pedidos = []

# Funções da parte dos produtos
def adicionarProdutos(nome, quantidade, preço):
  produto = {
    "nome": nome,
    "quantidade": quantidade,
    "preço": preço
  }
  produtos[nome] = produto

def removerProdutos(nome):
  produtos.pop(nome)

def atualizarProdutos(nome, quantidade):
  produtos[nome]["quantidade"] = quantidade

def pesquisarProdutos(nome):
  return produtos[nome]

# Funções da parte dos clientes
def adicionarClientes(nome, cpf, email, telefone):
  cliente = {
    "nome": nome,
    "cpf": cpf,
    "email": email,
    "telefone": telefone
  }
  clientes[nome] = cliente

def removerClientes(nome):
  for cliente in clientes:
    if cliente["nome"] == nome:
      clientes.remove(cliente)
      break

def atualizarClientes(nome, cpf, email, telefone):
  for cliente in clientes:
    if cliente["nome"] == nome:
      cliente["cpf"] = cpf
      cliente["email"] = email
      cliente["telefone"] = telefone
      break

def pesquisarClientes(nome):
  for cliente in clientes:
    if cliente["nome"] == nome:
      return cliente

# Funções da parte dos pedidos
def adicionarPedidos(cliente, produto, quantidade):
  pedido = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": quantidade
  }
  pedidos.append(pedido)

def removerPedido(idPedido):
  for pedido in pedidos:
    if pedido["id"] == idPedido:
      pedidos.remove(pedido)
      break

def atualizarPedido(idPedido, cliente, produto, quantidade):
  for pedido in pedidos:
    if pedido["id"] == idPedido:
      pedido["cliente"] = cliente
      pedido["produto"] = produto
      pedido["quantidade"] = quantidade
      break

def pesquisarPedido(idPedido):
  for pedido in pedidos:
    if pedido["id"] == idPedido:
      return pedido

# Função para carregar os dados de um arquivo json
def carregarDadoJson():
  with open("produtos.json", "r") as arquivo:
    produto_json = json.load(arquivo)

  for produto in produto_json["produtos"]:
    adicionarProdutos(produto["nome"], produto["quantidade"], produto["preço"])

  with open("clientes.json", "r") as arquivo:
    cliente_json = json.load(arquivo)

  for cliente in cliente_json["clientes"]:
    adicionarClientes(cliente["nome"], cliente["cpf"], cliente["email"], cliente["telefone"])

  with open("pedidos.json", "r") as arquivo:
    pedido_json = json.load(arquivo)

  for pedido in pedido_json["pedidos"]:
    adicionarPedidos(pedido["idPedido"], pedido["cliente"], pedido["produto"], pedido["quantidade"])

# Função para salvar os dados em um arquivo json


class Database:
    def __init__(self):
        self.pedidos = []

    def salvar_pedido(self, pedido):
        self.pedidos.append(pedido)
        print("Pedido salvo no banco (simulação).")
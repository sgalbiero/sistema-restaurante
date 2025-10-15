from models.pedido_model import Pedido
from database.connection import Database

class PedidoService:
    def __init__(self):
        self.db = Database()

    def criar_pedido(self, mesa, itens):
        pedido = Pedido(mesa, itens)
        self.db.salvar_pedido(pedido)
        return pedido
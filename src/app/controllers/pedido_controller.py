from services.pedido_service import PedidoService

class PedidoController:
    def __init__(self):
        self.service = PedidoService()

    def criar_pedido(self, mesa, itens):
        pedido = self.service.criar_pedido(mesa, itens)
        print(f"Pedido criado com sucesso: {pedido}")
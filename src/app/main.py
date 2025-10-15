from controllers.pedido_controller import PedidoController

if __name__ == "__main__":
    controller = PedidoController()
    controller.criar_pedido("Mesa 3", ["Pizza", "Refrigerante"])
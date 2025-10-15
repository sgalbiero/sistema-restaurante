class Pedido:
    def __init__(self, mesa, itens):
        self.mesa = mesa
        self.itens = itens

    def __repr__(self):
        return f"<Pedido mesa={self.mesa}, itens={self.itens}>"
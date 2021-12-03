class CommandInterface:

    def run(self, increase, horizontal, vertical, aim):
        pass


class FactoryInterface:

    def create_forward(self):
        pass

    def create_down(self):
        pass

    def create_up(self):
        pass

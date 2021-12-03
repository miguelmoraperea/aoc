from interfaces import CommandInterface, FactoryInterface


class Forward(CommandInterface):

    def run(self, increase, horizontal, vertical, aim):
        return horizontal + increase, vertical, aim


class Down(CommandInterface):

    def run(self, increase, horizontal, vertical, aim):
        return horizontal, vertical + increase, aim


class Up(CommandInterface):

    def run(self, increase, horizontal, vertical, aim):
        return horizontal, vertical - increase, aim


class FactoryPart1(FactoryInterface):

    def create_forward(self):
        return Forward()

    def create_down(self):
        return Down()

    def create_up(self):
        return Up()

from commands_1 import CommandInterface, FactoryInterface


class Forward(CommandInterface):

    def run(self, increase, horizontal, vertical, aim):
        return horizontal + increase, vertical + (aim * increase), aim


class Down(CommandInterface):

    def run(self, increase, horizontal, vertical, aim):
        return horizontal, vertical, aim + increase


class Up(CommandInterface):

    def run(self, increase, horizontal, vertical, aim):
        return horizontal, vertical, aim - increase


class FactoryPart2(FactoryInterface):

    def create_forward(self):
        return Forward()

    def create_down(self):
        return Down()

    def create_up(self):
        return Up()

class Submarine:

    def __init__(self, factory):
        self._factory = factory
        self._horizontal_pos = 0
        self._vertical_pos = 0
        self._aim = 0

    def get_end_position(self, course):
        actions = self._create_cmds_from_course(course)

        xpos = self._horizontal_pos
        ypos = self._vertical_pos
        aim = self._aim

        for action in actions:
            cmd = action[0]
            increase = action[1]
            xpos, ypos, aim = cmd.run(increase, xpos, ypos, aim)

        return xpos * ypos

    def _create_cmds_from_course(self, course):
        lines = course.splitlines()
        res = []
        for line in lines:
            splitted = line.split()
            cmd_str = splitted[0]
            increase = splitted[1]
            res.append([self._create_cmd(cmd_str), int(increase)])
        return res

    def _create_cmd(self, name):
        if name == 'forward':
            return self._factory.create_forward()
        if name == 'down':
            return self._factory.create_down()
        if name == 'up':
            return self._factory.create_up()

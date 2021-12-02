class Sonar:

    def __init__(self, measurements):
        self._data = measurements

    def get_increase_count(self):

        if not self._data:
            return 0

        prev = self._data[0]
        n = len(self._data)
        res = 0

        for idx in range(1, n):
            current = self._data[idx]

            if current > prev:
                res += 1

            prev = current

        return res

    def get_three_measurement_increase_count(self):
        n = len(self._data)

        if n < 3:
            return 0

        prev = sum(self._data[0:3])
        res = 0

        for i in range(1, n - 2):

            start = i
            end = i + 3

            current = sum(self._data[start:end])

            if current > prev:
                res += 1

            prev = current

        return res

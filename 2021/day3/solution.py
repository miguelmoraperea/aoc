from copy import deepcopy


class Submarine:

    def __init__(self, data):
        self._data = data
        self._num_of_readings = len(self._data)
        self._len_of_reading = len(self._data[0])

    def get_power_consuption(self):
        gamma_rate_str = ""

        for col in range(self._len_of_reading):
            cnt_0 = 0
            cnt_1 = 0
            for row in range(self._num_of_readings):
                if self._data[row][col] == "0":
                    cnt_0 += 1
                else:
                    cnt_1 += 1
            gamma_rate_str += "0" if cnt_0 > cnt_1 else "1"

        gamma_rate = int(gamma_rate_str, base=2)
        epsilon_rate_str = ''.join('1' if i == '0' else '0'
                                   for i in gamma_rate_str)
        epsilon_rate = int(epsilon_rate_str, base=2)
        return gamma_rate * epsilon_rate

    def get_life_support_rating(self):
        oxygen_generator = self._filter_data(True)
        co2_scrubber = self._filter_data(False)
        return oxygen_generator * co2_scrubber

    def _filter_data(self, on_1):
        numbers = deepcopy(self._data)

        for col in range(self._len_of_reading):

            cnt_0 = 0
            cnt_1 = 0
            row = 0

            # Find most popular bit 0/1 for bit in col
            while row < len(numbers):
                if numbers[row][col] == "0":
                    cnt_0 += 1
                else:
                    cnt_1 += 1
                row += 1

            if on_1:
                keep = "0" if cnt_0 <= cnt_1 else "1"
            else:
                keep = "0" if cnt_0 > cnt_1 else "1"

            # Get only values that contain "keep" in the column number
            numbers = [number for number in numbers if number[col] == keep]

            if len(numbers) == 1:
                break

        return int(numbers[0], base=2)

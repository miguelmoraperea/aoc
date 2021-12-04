class Submarine:

    def get_power_consuption(self, data):
        num_of_readings = len(data)
        len_of_reading = len(data[0])

        gamma_rate_str = ""

        for col in range(len_of_reading):
            cnt_0 = 0
            cnt_1 = 0
            for row in range(num_of_readings):
                if data[row][col] == "0":
                    cnt_0 += 1
                else:
                    cnt_1 += 1
            gamma_rate_str += "0" if cnt_0 > cnt_1 else "1"

        gamma_rate = int(gamma_rate_str, base=2)
        epsilon_rate_str = ''.join('1' if i == '0' else '0'
                                   for i in gamma_rate_str)
        epsilon_rate = int(epsilon_rate_str, base=2)
        return gamma_rate * epsilon_rate

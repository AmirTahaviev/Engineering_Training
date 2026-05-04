import smbus
import time
import matplotlib.pyplot as plt


class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_i2c_block_data(self.address, 0x00, 2)
        upper_data_byte = data[0]
        lower_data_byte = data[1]
        number = (upper_data_byte << 2) | ((lower_data_byte & 0xC0) >> 6)

        if self.verbose:
            print(f"Число: {number}")

        return number

    def get_voltage(self):
        code = self.get_number()
        max_code = 2 ** 10 - 1
        voltage = self.dynamic_range * code / max_code
        return voltage


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage, 'b-', linewidth=2)

    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')

    plt.xlim(0, max(time))
    plt.ylim(0, max_voltage)

    plt.grid(True, alpha=0.3)
    plt.show()


def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        period = time[i] - time[i - 1]
        sampling_periods.append(period)

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Распределение периодов дискретизации')
    plt.xlabel('Период измерения, с')
    plt.ylabel('Количество измерений')
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    try:
        adc = MCP3021(dynamic_range=5.0, verbose=False)

        time_data = []
        voltage_data = []

        print("Начинаю сбор данных. Изменяйте напряжение на входе АЦП во всем диапазоне от 0 до 5В")
        print("Для остановки нажмите Ctrl+C")

        start_time = time.time()

        while True:
            voltage = adc.get_voltage()
            current_time = time.time() - start_time

            time_data.append(current_time)
            voltage_data.append(voltage)

            print(f"Время: {current_time:.2f} с, Напряжение: {voltage:.3f} В")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print(f"\nСобрано {len(time_data)} измерений")

        if len(time_data) > 1:
            max_voltage = max(voltage_data)
            min_voltage = min(voltage_data)
            print(f"Максимальное напряжение: {max_voltage:.3f} В")
            print(f"Минимальное напряжение: {min_voltage:.3f} В")
            print(f"Диапазон: {min_voltage:.3f} - {max_voltage:.3f} В")

            plot_voltage_vs_time(time_data, voltage_data, 5.0)
            plot_sampling_period_hist(time_data)
        else:
            print("Недостаточно данных для построения графиков")

    finally:
        adc.deinit()
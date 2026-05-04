import smbus
import time


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
            print(f"Старший байт: 0x{upper_data_byte:02x}, Младший байт: 0x{lower_data_byte:02x}, Число: {number}")

        return number

    def get_voltage(self):
        code = self.get_number()
        max_code = 2 ** 10 - 1
        voltage = self.dynamic_range * code / max_code
        return voltage


if __name__ == "__main__":
    try:
        adc = MCP3021(dynamic_range=5.0, verbose=True)

        while True:
            voltage = adc.get_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(1.0)

    except KeyboardInterrupt:
        pass
    finally:
        adc.deinit()
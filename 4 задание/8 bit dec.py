import RPi.GPIO as GPI0
import time

GPI0.setmode(GPI0.BCM)

dac_bits = [16,20, 21, 25, 26, 17, 27, 22]

num = 0

GPI0.setup(dac_bits, GPI0.OUT)
GPI0.output(dac_bits, 0)


dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП(0,00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)
    
def dec2bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

try:
    while True:
        try:
            voltage = float(input('Введите напряжение в Вольтах:'))
            num = voltage_to_number(voltage)
            GPI0.output(dac_bits, dec2bin(num))
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPI0.output(dac_bits, 0)
    GPI0.cleanup()
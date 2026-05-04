if __name__ == "__main__":

    adc = R2R_ADC(dynamic_range=3.3, compare_time=0.0001)

    voltage_values = []
    time_values = []
    duration = 3.0

    try:
        start_time = time.time()

        while time.time() - start_time < duration:
            voltage = adc.get_sc_voltage()
            voltage_values.append(voltage)
            time_values.append(time.time() - start_time)
            print(f"Время: {time_values[-1]:.3f}s, Напряжение: {voltage:.3f}V")
            time.sleep(0.01)

        print(f"\nВсего измерений: {len(voltage_values)}")

        if len(voltage_values) > 0:
            print("Строим графики...")
            plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
            plot_sampling_period_hist(time_values)
            print("Графики построены")
        else:
            print("Нет данных для построения")

        input("Нажмите Enter для выхода...")

    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback

        traceback.print_exc()

    finally:
        del adc
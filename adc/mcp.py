import time
import sys
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

if __name__ == "__main__":
    print("=" * 50)
    print("ВЫБОР ДАТЧИКА")
    print("1 - Терморезистор (прижмите палец в середине записи)")
    print("2 - Фоторезистор (посветите фонариком в середине записи)")
    choice = input("Введите 1 или 2: ").strip()

    if choice not in ("1", "2"):
        print("❌ Неверный выбор. Завершение.")
        sys.exit(1)

    # Для лабораторного эксперимента 3 сек слишком мало.
    # Установлено 10 сек, чтобы успеть выполнить действие.
    duration = 10.0
    sleep_interval = 0.01  # 10 мс. 1 мс часто вызывает таймауты I2C

    print(f"\n🔌 Инициализация MCP3021...")
    try:
        adc = MCP3021(dynamic_range=3.183, verbose=False)
    except Exception as e:
        print(f"❌ Ошибка подключения к АЦП: {e}")
        print("💡 Проверьте: sudo i2cdetect -y 1, права root, pull-up резисторы")
        sys.exit(1)

    voltage_values = []
    time_values = []
    errors = 0

    print(f"⏱️  Начало записи на {duration} секунд...")
    print("   Выполняйте действия с датчиком прямо сейчас!\n")

    try:
        start_time = time.time()
        while time.time() - start_time < duration:
            try:
                voltage = adc.get_voltage()
                if voltage is not None:
                    voltage_values.append(voltage)
                    time_values.append(time.time() - start_time)
                else:
                    errors += 1
            except Exception as e:
                errors += 1

            time.sleep(sleep_interval)

    except KeyboardInterrupt:
        print("\n⏹️ Запись прервана пользователем")
    finally:
        elapsed = time.time() - start_time
        print(f"\n✅ Запись завершена ({elapsed:.2f} сек)")
        print(f"📊 Успешных измерений: {len(voltage_values)}")
        if errors > 0:
            print(f"⚠️ Пропущено ошибок шины: {errors}")

        # Построение графиков
        if len(voltage_values) > 1:
            plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
            plot_sampling_period_hist(time_values)
        else:
            print("❌ Недостаточно данных для графиков. Проверьте подключение I2C.")

        adc.deinit()
        print("🔌 АЦП отключён.")
import matplotlib.pyplot as plt

def plot_voltage_vs_time(time_vals, voltage, max_voltage):
    if len(time_vals) == 0:
        print("⚠️ Нет данных для построения графика напряжения")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(time_vals, voltage, 'b-', linewidth=2)

    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')

    plt.xlim(0, max(time_vals))
    plt.ylim(0, max_voltage)

    plt.grid(True, alpha=0.3)
    plt.show()

def plot_sampling_period_hist(time_vals):
    if len(time_vals) < 2:
        print("⚠️ Недостаточно данных для гистограммы периодов")
        return

    sampling_periods = [time_vals[i] - time_vals[i-1] for i in range(1, len(time_vals))]

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Распределение периодов дискретизации')
    plt.xlabel('Период измерения, с')
    plt.ylabel('Количество измерений')
    plt.xlim(0, 0.06)
    plt.grid(True, alpha=0.3)

    plt.show()
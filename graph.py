import matplotlib.pyplot as plt

def show_graphs(sim):

    plt.figure()

    plt.plot(sim.time_data, sim.speed_data)

    plt.title("Kecepatan vs Waktu")
    plt.xlabel("Waktu (s)")
    plt.ylabel("Kecepatan (km/h)")
    plt.grid()

    plt.figure()

    plt.plot(sim.time_data, sim.position_data)

    plt.title("Posisi vs Waktu")
    plt.xlabel("Waktu (s)")
    plt.ylabel("Posisi (m)")
    plt.grid()

    plt.show()
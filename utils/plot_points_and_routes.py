import matplotlib.pyplot as plt

# Separar coordenadas en listas X y Y
def plot_points_and_routes(points, secuence):

    ordenated_secuense = [points[i] for i in secuence]

    x_vals = [p[0] for p in ordenated_secuense]
    y_vals = [p[1] for p in ordenated_secuense]

    
    # Crear la figura y ejes
    fig, ax = plt.subplots()

    # Dibujar los points
    ax.plot(x_vals, y_vals, 'bo', label='Clientes')  # 'bo' = blue circles
    ax.plot([x_vals[0]], [y_vals[0]], 'ro', label='Deposito')  # 'bo' = blue circles

    ax.plot(x_vals, y_vals, 'r-', label='Ruta secuencial')
    
    # Dibujar ejes X e Y
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # Cuadrícula y etiquetas
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title("Plano Cartesiano con points Unidos")

    # Mostrar leyenda
    ax.legend()

    # Mostrar el gráfico
    plt.show()
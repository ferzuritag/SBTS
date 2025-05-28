import math

def get_distance_matrix(points):
    n = len(points)
    matriz = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        xi, yi = points[i]
        for j in range(n):
            xj, yj = points[j]
            distancia = round(math.hypot(xi - xj, yi - yj))
            matriz[i][j] = distancia
            
    return matriz
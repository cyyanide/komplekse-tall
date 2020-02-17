# Du skal lage et program som løser oppgave oppgave 2 i oblig 1B ved bruk 
# av Python. Her kan du velge selv hvilke parametere programmet skal be brukeren
# om som er nødvendige for å løse oppgaven. Det viktigste er programmet skal 
# tegne løsningene for oppgaven som punkter i det komplekse planet.

import matplotlib.pyplot as plt
from numpy import exp, pi, arctan2

# Oppgave 1a 

def cube_root(z):
    r = abs(z)  # Magnitude of z. -> re^(i*theta)
    a, b = z.real, z.imag  # z in cartesian form. -> a+bi
    theta = arctan2(b, a)  # Find theta.
    roots = [r**(1.0/3.0) * exp(1j*(theta+2*n*pi)/3) 
    for n in range(1, 4)]
    for i in range(len(roots)):
        roots[i] = round(roots[i], 2)

    return roots

points = cube_root(-216)  
print(points)

x_coordinates, y_coordinates = [], []
for i in points:
    x_coordinates.append(i.real), y_coordinates.append(i.imag)

plt.scatter(x_coordinates, y_coordinates), plt.scatter(0, 0, c='red')
plt.title('Oppgave 1a'), plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.grid(), plt.show()




# Oppgave 1b

def complex_roots(a, b, c):
    D = (b**2 - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_1 = round(x_1.real, 2) + round(x_1.imag, 2) * 1j
    x_2 = (-b - D)/(2*a)
    x_2 = round(x_2.real, 2) + round(x_2.imag, 2) * 1j
    return(x_1, x_2)


a = 1.0/2.0
b = -(3 + 1j)
c = 4 - 1j

points = complex_roots(a, b, c)
print(points)

x_coordinates, y_coordinates = [], []
for i in points:
    x_coordinates.append(i.real), y_coordinates.append(i.imag)

plt.scatter(x_coordinates, y_coordinates), plt.scatter(0, 0, c='red')
plt.title('Oppgave 1b)'), plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.grid(), plt.show() 




 
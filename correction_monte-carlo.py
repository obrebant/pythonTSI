## Exercice : aire par monte-carlo
import matplotlib.pyplot as plt
from random import uniform

def f(x) :
    return pow(x,2)

def dessine_f(f,xmin,xmax) :
	''' Dessin de la fonction f entre xmin et xmax :'''
	nb_points = 50
	x = [xmin+t*(xmax-xmin)/nb_points for t in range(nb_points+1)]
	y = [f(t) for t in x]
	plt.plot(x,y,'m--', label = 'f')
	plt.legend()

def dessine_zone(xmin,ymin,xmax,ymax):
	''' Dessin du carré :'''
	plt.plot([xmin,xmax,xmax,xmin,xmin],
			[ymin,ymin,ymax,ymax,ymin],
			color='black')

xmin, ymin = 0,0
xmax, ymax = 1,1
dessine_f(f,xmin,xmax)
dessine_zone(xmin,ymin,xmax,ymax)

# algo de Monte-Carlo
N = 100 # nbre de points au hasard

success = 0
for i in range(N):
    x, y = uniform(xmin,xmax), uniform(ymin,ymax)
    if y<=f(x) :
        success += 1
        plt.plot(x,y,'bx')
    else :
        plt.plot(x,y,'r*')

p_success = success/N # proportion des succes
a_zone = (xmax-xmin)*(ymax-ymin) # aire de la zone de tirage

print("Estimation de l'aire : ",p_success*a_zone)

plt.show()

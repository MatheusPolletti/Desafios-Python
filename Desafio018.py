from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo a seu gosto: '))

print('O seno dele é = {0:.2f}\nO coseno dele é = {1:.2f}\nA tangente dele é = {2:.2f}'.format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))

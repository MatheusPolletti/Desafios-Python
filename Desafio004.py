n = input('Digite algo: ')

print('O tipo primitivo dele é: {0}'.format(type(n)))



print('Ele é um número? {0}\nEle é uma letra?{1}\nEle é um ascii?{2}\nEle é um identificador?{3}'
      .format(n.isalnum(), n.isalpha(), n.isascii(), n.isidentifier()))

#print(n.isalpha())
#print(n.isalnum())
#print(n.isascii())
#print(n.isdecimal())
#print(n.isdigit())
#print(n.isidentifier())
#print(n.islower())
#print(n.isprintable())
#print(n.isspace())
#print(n.isupper())
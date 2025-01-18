import string
import numpy as n

senha=''

caracter = string.punctuation + string.ascii_letters + string.digits

for i in n.random.choice(list(caracter),10):
    senha+=i

print( f'  A senha criada foi :  {senha}' )

 
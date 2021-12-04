
from statistics import mode

f = open('inputs/input3.txt', 'r')
data = f.read()
f.close()

binstring = ''.join(data.splitlines())
gamma = ''.join([mode(binstring[i::12]) for i in range(12)])
epsilon = gamma.translate(str.maketrans("10","01"))

print(int(gamma,2)* int(epsilon,2))

from statistics import mode, multimode

f = open('inputs/input3.txt', 'r')
data = f.read()
f.close()

binstring = ''.join(data.splitlines())
gamma = ''.join([mode(binstring[i::12]) for i in range(12)])
epsilon = gamma.translate(str.maketrans("10","01"))

print(int(gamma,2)* int(epsilon,2))

def find_oxygen_rating(arr):
    i = 0
    while len(arr) > 1:
        modal_bit = max(multimode([bit[i] for bit in arr]))
        print(modal_bit)
        arr = [bit for bit in arr if bit[i] == modal_bit]
        print(arr)
        i += 1
    
    return int(''.join(arr), 2)

def find_co2_rating(arr):
    i = 0
    while len(arr) > 1:
        modal_bit = max(multimode([bit[i] for bit in arr]))
        arr = [bit for bit in arr if bit[i] != modal_bit]
        i += 1
    
    return int(''.join(arr), 2)



answer1 = find_oxygen_rating(data.splitlines())
answer2 = find_co2_rating(data.splitlines())

print(answer1 * answer2)




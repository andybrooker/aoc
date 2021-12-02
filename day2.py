from typing import List


f = open('input2.txt', 'r')
content = f.read()
f.close()
directions = content.split()
words = directions[::2]
values = directions[1::2]


class Submarine:
    def __init__(self, instructions: zip(List, List)):
        self.depth = 0
        self.length = 0
        self.aim = 0
        self.instructions = instructions
    
    def calculate_position(self):
        for x, y in self.instructions:
            if x == 'forward':
                self.forward(int(y))
            elif x == 'down':
                self.down(int(y))
            elif x == 'up':
                self.up(int(y))

        return self.depth * self.length
    
    def down(self, value: int):
        self.depth += value
    
    def up(self, value: int):
        self.depth -= value
    
    def forward(self, value: int):
        self.length += value

class WorkingSubmarine(Submarine):
    
    def down(self, value: int):
        self.aim += value
    
    def up(self, value: int):
        self.aim -= value

    def forward(self, value: int):
        self.length += value
        self.depth += (self.aim * value)
    
submarine = Submarine(zip(words, values))
working_submarine = WorkingSubmarine(zip(words, values))

answer1 = submarine.calculate_position()
answer2 = working_submarine.calculate_position()
print(answer1, answer2)
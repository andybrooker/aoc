import csv
import functools
from typing import List

with open('inputs.csv', newline='') as f:
    reader = csv.reader(f)
    input_list = list(reader)

depths = [int(x[0]) for x in input_list[1:]]

def count_number_of_increasing_depths(depths: List[int]):

    times_depths_increased = len([depths[i] for i in range(1, len(depths)) if depths[i] > depths[i-1]])
    return times_depths_increased

def count_number_of_increasing_depths_by_sliding_window(depths: List[int]):

    sliding_windows = [sum(depths[i-1:i+2]) for i in range(1, len(depths)-1)]
    answer = count_number_of_increasing_depths(sliding_windows)
    return answer

part1answer = count_number_of_increasing_depths(depths)
part2answer = count_number_of_increasing_depths_by_sliding_window(depths)

print(part1answer, part2answer)

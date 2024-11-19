from tqdm import tqdm
import time
import random


def count_number(n):
    count = 0
    
    for _ in tqdm(
        range(n),
        desc="Loading",
        ncols=70,
        colour='#009fbd',
    ):
        count += 1
        time.sleep(0.01)
    return count
x = random.randrange(1, 1000)
total_numbers = count_number(x)
print(f'Total numbers generated:{x}')

 

import random
import csv

def generate_random_numbers():
    return random.randint(10000, 100000), random.randint(10000, 100000), random.randint(10000, 100000)

num_iterations = 10000

random_numbers_list = [generate_random_numbers() for _ in range(num_iterations)]

with open('../data/random_numbers_10000_100000.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(random_numbers_list)
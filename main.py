#!/usr/bin/env python
import argparse
import sys
from itertools import product

parser = argparse.ArgumentParser(description="Wordlist Oluşturma")

parser.add_argument("-n", type=int, help="Minimum Karakter Sayısı", required=True)
parser.add_argument("-x", type=int, help="Maksimum Karakter Sayısı", required=True)
parser.add_argument("-i", type=str, help="Karakter Seti", required=True)
parser.add_argument("-w", type=str, help="Dosya İsmi", required=True)


args = parser.parse_args()

min_length = args.n
max_length = args.x
char_set = args.i
filename = args.w


def generate_combinations(char_set, min_length, max_length):
    combinations = []
    for length in range(min_length, max_length + 1):
        for combination in product(char_set, repeat=length):
            combinations.append(''.join(combination))
    return combinations

wordlist = generate_combinations(char_set, min_length, max_length)

with open(f"{filename}.txt", "w") as f:
    f.write("\n".join(wordlist))

print(f"{filename} dosyası başarıyla oluşturuldu!")


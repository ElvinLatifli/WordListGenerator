#!/usr/bin/env python3

import argparse
from itertools import product

def generate_combinations(char_set, min_length, max_length):
    try:
        combination_count = sum(len(char_set) ** length for length in range(min_length, max_length + 1))
        total_characters = combination_count * sum(range(min_length, max_length + 1))

        total_characters *= 1.6
        
        units = ['byte', 'KB', 'MB', 'GB', 'TB', 'PB']
        size = total_characters
        unit_index = 0
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1

        print(f"\033[91mSize of File: {round(size, 2)} {units[unit_index]}\033[91m")

        confirm = input("\033[92mDo you want to continue? (Yes-y/No-n):\033[92m ").lower()

        if confirm == "y":
            tamamlanma_saniye = combination_count / 1_600_000
            dakika, saniye = divmod(tamamlanma_saniye, 60)
            saat, dakika = divmod(dakika, 60)
            gun, saat = divmod(saat, 24)
            yil, gun = divmod(gun, 365)
            ay, gun = divmod(gun, 30)
        
            if yil >= 1:
                print(f"\033[93mRemaining time of completion: {int(yil)} Year\033[93m")
            elif ay >= 1:
                print(f"\033[93mRemaining time of completion: {int(ay)} Month\033[93m")
            elif gun >= 1:
                print(f"\033[93mRemaining time of completion: {int(gun)} Day\033[93m")
            elif saat >= 1:
                print(f"\033[93mRemaining time of completion: {int(saat)} Hour\033[93m")
            elif dakika >= 1:
                print(f"\033[93mRemaining time of completion: {int(dakika)} Minute\033[93m")
            elif saniye >= 1:
                print(f"\033[93mRemaining time of completion: {int(saniye)} Second\033[93m")

            with open(f"{filename}.txt", "w") as f:
                for length in range(min_length, max_length + 1):
                    for combination in product(char_set, repeat=length):
                        f.write(''.join(combination) + '\n')
            print(f"\033[96mCompleted Successfully!\033[96m")
        else:
            print("\033[91mCancelled\033[91m")
    except:
        print("\033[91mCancelled\033[91m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creating Wordlist")
    parser.add_argument("-n", type=int, help="Minimum Number of Characters", required=True)
    parser.add_argument("-x", type=int, help="Maximum Number of Characters", required=True)
    parser.add_argument("-i", type=str, help="Character Set", required=True)
    parser.add_argument("-w", type=str, help="File Name", required=True)
    args = parser.parse_args()

    min_length = args.n
    max_length = args.x
    char_set = args.i
    filename = args.w

    generate_combinations(char_set, min_length, max_length)

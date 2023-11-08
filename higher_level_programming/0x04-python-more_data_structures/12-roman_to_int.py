#!/usr/bin/python3
def roman_to_int(rom_num):
    if rom_num and isinstance(rom_num, str):
        ara_num = 0
        num = 0
        conv = 0
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for val in reversed(rom_num):
            num = rom[val]
            num = num if num >= conv else -num
            ara_num += num
            conv = num
        return (ara_num)
    return 0

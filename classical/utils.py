import math

def hamming_weight(n: int) -> int:
    return bin(n).count("1")

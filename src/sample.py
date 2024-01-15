# 素数判定の関数
import sys


def is_prime(n):
    """
    素数判定を行う
    Args:
        n: 判定する整数
    Returns:
        bool: nが素数ならTrue, 素数でないならFalse
    """
    if n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: python sample.py <number>")
        sys.exit()
    n = int(args[1])
    if is_prime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")

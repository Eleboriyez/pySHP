def main():
    print(*(lambda a, b: [(2 * a - b) // 3, (2 * b - a) // 3] if
    (2 * b - a) % 3 == 0 and (2 * a - b) % 3 == 0 and 2 * a - b >= 0 and 2 * b - a >= 0 else [-1])
    (int(input()), int(input())))


if __name__ == '__main__':
    main()

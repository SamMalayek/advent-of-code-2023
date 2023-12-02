
def main():
    lines = open('day01.txt').read().splitlines()
    resp = 0

    for line in lines:
        i, j = 0, len(line)-1
        first, last = '', ''

        while i < len(line):
            if line[i].isnumeric():
                first = line[i]
                break
            i += 1

        while j >= 0:
            if line[j].isnumeric():
                last = line[j]
                break
            j -= 1

        resp += int(first+last)

    print(resp)


if __name__ == "__main__":
    main()

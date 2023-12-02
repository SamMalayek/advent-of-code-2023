
nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


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
            found = False
            for word, num in nums.items():
                if line[i:i + len(word)] == word:
                    first = nums[word]
                    found = True
                    break
            if found:
                break
            i += 1

        while j >= 0:
            if line[j].isnumeric():
                last = line[j]
                break
            found = False
            for word, num in nums.items():
                if j - len(word) >= 0 and line[j - len(word) + 1:j + 1] == word:
                    last = nums[word]
                    found = True
                    break
            if found:
                break

            j -= 1

        num = int(first+last)
        resp += num

    print(resp)


if __name__ == "__main__":
    main()

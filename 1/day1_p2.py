if __name__ == "__main__":
    with open("input.txt",'r') as f:
        lines = f.readlines()
    zero_count = 0
    val = 50
    for line in lines:
        line = line.strip()
        dir = line[0:1]
        amount = int(line[1:])
        for _ in range(amount):
            if dir == 'R':
                val = (val + 1) % 100
            else: #if not R then L
                val = (val - 1) % 100
            if val == 0:
                zero_count += 1

    print(zero_count)
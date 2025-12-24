




if __name__ == "__main__":
    with open("input.txt",'r') as f:
        lines = f.readlines()
    
    items = lines[0].split(",")

    ranges = []
    for item in items:
        item = item.strip()
        ranges.append(list(map(int,item.split('-'))))

    #print(ranges)

    numbers = []
    for start,end in ranges:
        for i in range(start,end+1):
            numbers.append(i)

    #print(numbers)

    total = 0

    for num in numbers:
        s = str(num)
        for i in range(2,len(s)+1):
            if len(s) % i == 0:
                if s[:len(s)//i]*i == s:
                    print(num)
                    total += num
                    break
    print(total)
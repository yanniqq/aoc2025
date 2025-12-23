



if __name__ == "__main__":
    with open("input.txt",'r') as f:
        lines = f.readlines()
    zero_count = 0
    val = 50
    print("The dial starts by pointing at " + str(val))
    for line in lines:
        line = line.strip()
        if line[0:1] == 'R':
            val = (val + int(line[1:])) % 100
        else: #if not R then L
            val = (val - int(line[1:])) % 100
        print("The dial is rotated " + line +" to point at " + str(val))
        if val == 0:
            zero_count += 1

    print(zero_count)
    
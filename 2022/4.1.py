# https://adventofcode.com/2022/day/4

# In how many assignment pairs does one range fully contain the other?

sum = 0

with open('4_input.txt') as input_file:
    for uncleanLine in input_file:
        line = uncleanLine.strip()
        #print(line)
        fields = line.split(',')
        left = fields[0].split('-')
        right = fields[1].split('-')
        #print(left, ' ', right)
        a = int(left[0])
        b = int(left[1])
        c = int(right[0])
        d = int(right[1])


        if a >= c and a <= d:
            if b >= c and b <= d:
                sum = sum + 1
        elif c >= a and c <= b:
            if d >= a and d <= b:
                sum = sum + 1 
        

print(sum)  # 579 too low
# https://adventofcode.com/2022/day/4

# In how many assignment pairs does one range fully contain the other?

sum = 0

with open('4_input.txt') as input_file:
    for uncleanLine in input_file:
        line = uncleanLine.strip()
        print(line)
        fields = line.split(',')
        left = fields[0].split('-')
        right = fields[1].split('-')
        print(left, ' ', right)
    #Wertebereiche finden
        #Prüfen ob linke Seite die rechte Seite vollkommen abdeckt
        #Prüfen ob umgekehrt 
def sep(line):
    line = line.split(" ")
    
    
    line = '-'.join(line)
# line+='-'.join(line)
    return line

line = input("go on : ")

returns = sep(line)

print(returns)
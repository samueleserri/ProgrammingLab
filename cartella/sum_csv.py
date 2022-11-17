values = []
my_file=open('shampo.csv', 'r')
for line in my_file:
    elements = line.split(',')
    if elements[0] != 'Date':
        value = elements[1]
        values.append(float(value))
        
def sum_csv(values):
    result = 0;
    for item in values:
        result = result+item

    return result

print(sum_csv(values))
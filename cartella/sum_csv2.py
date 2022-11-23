def sum_csv(nome_file):
    values = []
    total = 0
    my_file=open(nome_file, 'r')

    for line in my_file:
        elements=line.split(',')
        if elements[0]!='Date':
            value=elements[1]
            values.append(float(value))
    my_file.close()

    for item in values:
        total = total + item

    if values == []:
        return None
    else:
        return total
    
    


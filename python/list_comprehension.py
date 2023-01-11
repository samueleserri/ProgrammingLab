def aumenta_di_c(c, vettore):
    return [vettore[i]+c for i in range(len(vettore))]

x = int(input('inserire c: '))
vettore=[1, 3, 4, 5, 6, 7]
print(aumenta_di_c(x, vettore))
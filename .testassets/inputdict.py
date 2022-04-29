def zbroj(x,y):
    xy = {
    'int' : int(input('Unesite broj: ')),
    'float' : float(input('Unesite broj: ')),
}
    x = xy[x]
    y = xy[y]
    return print(x+y)

zbroj('int','int')
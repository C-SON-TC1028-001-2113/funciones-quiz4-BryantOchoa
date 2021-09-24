def tarjeteria(x,y):
    pliego = x*12
    plumon = y*35
    if pliego<plumon:
        return(pliego)
    elif pliego>plumon:
        return(plumon)
def main():
    pliego = int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumon = int(input('Dame la cantidad de plumones: '))
    total = tarjeteria(pliego,plumon)
    print('El número máximo de tarjetas que se pueden hacer es: '+str(total))

if __name__=='__main__':
    main()

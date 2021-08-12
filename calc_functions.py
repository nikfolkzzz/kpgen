import math
from math import floor


# функция должна возвращать словарь со строкой и ценой cost , answer

FEJ_PRICE = 25000
METALL_PRICE = 700
BOLT_PRICE = 70
DENS  = 7850





def circle_fej(arr):
    Dn, FL, EH ,BH,  qty , material = arr
    area = round(Dn*math.pi * (BH+2*FL) * 10**-6,1)
    price = area * FEJ_PRICE
    all_price = price * qty
    mass = round(area * 10 * 2.56*10**-3 ,2)
    description  = f''' 
    тканевый компенсатор из {material}
    по ТУ 2343435       
    DK={Dn+FL}, EH={EH}    
    BH={BH} FL={FL}        
    вес={floor(mass)}          
    '''
    answer = [qty, description, price, all_price ]
    return answer

def circle_fl(arr):
    Dmin, Dmax , thick, qty , material = arr

    PROFILE = f'{(Dmax-Dmin)/2}x{thick}'
    WEIGHT = round(3.14*(Dmax**2 - Dmin**2)/4*thick*DENS * 10**-9,1 )
    PRICE = floor(WEIGHT*METALL_PRICE)
    ALL_PRICE = floor(PRICE*qty)

    description  = f''' 
    фланец газохода - {material}
    размеры {Dmax}/{Dmin}
    профиль {PROFILE}
    масса {WEIGHT}


    '''
    answer = [qty, description, PRICE, ALL_PRICE ]
    return answer

def circle_сfl(arr):
    Dmin, Dmax , thick, qty , material = arr

    PROFILE = f'{(Dmax-Dmin)/2}x{thick}'
    WEIGHT = round(3.14*(Dmax**2 - Dmin**2)/4*thick*DENS * 10**-9,1)
    PRICE = WEIGHT*METALL_PRICE
    ALL_PRICE = PRICE*qty

    description  = f''' 
    Прижимная планка - {material}
    размеры {Dmax}/{Dmin}
    профиль {PROFILE}
    масса {WEIGHT}
    '''
    answer = [qty, description, PRICE, ALL_PRICE ]
    return answer

def circle_bolting(arr):
    qty , bolt_size = arr
    BOLT_PRICE = 70
    ALL_PRICE = BOLT_PRICE*qty
    PRICE= f'{ALL_PRICE}₽'

    description  = f''' 
    Болтовое соединение - {bolt_size}
    '''
    answer = [qty, description, PRICE, ALL_PRICE ]
    return answer
    


  
def circle_def(arr):
    Dmax, Dmin, alfa, L, thick, qty, material = arr 

    A = float((Dmax-Dmin)/2000)

    THICK = float(thick / 1000)
    RADIUS = float(Dmax / 2000)
    L = float(L / 1000)
    ALFA = float((alfa * math.pi) / 180)
    A1 = A * THICK
    A3 = ((L - THICK) / math.cos(ALFA)) * THICK
    V1 = RADIUS - A / 2
    V3 = RADIUS - A - ((L - THICK) / (2 * math.cos(ALFA))) * math.sin(ALFA) - (THICK / 2) * math.cos(ALFA) 

    Vc = (A1 * V1 + A3 * V3) / (A1 + A3) 
    m = round((A1 + A3) * 2 * math.pi * Vc * DENS  , 1 )

    PRICE = f'{METALL_PRICE * m}₽'

    ALL_PRICE = f'{PRICE * qty}₽'

    description  = f'''
    дефлектор - {material}
    Рзмеры Ø{Dmax}/Ø{Dmin}/ ??
    масса {m}кг
    
    '''

    answer = [qty , description , PRICE , ALL_PRICE]

    return answer 



import math
from math import floor


# функция должна возвращать словарь со строкой и ценой cost , answer





def circle_fej(arr):
    Dn, FL, EH ,BH,  qty , material = arr
    area = Dn *EH * BH * qty
    price = area * 2
    all_price = price * qty
    mass = area * 10 
    description  = f''' 
    тканевый компенсатор
    по ТУ 2343435       
    DK={Dn+FL}, EH={EH}    
    BH={BH} FL={FL}        
    вес={mass}          
    '''
    answer = [qty, description, price, all_price ]
    return answer

def circle_fl(arr):
    Dmin, Dmax , thick, qty , material = arr

    PROFILE = f'{Dmax-Dmin/2}x{thick}'
    WEIGHT = 3.14*(Dmax**2 - Dmin**2)/4*thick*7850 * 10**-9
    PRICE = WEIGHT*700
    ALL_PRICE = PRICE*qty

    description  = f''' 
    фланец газохода 
    размеры {Dmax}/{Dmin}
    профиль {PROFILE}
    масса {WEIGHT}
    '''
    answer = [qty, description, PRICE, ALL_PRICE ]
    return answer
    
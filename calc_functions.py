import math
from math import floor


# функция должна возвращать словарь со строкой и ценой cost , answer





def circle_fej(arr):


    Dn, FL, EH ,BH,  qty , material = arr
    area = Dn * 3.14 *(EH + FL)*10**-6
    price = f'{area * 25000} ₽'
    all_price = price * qty
    mass = area * 10 *10**-3


    

    description  = f''' 
тканевый компенсатор
по ТУ 2343435       
DK={Dn+FL}, EH={EH}    
BH={BH} FL={FL}        
вес={mass}          


    
    
    '''





    answer = [qty, description, price, all_price ]





    return answer
    
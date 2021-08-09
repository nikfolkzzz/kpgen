import math
from math import floor


# функция должна возвращать словарь со строкой и ценой cost , answer





def circle_fej(arr):


    Dn, FL, EH ,BH,  qty , material = arr
    area = Dn *EH * BH * qty
    price = area * 2
    all_price = price * qty
    mass = area * 10 


    

    # description  = f''' 
    # тканевый компенсатор
    # по ТУ 2343435       
    # DK={Dn+FL}, EH={EH}    
    # BH={BH} FL={FL}        
    # вес={mass}          
    # '''

    description = f'{Dn}, {FL} ,{BH}  жижа'




    answer = [qty, description, price, all_price ]
    # answer = 'i am from func()'
 




    return answer
    
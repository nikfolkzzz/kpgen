import math
from math import floor


# функция должна возвращать словарь со строкой и ценой cost , answer





def circle_fej(arr, name , mp , bp ,fp ):
    fabric_price = floor(int(fp))
    metall_price = mp
    bolt_price = bp


    diameter, flange, EH = arr
    area = diameter * 3.14 *(EH + flange)*10**-6
    price = area * fabric_price 

    answer = {

        'cost': price,
        'answer': f'''

цена тканевой части за кв м {fabric_price}
name : {name}
площадь компенсатора - {area}
цена  {price}
    '''
    }

    return answer
    
import math
from math import floor


# функция должна возвращать словарь со строкой и ценой cost , answer





def circle_fej(arr):


    diameter, flange, EH = arr
    area = diameter * 3.14 *(EH + flange)*10**-6
    price = area


    answer = {

        'cost': price,
        'answer': f'''

цена тканевой части за кв м 
name : 
площадь компенсатора - {area}
цена  {price}
    '''
    }

    return answer
    
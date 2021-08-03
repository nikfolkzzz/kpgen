import math
from math import floor
from helpers import rect_fej
# функция должна возвращать словарь со строкой и ценой cost , answer



def rect_flange(arr,name): 
    amin, bmin, thick , amax , bmax = arr
    mass = (amax*bmax - amin*bmin)*thick*7850*10**-9
    mass = round(mass,1)
    cost = mass*700*2
    cost =round(int(cost),1)
    answer = f'''
    {name}
    масса одного фланца {mass}
    масса двух фланцев {mass*2}
    цена за два фланца {cost} ₽
    '''   

    answer = {
        'cost':cost,
        'answer':answer,
    }

    return answer


def rect_fej(arr, name): 
    A, B , L , C = arr 
    perimetr = (A+B)*2
    full_len  = L + 2*C
    area = round(perimetr*full_len*10**-6 , 1)
    cost = area * 25000 
    answer = f'''
    тканевый: {name} 
    площадь компенсатора тип 2: {area}
    цена: {cost}
        '''

    answer = {
        'cost':cost,
        'answer':answer,
    }



    return answer


def rect_cflange(arr,name): 
    amin, bmin, thick , amax , bmax = arr
    mass = (amax*bmax - amin*bmin)*thick*7850*10**-9
    cost = mass*700*2
    answer = f'''
    {name}
    масса одной планки {mass}
    масса двух планок {mass*2}
    цена за две планки {cost} ₽
    '''   

    answer = {
        'cost':cost,
        'answer':answer,
    }

    return answer

def bolting_calc(arr,name):
    qty = arr[0]

    cost = qty *70 
    answer =f'''
    количество крепежа: {qty}
    цена крепежа: {cost}
    
    '''

    answer = {
        'cost':cost,
        'answer':answer,
    }

    return answer


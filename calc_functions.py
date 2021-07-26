import math
from math import floor



def calc_circle_area(arr):



    return f'circle area : {3.14*arr[0]**2/2}'

def calc_rectangular_area(arr):
    return f'площадь квадрата = {arr[0]*arr[1]}'




def rect_flange(arr,name): 

    amax,bmax,amin,bmin,thick = arr 

    mass = round((amax*bmax - amin*bmin)*thick*7850*10**-9 ,1 )
    price = 700
    one_flang_price = round(mass * price)
    qty = 2 

    return f'''
    {name}
    масса одной штуки: {mass} кг 
    масса двух {name}: {2*mass}кг 
    цена за штуку {one_flang_price}
    цена за {qty} позиции: {one_flang_price*2}
    профиль : {(amax-amin)/2} x {thick}
    '''


def rect_fej(arr, name): 
    A, B , L , C = arr 
    perimetr = (A+B)*2
    full_len  = L + 2*C
    area = round(perimetr*full_len*10**-6 , 1)
    cost = area * 25000 
    return f'''
    тканевый: {name} 
    площадь компенсатора тип 2: {area}
    цена: {cost}
    '''

def circ_fej(arr,name):
    D, fl_high,L, = arr
    full_length = L + 2*fl_high
    C = math.pi * D 
    area = round(full_length*C*10**-6,1)
    cost = round(area * 25000,1)


    return f'''
    тканевый: {name} 
    площадь компенсатора тип 2: {area}
    цена: {cost}
    '''

def kpheader(arr): 
    name, design  = arr
    return f'''
    предложение по чертежу {name}
    исполнение: {design}
    '''
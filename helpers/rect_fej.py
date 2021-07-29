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

import reportlab
# !/usr/bin/env python
# -*- coding: utf-8 -*-


def rektangle_area(a, b): 
    return a*b 

def circle_area(r): 
    return 3.14*r**2/2 
    
    
    
shapes = [
    {
        'name': 'rektangle'
        'inputs': ['a', 'b'],
        'func': rektangle_area 
    }
    {
        'name': 'circle'
        'inputs': ['r'],
        'func': cirlcle_area 
    }
]


table_header = '''
<tr> 
    <td>поз.</td>
    <td>кол-во</td>
    <td>описание</td>
    <td>цена за шт.</td>
    <td>полная стоимость</td>
</tr> 

'''


class Detail: 
    def __init__(self,dict, func): 
        name = dict[name]
        inputs = dict[inputs]
        calculated_data = func

    def data_returner: 
        return calculated_data






# class_scope = []
# final_class_scope=[]
# html_table_scoup_arr = []


# for item in scope: 
#     class_scope.append(eval(item))

# for item in class_scope: 
#     final_class_scope.append(item())

# for item in final_class_scope:
#     html_table_scoup_arr.append(item.return_data())


# print(html_table_scoup_arr)


# STRING WITH calculated areas 

# html_table_string = ''.join(html_table_scoup_arr)

html_body = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>report test</title>
   <link rel="stylesheet" href="main.css">
</head>
<body>
  <table> 
  <tr>
    <td> поз. </td> 
    <td> кол-во  </td> 
    <td> описание </td> 
    <td> цена за шт </td> 
    <td> полная цена</td> 


   </tr> 
    {}
  </table> 
</body>
</html>
'''.format(html_table_string)

# f = open('report.html','w',encoding='utf-8')
# f.write(html_body)
# f.close()

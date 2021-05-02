import reportlab
# !/usr/bin/env python
# -*- coding: utf-8 -*-




table_header = '''
<tr> 
    <td>поз.</td>
    <td>кол-во</td>
    <td>описание</td>
    <td>цена за шт.</td>
    <td>полная стоимость</td>
</tr> 

'''


class FEJ: 
    name="Тканевый компенсатор"
    mockdata='jojo'
    def __init__ (self): 
        # print('enter the data for FEJ ex: 1488 1588 300: ')
        data = '100 120 300'
        data_arr = data.split(' ')
        self.pos = 1 
        self.qty = 1 
        self.d_min=eval(data_arr[0])
        self.d_max=eval(data_arr[1])
        self.length=eval(data_arr[2])
        self.price = (self.d_max - self.d_min)*self.length*10*-6*25000

    def return_data(self): 
        return """
        <tr> 
            <td>{0} </td> 
            <td>{1} </td> 
            <td>{2} </td> 
            <td>{3} </td> 
            <td>{4} </td> 
        </tr>
        """.format(self.name,self.pos,self.qty, self.price, self.mockdata)



class FL: 
    name='фланец газохода'
    mockdata='jojo'
    pos = 1 
    qty = 2 
    price = 333
    def __init__(self):
        # print('enter the data for FL ex: 1455 4554 5')
        data = '90 100 10'
        data_arr = data.split(' ')
        self.d_min=eval(data_arr[0])
        self.d_max=eval(data_arr[1])
        self.thic=eval(data_arr[2])
        self.mass = 3.14*(self.d_max**2-self.d_min**2)/4*self.thic*7850*10**-9


    def return_data(self): 
        return """
        <tr> 
            <td>{0} </td> 
            <td>{1} </td> 
            <td>{2} </td> 
            <td>{3} </td> 
            <td>{4} </td> 
        </tr>
        """.format(self.name, self.pos,self.qty, self.price, self.mockdata)



scope = ['FEJ','FL']

class_scope = []
final_class_scope=[]
html_table_scoup_arr = []


for item in scope: 
    class_scope.append(eval(item))

for item in class_scope: 
    final_class_scope.append(item())

for item in final_class_scope:
    html_table_scoup_arr.append(item.return_data())


# print(html_table_scoup_arr)
html_table_string = ''.join(html_table_scoup_arr)

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

f = open('report.html','w',encoding='utf-8')
f.write(html_body)
f.close()

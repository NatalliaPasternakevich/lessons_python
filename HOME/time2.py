import time
import os

n_0= ['XXXX',
       'X  X',
       'X  X',
       'X  X',
      'XXXX']
n_1= [' XX ',
      '  X ',
      '  X ',
      '  X ',
      'XXXX']
n_2= ['XXXX',
      '   X',
      'XXXX',
      'X   ',
      'XXXX']
n_3= ['XXXX',
      '   X',
      'XXXX',
      '   X',
      'XXXX']
n_4= ['X  X',
      'X  X',
      'XXXX',
      '   X',
      '   X']
n_5= ['XXXX',
      'X   ',
      'XXXX',
      '   X',
      'XXXX']
n_6= ['XXXX',
      'X   ',
      'XXXX',
      'X  X',
      'XXXX']
n_7= ['XXXX',
      '   X',
      '   X',
      '   X',
      '   X']
n_8= ['XXXX',
      'X  X',
      'XXXX',
      'X  X',
      'XXXX']
n_9= ['XXXX',
      'X  X',
      'XXXX',
      '   X',
      'XXXX']
n_u= ['    ',
      ' X  ',
      '    ',
      ' X  ',
      '    ']

while 1:
    time_now = time.strftime("%H:%M:%S")
    print(time_now)
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    row5 = ''
    for i in time_now:
        if i == '0':
            row1 = row1 + '  ' + n_0[0]
            row2 = row2 + '  ' + n_0[1]
            row3 = row3 + '  ' + n_0[2]
            row4 = row4 + '  ' + n_0[3]
            row5 = row5 + '  ' + n_0[4]
        if i == '1':
            row1 = row1 + '  ' + n_1[0]
            row2 = row2 + '  ' + n_1[1]
            row3 = row3 + '  ' + n_1[2]
            row4 = row4 + '  ' + n_1[3]
            row5 = row5 + '  ' + n_1[4]
        if i == '2':
            row1 = row1 + '  ' + n_2[0]
            row2 = row2 + '  ' + n_2[1]
            row3 = row3 + '  ' + n_2[2]
            row4 = row4 + '  ' + n_2[3]
            row5 = row5 + '  ' + n_2[4]
        if i == '3':
            row1 = row1 + '  ' + n_3[0]
            row2 = row2 + '  ' + n_3[1]
            row3 = row3 + '  ' + n_3[2]
            row4 = row4 + '  ' + n_3[3]
            row5 = row5 + '  ' + n_3[4]
        if i == '4':
            row1 = row1 + '  ' + n_4[0]
            row2 = row2 + '  ' + n_4[1]
            row3 = row3 + '  ' + n_4[2]
            row4 = row4 + '  ' + n_4[3]
            row5 = row5 + '  ' + n_4[4]
        if i == '5':
            row1 = row1 + '  ' + n_5[0]
            row2 = row2 + '  ' + n_5[1]
            row3 = row3 + '  ' + n_5[2]
            row4 = row4 + '  ' + n_5[3]
            row5 = row5 + '  ' + n_5[4]
        if i == '6':
            row1 = row1 + '  ' + n_6[0]
            row2 = row2 + '  ' + n_6[1]
            row3 = row3 + '  ' + n_6[2]
            row4 = row4 + '  ' + n_6[3]
            row5 = row5 + '  ' + n_6[4]
        if i == '7':
            row1 = row1 + '  ' + n_7[0]
            row2 = row2 + '  ' + n_7[1]
            row3 = row3 + '  ' + n_7[2]
            row4 = row4 + '  ' + n_7[3]
            row5 = row5 + '  ' + n_7[4]
        if i == '8':
            row1 = row1 + '  ' + n_8[0]
            row2 = row2 + '  ' + n_8[1]
            row3 = row3 + '  ' + n_8[2]
            row4 = row4 + '  ' + n_8[3]
            row5 = row5 + '  ' + n_8[4]
        if i == '9':
            row1 = row1 + '  ' + n_9[0]
            row2 = row2 + '  ' + n_9[1]
            row3 = row3 + '  ' + n_9[2]
            row4 = row4 + '  ' + n_9[3]
            row5 = row5 + '  ' + n_9[4]
        if i == ':':
            row1 = row1 + '  ' + n_u[0]
            row2 = row2 + '  ' + n_u[1]
            row3 = row3 + '  ' + n_u[2]
            row4 = row4 + '  ' + n_u[3]
            row5 = row5 + '  ' + n_u[4]
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    time.sleep(1)
    os.system('clear')


    n_0 = ['⬜⬜⬜⬜⬜⬜',
       '⬜⬛⬛⬛⬛⬜',
       '⬜⬛⬜⬜⬛⬜',
       '⬜⬛⬜⬜⬛⬜',
       '⬜⬛⬜⬜⬛⬜',
       '⬜⬛⬛⬛⬛⬜',
       '⬜⬜⬜⬜⬜⬜']
n_1 = ['⬜⬜⬜⬜⬜⬜',
       '⬜⬜⬛⬛⬜⬜',
       '⬜⬜⬜⬛⬜⬜',
       '⬜⬜⬜⬛⬜⬜',
       '⬜⬜⬜⬛⬜⬜',
      '⬜⬛⬛⬛⬛⬜',
      '⬜⬜⬜⬜⬜⬜']
n_2 = ['⬛⬛⬛⬛',
        '     ⬛',
    '⬛⬛⬛⬛',
    '⬛     ',
    '⬛⬛⬛⬛']
n_3 = ['⬛⬛⬛⬛',
       '       ⬛',
       '⬛⬛⬛⬛',
       '      ⬛',
       '⬛⬛⬛⬛']
n_4 = ['⬛    ⬛',
        '⬛    ⬛',
       '⬛⬛⬛⬛',
       '      ⬛',
       '      ⬛']
n_5 = ['⬛⬛⬛⬛',
        '⬛     ',               
       '⬛⬛⬛⬛',
       '      ⬛',
       '⬛⬛⬛⬛']
n_6 = ['⬛⬛⬛⬛',
        '⬛     ',        
       '⬛⬛⬛⬛',
       '⬛    ⬛',
       '⬛⬛⬛⬛']
n_7 = ['⬛⬛⬛⬛',
        '      ⬛',
       '      ⬛',
       '      ⬛',   
       '      ⬛']
n_8 = ['⬛⬛⬛⬛',
       '⬛    ⬛',
       '⬛⬛⬛⬛',
       '⬛    ⬛',
       '⬛⬛⬛⬛']
n_9 = ['⬛⬛⬛⬛',
       '⬛    ⬛',
       '⬛⬛⬛⬛',
       '      ⬛',
       '⬛⬛⬛⬛']
n_u = ['⬜⬜⬜⬜⬜',
       '⬜⬜⬛⬜⬜',
       '⬜⬜⬜⬜⬜',
       '⬜⬜⬛⬜⬜',
       '⬜⬜⬜⬜⬜']

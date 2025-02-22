kun  = int(input('kunni kiriting: '))
oy = int(input('oyni kiriting: '))

day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
if oy < 1 or oy > 12:
    print('bunday oy yoq')
elif kun < 1 or kun > day_in_month[-1]:
    print('bunday sana yoq')
else:
    if kun == day_in_month[-1]:
        oy += 1
        kun = 1
    else:
        kun += 1
    if oy > 12:
        oy = 1
    print(f'{kun:02} {oy:02}')
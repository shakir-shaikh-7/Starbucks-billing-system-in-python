print('\t\t\t\t\tWelcome to Starbucks ')

print(f"{'-'*120}")

print('''\t\t\t\t\t\t Menu
    \n
\t     Hot Coffees               $           Tea                   $            Cold Coffee                  $

\t 01: Veranda Blend             4$     07: Chai Tea               2$        13: Iced Coffee                4$
\t 02: White Chocolate Mocha     5$     08: Mint Majesty           3$        14: pink Drink Starbucks       5$
\t 03: Peppermint Mocha          4$     09: Chai Tea latte         3$        15: Fresh Orange               5$
\t 04: Flat White                3$     10: Earl Grey Tea          2$        16: Apple Juice                7$
\t 05: Caffe Americano           2$     11: Matcha Tea latte       3$        17: SBC Milk                   7$
\t 06: Breakfast Sandwich        5$     12: Teavana Tea Latte      4$        18: Nitro Cold Brew            5$''')

print(f"{'-'*120}")

db = {1: ['Veranda Blend', 4], 2: ['White Chocolate Mocha', 5], 3: ['Peppermint Mocha', 4], 4: ['Flat White', 3], 5: ['Caffe Americano', 2], 6: ['Breakfast Sandwich', 5], 7: ['Chai Tea', 2], 8: ['Mint Majesty', 3], 9: ['Chai Tea latte', 3], 10: [
    'Earl Grey Tea', 2], 11: ['Matcha Tea latte', 3], 12: ['Teavana Tea Latte', 4], 13: ['Iced Coffee', 4], 14: ['pink Drink Starbucks', 5], 15: ['Fresh Orange', 5], 16: ['Apple Juice', 7], 17: ['SBC Milk', 7], 18: ['Nitro Cold Brew', 5]}

order_list = []
while True:
    order = int(input('Enter your order no: '))
    if order > len(db):
        print()
        print('please enter valid order name')
        break
    order_list.append(db[order])
    choice = input('Do you want to continue [y/n] : ')
    if choice == 'n':
        print('\n\t\t\t\t\t Thank You for order')
        break

print(f"{'-'*100}")
print(f'\n{"Order_No"} \t\t{"Order_Name"} \t\t\t{"Price"}\t\t\t{"Total"}')
print(f"{'-'*100}")

Sr_No = 0
Total = 0
for i in order_list:
    Sr_No += 1
    Total += i[1]
    r = 24-len(i[0][::])
    print(f'{Sr_No:5d}\t\t {i[0]} {" "*r} {i[1]:15d} {""}')
    print(f"{'.'*100}")


print(f'\n\t\t\t\t\t\tYour total Bill without GST: \t{Total}$')
GST = (Total*0.18)+Total
print(f"\n{' '*30}{'.'*70}")
print(
    f'\n\t\t\t\tYour total Bill in Rupees Including 18% GST:\t{GST*80:04.2f} \u20B9')
print(f"\n{'.'*100}")
print('\n\t\t\t\tThank you for visiting Starbucks')

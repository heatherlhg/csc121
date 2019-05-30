shipping_method = input('Please select your preferred method of shipping: [S for standard or E for express]: ')
weight = float(input('Please enter the weight of your package: '))

shipping_method = shipping_method.upper()

if shipping_method == 'S':
    if weight < 4:
        shipping_charge = weight * 1.05
        print('Your shipping charge will be: $',shipping_charge)
    if 4 < weight < 8:
        shipping_charge = weight * 0.95
        print('Your shipping charge will be: $', shipping_charge)
    if 8 < weight < 15:
        shipping_charge = weight * 0.85
        print('Your shipping charge will be: $', shipping_charge)
    if weight > 15:
        shipping_charge = weight * 1.05
        print('Your shipping charge will be: $', shipping_charge)
elif shipping_method =='E':
    if weight < 2:
        shipping_charge = weight * 3.25
        print('Your shipping charge will be: $',shipping_charge)
    if 2 < weight < 5:
        shipping_charge = weight * 2.95
        print('Your shipping charge will be: $', shipping_charge)
    if 5 < weight < 10:
        shipping_charge = weight * 2.75
        print('Your shipping charge will be: $', shipping_charge)
    if weight > 10:
        shipping_charge = weight * 2.55
        print('Your shipping charge will be: $', shipping_charge)

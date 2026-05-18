import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

choice = random.choice(products)
print(choice)

samples_3 = random.sample(products, 3)
print(samples_3)

samples_shuffled = random.shuffle(products)
print(products)

daily_tran = random.randint(50,300)
print(daily_tran)



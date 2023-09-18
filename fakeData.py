import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Product, Brand



def seed_brand(n):
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image= f'brands/{images[random.randint(0,9)]}'


        )
    print(f'seed {n} brands successfully')


def seed_product(n):
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg']
    flags = ['New','Sale','Feature']
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            image = f'brands/{images[random.randint(0,9)]}', 
            flag = flags[random.randint(0,2)], 
            price = round(random.uniform(20.99,99.99),2),
            sku =  random.randint(1000,10000000),
            subtitle = fake.text(max_nb_chars=150),
            dsecreiption = fake.text(max_nb_chars=1500),
            quantity = random.randint(0,30),
            brand = Brand.objects.get(id=random.randint(1,100))
        )

    print(f'seed {n} Product successfully')

#seed_brand(105)

seed_product(2000)
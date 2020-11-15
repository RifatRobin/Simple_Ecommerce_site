from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField
    productName = models.CharField(max_length=30)
    productDescription = models.CharField(max_length=250)
    # category
    Med = 'Medicine'
    Food = 'Food'
    Fshn = 'Fashion'
    Category = [
        (Med, 'Medicine'),
        (Food, 'Food'),
        (Fshn, 'Fashion'),
    ]
    category = models.CharField(
        max_length=10,
        choices=Category,
        default=Med,
    )

    Image = models.ImageField(upload_to='shop/img', default="")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # currency
    tk = 'taka'
    rp = 'rupe'
    Currency = [
        (tk, 'taka'),
        (rp, 'rupe')
    ]
    currency = models.CharField(max_length=6, choices=Currency, default=tk,)

    madeDate = models.DateField()
    expireDate = models.DateField()
    # quantity = models.IntegerField(null=False)

    # stock_status
    IS = 'In stock'
    OS = 'Out of stock'
    Status_Of_Product = [
        (IS, 'In stock'),
        (OS, 'Out of stock'),
    ]
    status_of_product = models.CharField(
        max_length=15,
        choices=Status_Of_Product,
        default=IS,
    )

    # adding the name of product instade of deafult products object(value)

    def __str__(self):
        return self.productName


class Contact(models.Model):
    problem_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    problem = models.CharField(max_length=1000)

    def __str__(self):
        return "Objection from: "+self.name


class Order(models.Model):
    order_id = models.IntegerField(
        primary_key=True, blank=False, serialize=True, unique=True)

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    Bemail = models.EmailField(max_length=30)
    phone = models.CharField(max_length=11)
    pid = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)

    # def __str__(self):
    #     return str("Order id : "+str(self.order_id))

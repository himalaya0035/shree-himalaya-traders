from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):  # all the info about the customer
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  # ek user ka ek hi customer se
    name = models.CharField(max_length=200, null=True)  # and we have also linked customer with the user in the database
    email = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=12, null=True, blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc1 = models.CharField(max_length=100)
    price1 = models.DecimalField(max_digits=7, decimal_places=0)
    desc2 = models.CharField(max_length=100, null=True, blank=True)
    price2 = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    desc3 = models.CharField(max_length=100, null=True, blank=True)
    price3 = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property  # decorator
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url


class Order(models.Model):  # this model contains the complete order of a customer
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    order_total = models.DecimalField(max_digits=7, decimal_places=0, default=0, null=True, blank=True)
    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):    # each order item
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    feedback = models.CharField(max_length=600, null=True,blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS,blank=True,default='Pending')
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.product.name

    @property
    def get_total(self):  # self is the object which calls the fn
        total = self.price * self.quantity
        return total


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    store_address = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_address


class ContactForm(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.CharField(max_length=100, default=None)
    PhoneNo = models.CharField(max_length=12)
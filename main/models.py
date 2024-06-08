from django.contrib.auth.models import User
from django.db import models




class MenuUser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class AdminCustomer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField(unique=True, null=True)
    account_type = models.CharField(max_length=100, null=True)
    profile_img = models.ImageField(upload_to='customer_imgs/', null=True)

    def __str__(self):
        return self.user.username


class Menu(models.Model):
    
    customer = models.ForeignKey(AdminCustomer, on_delete=models.CASCADE, null=True,related_name='customer_menus')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='product_imgs/', null=True, blank=True)
    cook = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=200, unique=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    price = models.CharField(max_length=13)

    def __str__(self):
        return self.title





class Review(models.Model):
    customer = models.ForeignKey(AdminCustomer, on_delete=models.CASCADE, null=True,related_name='reviews_user')
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE, null=True,related_name='menu_ratings')
    rating = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.comment}'

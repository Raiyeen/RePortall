from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True) 
    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    

# class Tag(models.Model):
#     name =models.CharField(max_length=100, null=True)
    
#     def __str__(self):
#         return self.name

    
class Review(models.Model):
    ADDRRESS =(
        ('Mirpur 10', 'Mirpur 10'),
        ('Pallabi', 'Pallabi'),
        ('Kazipara', 'Kazipara'),
        ('Agargaon', 'Agargaon'),
        ('shewrapara', 'shewrapara'),
        ('Uttara', 'Uttara'),
        ('Bijoy soroni', 'Bijoy soroni'),
        ('Rupnagar', 'Rupnagar'),
        ('Other', 'Other')
    )
    
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200, null=True, choices=ADDRRESS)
    # tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    
    

class ReportSubmission(models.Model):
        STATUS =(
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Completed', 'Completed')
        )
    
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
        review = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True)
        # date_created = models.DateTimeField(auto_now_add=True, null=True)
        status = models.CharField(max_length=50, null=True, choices=STATUS, default='Pending')
        
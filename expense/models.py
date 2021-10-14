from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Payment(models.Model):
    name=models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = 'payments'

    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) this show the article just created.
        return reverse('category-list')


class Expense(models.Model):
    description=models.CharField(max_length=200)
    amount= models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE,null=True)
    payment_date= models.DateTimeField(default=now)
    created_on= models.DateTimeField(auto_now_add=True)
    last_modified= models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.description

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) this show the article just created.
        return reverse('expense-list')

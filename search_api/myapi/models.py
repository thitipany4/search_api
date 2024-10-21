from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) ->str:
        return f'{self.name}'

class Products(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return f'{self.name}'
    
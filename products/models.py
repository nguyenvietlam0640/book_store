from django.db import models
from datetime import datetime
# Create your models here.




class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ('name', ) 

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/category/{self.slug}'
    
    def get_books_total(self):
        number = 0
        category = Category.objects.get(slug=self.slug)
        total= category.products.count()
        
        return total

    
class Book(models.Model):
    category = models.ForeignKey(Category, related_name= 'products', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(default=str(title))
    author = models.CharField(max_length=50, blank=False)
    des = models.TextField(blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    published_date = models.DateTimeField(default=datetime.now())
    unit_price = models.DecimalField(max_digits=5, decimal_places= 2)
    photo = models.ImageField(upload_to='bookcover/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/category/{self.category.slug}/{self.slug}'
    

    def get_image(self):
        if self.photo:
            return 'http://127.0.0.1:8000'+ self.photo.url
        return ''





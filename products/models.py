from django.db import models
from datetime import datetime, date
# Create your models here.
from authentication.models import User
import django.utils.timezone

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
        category = Category.objects.get(slug=self.slug)
        total = category.products.count()

        return total


class Book(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    slug = models.SlugField()  # this field must be unique
    author = models.CharField(max_length=50, blank=False)
    des = models.TextField(blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    published_date = models.DateField(default=datetime.now)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='bookcover/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/category/{self.category.slug}/{self.slug}'

    def get_total_rating_count(self):
        count = 0
        comments = self.comments.all()
        for comment in comments:
            count += 1
        return count

    def get_total_rating_value(self):
        total_rating_count = self.get_total_rating_count()
        total_rating_value = 0
        if total_rating_count == 0:
            return 0
        comments = self.comments.all()
        for comment in comments:
            total_rating_value += comment.rating

        sum = round(total_rating_value/total_rating_count)
        return sum

    def get_image(self):
        if self.photo:
            return 'http://127.0.0.1:8000' + self.photo.url
        return ''


class Comment(models.Model):

    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    created_for = models.ForeignKey(
        Book, related_name='comments', on_delete=models.CASCADE)

    rating = models.IntegerField(blank=False)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        ordering = ('-created_at',)
        unique_together = ('created_by', 'created_for')
    
    def __str__(self):
        return f'{self.created_by} for {self.created_for}'

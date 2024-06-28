from django.db import models
from django.utils.text import slugify
from django.db import transaction

#Category
class Category(models.Model):

    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=110)
    content = models.TextField()
    img_url = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        new_slug = slugify(self.title)
        original_slug = new_slug
        counter = 1
        while Post.objects.filter(slug=new_slug).exists():
            new_slug = f"{original_slug}-{counter}"
            counter += 1
        return new_slug

    def __str__(self):
        return self.title


   
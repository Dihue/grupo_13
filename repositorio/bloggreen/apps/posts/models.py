from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey()
    categoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title



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


class Comment(models.Model):
   # user = models.ForeignKey()
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   timestamp = models.DateTimeField(auto_now_add=True)
   content = models.TextField()


   def __str__(self):
       return self.user.username
       
class PostView(models.Model):
   # user = models.ForeignKey()
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   timestamp = models.DateTimeField(auto_now_add=True)


   def __str__(self):
       return self.user.username


class Like(models.Model):
    # user = models.ForeignKey()
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   
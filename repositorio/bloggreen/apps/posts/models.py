from django.db import models     
from django.conf import settings
from django.core.exceptions import ValidationError

def validar_extension(valor):
	if not valor.name.endswith(settings.ALLOWED_IMG):
		raise ValidationError("Ese formato de imagen no esta permitido.")

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    portada = models.ImageField(upload_to='post/', null=True, blank=True, validators=[validar_extension])
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, default=1, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=False, blank=False, default=1, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likesPost')
    dislike = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislikesPost')

    def __str__(self):
        return '%s - %s - %s - %s' % (self.title, self.categoria, self.user, self.portada)

    def total_likes(self):
        return self.like.count()
    
    def total_dislikes(self):
        return self.dislike.count()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=False, on_delete=models.CASCADE, related_name='commentsPost')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    def __str__(self):
       return self.user

from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length= 200)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    text = models.TextField()

    def __str__(self):
        return self.titulo
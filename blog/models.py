from django.db import models

# Create your models here.



class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']
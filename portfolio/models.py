from django.db import models




class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url_address = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
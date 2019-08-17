from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()

    def __str__(self):
        return self.title
    
    def summary_resume(self):
        final = ''
        if len(self.summary[:310])>=310:
            final = '...'
        return self.summary[:310]+final

    def pub_date_resume(self):
        return self.pub_date.strftime('%b %e %Y')
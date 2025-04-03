from django.db import models

class ResearchPaper(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    abstract = models.TextField()
    # publication_date = models.DateField()
    # journal_name = models.CharField(max_length=255)
    # doi = models.CharField(max_length=255, unique=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='research_papers/')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)  # New field for thumbnail
   
    def __str__(self):
        return self.title

# Create your models here.

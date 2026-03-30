from django.db import models

class Project(models.Model):

    CATEGORY_CHOICES = [
        ('personal', 'Personal Project'),
        ('experience', 'Work Experience'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')
    title=models.CharField(max_length=200)
    description=models.TextField()
    tech_stack=models.CharField()
    github_link=models.URLField()
    live_link=models.URLField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
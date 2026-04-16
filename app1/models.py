from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Resume(models.Model):
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    
    career_objective=models.TextField()
    education = models.TextField()
    t_skills = models.TextField()
    s_skills = models.TextField()
    projects=models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
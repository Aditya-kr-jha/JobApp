from django.db import models
from django.utils.text import slugify

# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.company


class Location(models.Model):
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=8)

    def __str__(self):
        return self.city


class jobPost(models.Model):
    JOB_TYPE = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    location = models.OneToOneField(
        Location, on_delete=models.CASCADE, null=True)  # type: ignore
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skills)
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE)

    def save(self, *args, **kwargs):
        if not self.id:  # type: ignore
            self.slug = slugify(self.title)
        return super(jobPost, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.salary}"

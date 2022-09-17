from django.db import models #importing objects from the database
from django.contrib.auth.models import User 


STATUS = (#tuple 
    (0,"Draft"),
    (1,"Publish")
)

# Each blog post object we create will have these characteristics
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)#the unique identifying part of a web address ie. website.com/`slug`
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)#Tells the website if its a draft or not default is found in the tuple STATUS

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

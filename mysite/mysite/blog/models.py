# importing classes from the databases
from django.db import models
from django.contrib.auth.models import User

#'STATUS' tells the website if the blog post is a draft or not
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

#each blog post object we create will have these characteristics
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)# 'slug' is the unique identifier for the web address. For example, website.com/slug
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
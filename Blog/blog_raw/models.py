from django.db import models
from django.contrib.auth.models import User

## status for the posted blog
STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Blog_posts')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS,default=0)

    ## how this is goinf to show in str
    def __str__(self):
        return self.title 
    
    ## how in order it show
    ## lest show first
    class Meta:
        ordering = ['-created_at']

    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment {} by {} '.format(self.body,self.name)

    class Meta:
        ordering = ['-created_at']

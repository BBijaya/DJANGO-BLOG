from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

#from ckeditor.fields import RichTextField # this doesnot supoort uploading image
from ckeditor_uploader.fields import RichTextUploadingField # supports uploading image

# Create your models here.

class PublishedManager(models.Manager):
    """ custom model manager """
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')



class Post(models.Model):
    """ blog post model """

    STATUS_CHOICES = (
        ('draft','DRAFT'),
        ('published','PUBLISHED'),
    )
    title = models.CharField(max_length=250,help_text="give title to your post")
    slug = models.SlugField(max_length=250, unique_for_date='publish',
                            help_text="SEO friendly post title (automatically filled)")
    thumbnail = models.ImageField(blank=True, null=True, upload_to="thumbnail/%Y/%m/%D/")
    body = RichTextUploadingField(help_text="content of the post goes here")
    tags =TaggableManager()
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE, 
                                related_name='blog_posts',help_text='select post author')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10 , choices= STATUS_CHOICES, default='draft')


    objects = models.Manager() # the default model manager
    published = PublishedManager() # our custom manager

    class Meta:
        ordering = ('-publish',) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, 
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug])



class Comment(models.Model):
    """ comment model for blog """
    post = models.ForeignKey('blog.Post',related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)



    class Meta:
        ordering = ('created',)

    def __str__(self):
        return ' comment by {} on {}'.format(self.name,self.post)

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# Custom Manager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


# Our Post Model

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='blog_posts')
    illustration = models.ImageField(null=True, blank=True, upload_to="blog/", default='images/LogoLarge.svg')
    body = RichTextUploadingField()
    highlight = models.BooleanField(default=False)
    tags = models.ManyToManyField("self",related_name='blog_tags')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # The default manager
    objects = models.Manager()

    # Custom made manager
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail_view', args=[self.publish.year, self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

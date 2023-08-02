from django.db import models

# Create your models here.


class Article(models.Model):
    # CharField is a string field, and CharField(max_length=100) means that the maximum length of the string is 100 characters.
    title = models.CharField(max_length=100)
    # SlugField is like CharField, but it can only contain letters, numbers, underscores, and hyphens. We will use the slug to build beautiful, SEO-friendly URLs for our blog posts.
    slug = models.SlugField()
    # TextField is for long text without a limit. Sounds perfect for blog posts, right?
    body = models.TextField()
    # DateTimeField is a field that will store date and time.
    date = models.DateTimeField(auto_now_add=True)
  # image = models.ImageField(upload_to='images/') # ImageField is a field for uploading images.
  #  author = models.TextField() # TextField is for long text without a limit. Sounds perfect for blog posts, right?

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."

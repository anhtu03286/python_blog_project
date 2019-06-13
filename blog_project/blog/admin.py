from django.contrib import admin

#import models Post
from .models import Post

# Register your models here.

admin.site.register(Post) #show Post in dashboard admin
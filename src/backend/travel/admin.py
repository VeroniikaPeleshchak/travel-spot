from django.contrib import admin
from .models import About, BlogPost, GalleryPhoto, ContactMessage, Review, TravelTip

admin.site.register(About)
admin.site.register(BlogPost)
admin.site.register(GalleryPhoto)
admin.site.register(ContactMessage)
admin.site.register(Review)
admin.site.register(TravelTip)


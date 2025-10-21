from django.db import models


class About(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GalleryPhoto(models.Model):
    title = models.CharField(max_length=150)
    image_url = models.URLField()
    location = models.CharField(max_length=100)
    date_taken = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    destination_name = models.CharField(max_length=150)
    rating = models.IntegerField()  
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} review for {self.destination_name}"

class TravelTip(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField(null=True, blank=True) 
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


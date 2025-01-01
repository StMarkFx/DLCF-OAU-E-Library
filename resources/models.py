from django.db import models
from django.contrib.auth.models import User

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="contributor")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="contributor_pics/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reader")
    last_downloaded_at = models.DateTimeField(blank=True, null=True)
    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Resource(models.Model):
    FACULTY_CHOICES = [
        ("SCI", "Science"),
        ("ENG", "Engineering"),
        ("ART", "Arts"),
        # Add more faculties as needed
    ]
    LEVEL_CHOICES = [
        ("100", "100 Level"),
        ("200", "200 Level"),
        ("300", "300 Level"),
        ("400", "400 Level"),
        ("500", "500 Level"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="resources/")
    uploaded_by = models.ForeignKey(Contributor, on_delete=models.SET_NULL, null=True, related_name="resources")
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES)
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    download_count = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

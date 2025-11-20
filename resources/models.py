from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Resource(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('science', 'Science'),
        ('english', 'English'),
        ('history', 'History'),
        ('computer', 'Computer Science'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology'),
        ('other', 'Other'),
    ]

    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_resources')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='other')
    file = models.FileField(
        upload_to='resources/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    download_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title

    def get_file_size(self):
        """Return file size in MB"""
        if self.file:
            return round(self.file.size / (1024 * 1024), 2)
        return 0

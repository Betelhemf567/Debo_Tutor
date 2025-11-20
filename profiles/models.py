from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    school = models.CharField(max_length=200, blank=True)
    grade_level = models.CharField(max_length=50, blank=True)
    favorite_subjects = models.CharField(max_length=200, blank=True, help_text="Comma-separated subjects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_questions_count(self):
        return self.user.questions.count()

    def get_replies_count(self):
        return self.user.replies.count()

    def get_resources_count(self):
        return self.user.uploaded_resources.count()


# Automatically create profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

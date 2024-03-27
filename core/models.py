from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extraFields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extraFields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extraFields):
        extraFields.setdefault('is_staff', True)
        extraFields.setdefault('is_superuser', True)
        extraFields.setdefault('is_active', True)

        if extraFields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extraFields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extraFields)


class User(AbstractUser):

    avatar = CloudinaryField('avatar')
    coverImage = CloudinaryField('coverImage', blank=True)
    refreshToken = models.CharField(max_length=200, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "first_name", "last_name", "avatar")

    def __str__(self) -> str:
        return self.email


class Video(models.Model):

    videoFile = CloudinaryField(
        'videoFile')
    thumbnailFile = CloudinaryField('thumbnail')
    owner = models.ForeignKey("User", verbose_name=_(
        "owner"), on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(_("title"), max_length=50)
    description = models.CharField(_("description"), max_length=50)
    duration = models.DecimalField(
        _("duration"), max_digits=5, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.title


class Tweet(models.Model):

    owner = models.ForeignKey("User", verbose_name=_(
        "user"), on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField(_("content"))
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    subscriber = models.ForeignKey("User", verbose_name=_(
        "subscriber"), on_delete=models.CASCADE, related_name='subscriber')
    channel = models.ForeignKey(
        "User", verbose_name=_(""), on_delete=models.CASCADE, related_name='channel')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


from django.db import models
from pytils.translit import slugify
from datetime import datetime
from django import forms

class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    image = models.CharField("URL-фото", max_length=500)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Guide(models.Model):
    title = models.CharField("Название гайда", max_length=255)
    image = models.CharField("URL-фото", max_length=500)
    creator = models.CharField("Автор", max_length=255)
    date = models.DateTimeField("Дата и время публикации", default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='guides')
    description = models.TextField("Описание", blank=True)  # Add this line for the description

    class Meta:
        verbose_name = "Гайд"
        verbose_name_plural = "Гайды"

    def __str__(self):
        return f"{self.title} by {self.creator}"
    
class Game(models.Model):
    title = models.CharField("Название гайда", max_length=255)
    image = models.CharField("URL-фото", max_length=500)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return f"Game with image URL: {self.image}"

class RegistrationForm(forms.Form):
    username = forms.CharField(label='User', max_length=100)
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Pass1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Pass2', widget=forms.PasswordInput)

class GamePost(models.Model):
    CATEGORY_CHOICES = [
        ('Minecraft', 'Minecraft'),
        ('Doom', 'Doom'),
        ('Terraria', 'Terraria'),
        ('Stardew Valley', 'Stardew Valley'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()

    def __str__(self):
        return self.title
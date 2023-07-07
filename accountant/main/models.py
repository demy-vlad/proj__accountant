from django.db import models

# Create your models here.

class ParserConfig(models.Model):
    title = models.CharField("Короткий опис", max_length=250)
    url = models.URLField("Посилання")

    class Meta:
        verbose_name = "Налаштування"
        verbose_name_plural = "Налаштування"
    
    def __str__(self) -> str:
        return self.title

class ParserResult(models.Model):
    date = models.DateField("Дата додавання")
    time = models.TimeField("Час додавання")
    url = models.URLField("Посилання")

    class Meta:
        verbose_name = "Результат пошуку"
        verbose_name_plural = "Результат пошуку"
    
    def __str__(self) -> str:
        return self.url

class TelegramConfig(models.Model):
    chat_id = models.CharField("Посилання на чат", max_length=100)
    token = models.CharField("Токен боту", max_length=100)

    class Meta:
        verbose_name = "Telegram"
        verbose_name_plural = "Telegram"
    
    def __str__(self) -> str:
        return self.chat_id

from django.db import models
from django.contrib.auth.models import User

"""
Модели для сайта "Хранитель Семени"
- Skill — навыки героя
- Mission — лог битв
- WisdomTip — советы
- ContactMessage — сообщения из формы
- SeedForce — сила семени (одна запись)
- CodeExample — примеры кода для способности
"""

class Skill(models.Model):
    """Навыки героя"""
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    icon = models.CharField(max_length=10, default="", verbose_name="Иконка")
    power_level = models.IntegerField(default=5, verbose_name="Уровень силы")

    def __str__(self):
        return self.name

class Mission(models.Model):
    """Подвиги героя(лог битв)"""
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    
    def __str__(self):
        return self.title
    
class WisdomTip(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50]
    
class ContactMessage(models.Model):
    """Сообщения из формы"""
    name = models.CharField(max_length=100, verbose_name="Имя")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}: {self.message[:30]}"
    
    from django.db import models

class SeedForce(models.Model):
    value = models.IntegerField(default=100)

    def __str__(self):
        return f"Сила семени: {self.value}"

    def increase(self, amount):
        self.value += amount
        self.save()

    def decrease(self, amount):
        self.value -= amount
        if self.value < 0:
            self.value = 0
        self.save()

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1, defaults={'value': 100})
        return obj

class CodeExample(models.Model):
    title = models.CharField(max_length=100)
    bad_code = models.TextField()
    good_code = models.TextField()

    def __str__(self):
        return self.title
    
class Battle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100, default="Смыть баг")
    result = models.CharField(max_length=100) # Успех/Провал
    timestamp = models.DateTimeField(auto_now_add=True)
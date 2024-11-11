from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CarAd(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ads/')  # Путь для сохранения изображений
    phone_number = PhoneNumberField()  # Поле для номера телефона

    # Опции для рассрочки
    INSTALLMENT_CHOICES = [
        ('6', '6 месяцев'),
        ('9', '9 месяцев'),
        ('12', '12 месяцев'),
    ]
    installment_plan = models.CharField(
        max_length=2,
        choices=INSTALLMENT_CHOICES,
        default='6'  # Значение по умолчанию
    )

    # Опционально, чтобы выводить заголовок объявления в админке
    def __str__(self):
        return self.title

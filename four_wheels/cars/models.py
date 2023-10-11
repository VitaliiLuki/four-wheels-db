from django.db import models

from users.models import User

# Наполнить базу моделями авто
MODEL_OF_CAR = [('BMW', 'bmw'),
                ('MERSEDES_BENZ', 'Mersedes-Benz'),
                ('VW', 'Volkswagen'),
                ('SKODA', 'Skoda'),
                ('HONDA', 'Honda'),
                ('HYUNDAI', 'Hyundai'),
                ('OPEL', 'Opel'),
                ('PEUGEUT', 'Peugeut'),
                ('CITROEN', 'Citroen'),
                ('KIA', 'Kia'),
                ('FORD', 'Ford')]

TYPE_OF_TRANSMISSION = [('AUTOMATIC', 'automatic'),
                        ('MANUAL', 'manual'),
                        ('CVT', 'cvt')]

TYPE_OF_DRIVE = [('FRONT_DRIVE', 'front-wheel drive'),
                 ('REAR_DRIVE', 'rear drive'),
                 ('FOUR_WHEEL', 'four-wheel drive')]

TYPE_OF_ENGINE = [('PETROL', 'petrol engine'),
                  ('DIESEL', 'diesel engine')]

OPTIONS = [('AUTOPILOT', 'autopilot'),
           ('HEAT_SEATS', 'heated seats')]
# Нужно будет добавить опции, эти опции для тестинга


class CarModel(models.Model):
    model_name = models.CharField('Название модели',
                                  max_length=100)

    def __str__(self) -> str:
        return self.model_name


class Option(models.Model):
    option_name = models.CharField('Название опции',
                                   max_length=100)

    def __str__(self) -> str:
        return self.option_name


class Car(models.Model):
    """Keeps an information about Cars."""
    car_model = models.ForeignKey(CarModel,
                                  verbose_name='Модель авто',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='car_model')
    price = models.PositiveIntegerField(verbose_name='Цена авто')
    photo = models.ImageField(
        verbose_name='Фото авто',
        upload_to='cars/images/',
        null=True,
        blank=True,
        default=None
    )
    year_of_manufacture = models.CharField(verbose_name='Год выпуска',
                                           max_length=10)
    # Нужна валидация на чтобы год не мог быть больше текущего
    description = models.TextField('Описание авто', blank=True)
    mileage = models.PositiveIntegerField('Пробег')
    transmission_type = models.CharField(verbose_name='Тип коробки передач',
                                         max_length=50,
                                         choices=TYPE_OF_TRANSMISSION)
    drive_type = models.CharField('Тип привода',
                                  choices=TYPE_OF_DRIVE,
                                  max_length=50,
                                  default='front-wheel drive')
    engine_capacity = models.FloatField('Объем двигателя')
    engine_type = models.CharField('Тип двигателя',
                                   choices=TYPE_OF_ENGINE,
                                   max_length=50,
                                   default='petrol engine')
    car_power = models.SmallIntegerField('Мощность автомобиля л.с.')
    number_of_owners = models.SmallIntegerField('Количество владельцев')
    options = models.ManyToManyField(Option,
                                     verbose_name='Дополнительные опции',
                                     through='CarOption')
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='Car')
    _is_active = models.BooleanField('Объявление размещено',
                                     default=False)
    _is_closed = models.BooleanField('Объявление снято с публикации',
                                     default=False)

    def __str__(self) -> str:
        return '{0} {1}'.format(self.owner, self.car_model)


class CarOption(models.Model):
    """Кеeps information about car and option"""
    car = models.ForeignKey(Car,
                            related_name='car_option',
                            on_delete=models.CASCADE)
    option = models.ForeignKey(Option,
                               related_name='car_option',
                               on_delete=models.CASCADE)

    # def make_active(self):
    #     self._is_active = True
    #     return f'Объявление {self.id} размещено'

    # def close_announcement(self):
    #     self._is_closed = True
    #     return f'Объявление {self.id} снято с публикации'

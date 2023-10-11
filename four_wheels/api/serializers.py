from cars.models import Car, CarModel, CarOption, Option
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'mobile_phone',
                  'password')
        read_only_fields = ('id',
                            'first_name',
                            'last_name',
                            'mobile_phone')


class OptionGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ('option_name',)


class CarOptionSerializer(serializers.ModelSerializer):

    id = serializers.PrimaryKeyRelatedField(read_only=True, source='option.id')
    # option_name = serializers.CharField(source='option.option_name')

    class Meta:
        model = Option
        fields = ('id', 'option_name')


# Ошибка передачи данных, а именно options
class CarSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    options = CarOptionSerializer(many=True)
    car_model = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = ('__all__')

    def create(self, validated_data):
        options = validated_data.pop('options')
        instance = Car.objects.create(**validated_data)
        print(options)
        for option in options:
            option_id = option['id']
            try:
                current_option = Option.objects.get(id=option_id)
                print('current_option: ', current_option,
                      'current_option_type: ', type(current_option))
                CarOption.objects.create(option=current_option,
                                         car=instance)
            except ObjectDoesNotExist:
                raise (f'Указанная опция "{option}" отстутствует в базе.')
        instance.options.set(options)
        return instance

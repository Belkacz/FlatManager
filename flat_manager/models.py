from django.db import models
from django.contrib.auth.models import User
from django.db import models

from django.core.validators import MaxValueValidator

class Owner(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    pesel = models.IntegerField()
    date_of_birth = models.DateField()
    contact_number = models.IntegerField()
    def class_name(self):
        return self.__class__.__name__.lower()
    def __str__(self):
        return f"Pan/Pani {self.last_name}, {self.first_name},tel. {self.contact_number}"
    # def get_string_fields(self):
    #     excluded_fields = ['pesel', 'date_of_birth']
    #
    #     field_names = [field.name for field in self._meta.get_fields()
    #                    if field.name not in excluded_fields]
    #     values = []
    #     for field_name in field_names:
    #         values.append('%s' % getattr(self, field_name))
    #     return ' | '.join(values)


class Agent(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    agency = models.CharField(max_length=256)
    contact_number = models.SmallIntegerField()
    def class_name(self):
        return self.__class__.__name__.lower()
    def __str__(self):
        return f"Agent/ka {self.last_name}, {self.first_name}, tel. {self.contact_number}"

class Flat(models.Model):
    city = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    house_number = models.SmallIntegerField()
    flat_number = models.SmallIntegerField()
    post_code = models.IntegerField()
    flat_surface = models.SmallIntegerField()
    basic_flat_rental_cost = models.SmallIntegerField(null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    def class_name(self):
        return self.__class__.__name__.lower()
    def __str__(self):
        return f"Mieszkanie: ul. {self.street},nr. {self.house_number}/ {self.flat_number} - {self.city}"

class Room(models.Model):
    basic_room_rental_cost = models.SmallIntegerField(null=True)
    room_surface = models.SmallIntegerField()
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, null=True)
    room_number = models.IntegerField()
    def class_name(self):
        return self.__class__.__name__.lower()
    def __str__(self):
        return f"pokój nr.{self.room_number} w mieszkaniu ul.{self.flat.street}, {self.flat.house_number}/{self.flat.flat_number} "


class Rentier(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    pesel = models.IntegerField()
    contact_number = models.IntegerField()
    date_of_birth = models.DateField()
    def class_name(self):
        return self.__class__.__name__.lower()
    def __str__(self):
        return f"Najemca {self.last_name}, {self.first_name}, nr. tel. {self.contact_number}"

class LeaseAgreement(models.Model):
    contract_number = models.IntegerField(unique=True, null=True)
    end_of_contract = models.DateField()
    contract_date = models.DateField()
    date_of_payment = models.SmallIntegerField(null=True, validators=[
        MaxValueValidator(30),])
    monthly_cost = models.IntegerField()
    agent_provision = models.IntegerField()
    number_of_keys = models.SmallIntegerField(null=True)
    damage_desc = models.CharField(max_length=512)
    deposit = models.IntegerField(null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    equipment = models.CharField(max_length=512)
    flat = models.ManyToManyField(Flat)
    rooms = models.ManyToManyField(Room)
    rentier = models.ForeignKey(Rentier, on_delete=models.CASCADE, null=True)
    def class_name(self):
        return self.__class__.__name__.lower()
    def __str__(self):
        # flat = self.flat.get().first()
        # if flat:
        #     return f"{self.contract_number}, {self.owner}, " \
        #            f"{flat.city}, {flat.street}, {flat.flat_number}/{flat.house_number}",
        return f"Unowa nr. {self.contract_number} Między {self.owner} a najemcą {self.rentier} Miasto {self.flat.first().city}, ul. {self.flat.first().street}, " \
               f"{self.flat.first().house_number}/{self.flat.first().flat_number}"
    # flat = ", ".join(str(flat) for flat in self.flat.all())
    # return f"{self.contract_number}, {self.owner}, "
    # f"{flat}",
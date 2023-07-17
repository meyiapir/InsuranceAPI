from tortoise import fields
from tortoise.models import Model


class CargoType(Model):  # Модель типа груза
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    rate = fields.FloatField()
    date = fields.DateField()

    def __str__(self):
        return self.name


class InsuranceRequest(Model):  # Модель запроса на страховку
    id = fields.IntField(pk=True)
    rate = fields.FloatField()
    cargo_type = fields.ForeignKeyField('models.CargoType', related_name='insurance_requests')
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"Request #{self.id}"

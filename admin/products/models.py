from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"


class User(models.Model):
    pass

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"

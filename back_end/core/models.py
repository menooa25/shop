from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group

User = get_user_model()


class Staff(User):
    def save(self):
        self.is_staff = True
        self.password = make_password(self.password)
        super(Staff, self).save()
        group = Group.objects.get(name='staff')
        group.user_set.add(self.id)

    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمند ها'

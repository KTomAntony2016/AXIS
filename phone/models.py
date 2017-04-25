# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from model_utils.models import TimeStampedModel
from django.db import models
from phone.constants import STATUS_TYPE
# Create your models here.

class Phone(TimeStampedModel):

    STATUS_TYPE_C = (
        (STATUS_TYPE.NEW.value, 'New'),
        (STATUS_TYPE.SUCCESS.value, 'Success'),
        (STATUS_TYPE.FAILURE.value, 'Failure'),
        (STATUS_TYPE.Half_Filled.value, 'Half Filled'),
        (STATUS_TYPE.Not_reachable.value, 'Not Reachable'),
        (STATUS_TYPE.Wrong_No.value, 'Wrong No'),
        (STATUS_TYPE.Trash.value, 'Trash'),
    )

    phone = models.CharField(max_length=10, null=False)
    status = models.IntegerField(choices=STATUS_TYPE_C, null=False, default=STATUS_TYPE.NEW.value)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'phone'
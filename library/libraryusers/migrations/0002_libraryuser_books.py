# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stacks', '0001_initial'),
        ('libraryusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryuser',
            name='books',
            field=models.ManyToManyField(to='stacks.Book', through='stacks.LoanedBook'),
        ),
    ]

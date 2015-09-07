# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_number', models.CharField(help_text='Usually Dewey Decimal or Library of Congress classification.', max_length=100)),
                ('item_number', models.PositiveIntegerField(default=1, help_text='If we have multiple copies of this book, a unique identifier for the item.')),
                ('borrowing_period', models.PositiveIntegerField(default=14, help_text='Number of days this item can be borrowed before being renewed.')),
                ('max_renewal_count', models.IntegerField(default=2, help_text='Maxmimum number of times this item can be renewed.')),
                ('maximum_fine', models.DecimalField(default=b'25.00', help_text='Maximum amount the patron will be fined for an overdue item. This is usually the replacement cost of the item.', max_digits=5, decimal_places=2)),
                ('page_count', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=4000)),
                ('daily_fine', models.DecimalField(default=b'0.25', help_text='Amount the patron will be fined per day for an overdue library book', max_digits=4, decimal_places=2)),
                ('authors', models.ManyToManyField(related_name='works', to='stacks.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoanedBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkout_date', models.DateField()),
                ('due_date', models.DateField()),
                ('return_date', models.DateField(null=True, blank=True)),
                ('times_renewed', models.IntegerField(default=0)),
                ('fine_paid', models.NullBooleanField()),
                ('book', models.ForeignKey(to='stacks.Book')),
                ('patron', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('call_number', 'item_number')]),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-13 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='age',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

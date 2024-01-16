# Generated by Django 4.2.7 on 2024-01-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('booster_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='campaign/images')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('vaccines_offered', models.ManyToManyField(related_name='campaign', to='campaign.vaccine')),
            ],
        ),
    ]

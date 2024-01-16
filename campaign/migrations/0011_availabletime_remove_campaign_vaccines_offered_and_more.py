# Generated by Django 4.2.7 on 2024-01-15 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_useraccount_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaign', '0010_alter_review_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='vaccines_offered',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='booster_required',
        ),
        migrations.AddField(
            model_name='vaccine',
            name='campaign',
            field=models.ManyToManyField(related_name='campaign', to='campaign.campaign'),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='dose_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vaccine', to='account.useraccount'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='age',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='DoseBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_dose', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('first_dose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.availabletime')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
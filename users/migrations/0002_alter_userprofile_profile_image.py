# Generated by Django 3.2.8 on 2022-06-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
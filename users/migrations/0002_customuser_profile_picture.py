# Generated by Django 4.2.11 on 2024-03-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='profile_picture.jpg', upload_to=''),
        ),
    ]

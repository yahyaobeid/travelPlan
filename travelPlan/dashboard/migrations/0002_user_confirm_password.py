# Generated by Django 4.2.3 on 2023-07-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default='', max_length=300),
        ),
    ]
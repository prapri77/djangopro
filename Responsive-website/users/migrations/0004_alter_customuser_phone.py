# Generated by Django 5.0.3 on 2024-04-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
    ]
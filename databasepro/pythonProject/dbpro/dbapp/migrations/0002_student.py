# Generated by Django 5.0.3 on 2024-03-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
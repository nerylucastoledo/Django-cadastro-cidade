# Generated by Django 3.0.5 on 2021-02-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_cidade_capital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
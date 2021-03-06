# Generated by Django 3.0.5 on 2021-02-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Estado'),
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Pais'),
        ),
    ]

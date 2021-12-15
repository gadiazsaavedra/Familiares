# Generated by Django 3.2.9 on 2021-12-15 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamiliar', '0003_auto_20211211_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Primo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('profesional', models.BooleanField()),
                ('fechaDeNacimiento', models.DateField()),
            ],
        ),
    ]
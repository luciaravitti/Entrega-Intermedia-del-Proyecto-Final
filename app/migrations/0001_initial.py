# Generated by Django 4.1.4 on 2022-12-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('vegano', models.BooleanField()),
                ('cantidad_personas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('vegano', models.BooleanField()),
                ('cantidad_personas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('vegano', models.BooleanField()),
                ('cantidad_personas', models.IntegerField()),
            ],
        ),
    ]

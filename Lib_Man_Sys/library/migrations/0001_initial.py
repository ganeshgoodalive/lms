# Generated by Django 4.0.4 on 2022-10-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lib_Man_Sys_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('auth_name', models.CharField(max_length=50)),
                ('book_price', models.FloatField()),
                ('book_type', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('published_on', models.DateField()),
            ],
        ),
    ]
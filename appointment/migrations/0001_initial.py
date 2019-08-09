# Generated by Django 2.2.3 on 2019-08-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('num_people', models.IntegerField()),
                ('amount', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('text', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='home_title_image//%Y/%m/%d')),
                ('home_title', models.CharField(max_length=20)),
                ('home_image', models.ImageField(blank=True, null=True, upload_to='home_preview_images/%Y/%m/%d')),
            ],
        ),
    ]

# Generated by Django 2.0 on 2017-12-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='posts/img/', verbose_name='Картинка'),
        ),
    ]

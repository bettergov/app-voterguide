# Generated by Django 2.0.1 on 2018-02-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qas', '0009_auto_20180131_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
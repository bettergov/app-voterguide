# Generated by Django 2.0.1 on 2018-01-30 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qas', '0005_auto_20180130_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qas.Candidate'),
        ),
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qas.Question'),
        ),
    ]

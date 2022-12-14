# Generated by Django 4.1 on 2022-08-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precision_paint_api', '0002_alter_workorder_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='estimate_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

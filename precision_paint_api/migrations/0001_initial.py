# Generated by Django 4.1 on 2022-08-10 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimate_date', models.DateField()),
                ('start_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('approved', models.BooleanField()),
                ('completed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=110)),
                ('description', models.CharField(max_length=110)),
                ('date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField()),
                ('deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateField()),
                ('amount_owed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('completed', models.BooleanField()),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='precision_paint_api.estimate')),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='precision_paint_api.workorder')),
            ],
        ),
        migrations.AddField(
            model_name='estimate',
            name='work_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estimates', to='precision_paint_api.workorder'),
        ),
    ]
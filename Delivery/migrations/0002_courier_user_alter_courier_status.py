# Generated by Django 4.0.2 on 2022-02-24 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courier',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]

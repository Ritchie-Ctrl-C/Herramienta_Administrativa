# Generated by Django 4.1.7 on 2025-02-09 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0002_producto_creado_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-25 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_evolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='evolution',
            name='evolution',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='evolutions', to='api.pokemon'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.4 on 2025-04-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0002_alter_incident_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='Open', max_length=20),
        ),
    ]

# Generated by Django 5.1.2 on 2025-03-09 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_school', '0010_alter_aboutcourses_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclasssecond',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_second', to='it_school.masterclass'),
        ),
    ]

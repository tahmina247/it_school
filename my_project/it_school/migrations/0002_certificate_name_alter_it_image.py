# Generated by Django 5.1.7 on 2025-03-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='name',
            field=models.CharField(default=0, max_length=24),
        ),
        migrations.AlterField(
            model_name='it',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

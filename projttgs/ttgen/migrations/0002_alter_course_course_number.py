# Generated by Django 4.2.3 on 2023-08-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
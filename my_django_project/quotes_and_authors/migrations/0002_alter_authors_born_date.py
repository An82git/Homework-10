# Generated by Django 5.0.2 on 2024-02-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_and_authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='born_date',
            field=models.CharField(max_length=20),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testdb', '0003_delete_adltest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adltest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=100)),
                ('valor1', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-22 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210409_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffin',
            name='category_form_coffin',
        ),
        migrations.DeleteModel(
            name='qwerty',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.DeleteModel(
            name='Coffin',
        ),
        migrations.DeleteModel(
            name='FormOfCoffin',
        ),
    ]

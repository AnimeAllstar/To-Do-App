# Generated by Django 3.1 on 2020-09-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200919_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='content',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='colors',
            field=models.ManyToManyField(to='MainApp.color'),
        ),
    ]

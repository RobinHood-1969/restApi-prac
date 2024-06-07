# Generated by Django 5.0.6 on 2024-06-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='toDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('completed', models.BooleanField(default=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 5.0.7 on 2024-10-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0002_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('description', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

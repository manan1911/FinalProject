# Generated by Django 5.1.6 on 2025-04-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0020_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'doc')], default=1, max_length=50),
        ),
    ]

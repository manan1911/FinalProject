# Generated by Django 5.1.6 on 2025-04-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0027_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin')], default=1, max_length=50),
        ),
    ]

# Generated by Django 4.2 on 2024-08-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_status_alter_category_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

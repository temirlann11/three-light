# Generated by Django 4.2.9 on 2024-02-18 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tim',
            new_name='Post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Запис', 'verbose_name_plural': 'Записи'},
        ),
    ]

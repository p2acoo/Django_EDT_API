# Generated by Django 4.0.5 on 2022-06-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0003_alter_edt_semaine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edt',
            name='Semaine',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='edtweek',
            name='Semaine',
            field=models.IntegerField(unique=True),
        ),
    ]

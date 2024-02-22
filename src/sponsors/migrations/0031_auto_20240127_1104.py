# Generated by Django 3.1.7 on 2024-01-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0030_remove_pre_recorded_policy_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openrole',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017'), ('pycontw-2018', 'PyCon Taiwan 2018'), ('pycontw-2019', 'PyCon Taiwan 2019'), ('pycontw-2020', 'PyCon Taiwan 2020'), ('pycontw-2021', 'PyCon Taiwan 2021'), ('pycontw-2022', 'PyCon Taiwan 2022'), ('pycontw-2023', 'PyCon Taiwan 2023'), ('pycontw-2024', 'PyCon Taiwan 2024')], default='pycontw-2024', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017'), ('pycontw-2018', 'PyCon Taiwan 2018'), ('pycontw-2019', 'PyCon Taiwan 2019'), ('pycontw-2020', 'PyCon Taiwan 2020'), ('pycontw-2021', 'PyCon Taiwan 2021'), ('pycontw-2022', 'PyCon Taiwan 2022'), ('pycontw-2023', 'PyCon Taiwan 2023'), ('pycontw-2024', 'PyCon Taiwan 2024')], default='pycontw-2024', verbose_name='conference'),
        ),
    ]
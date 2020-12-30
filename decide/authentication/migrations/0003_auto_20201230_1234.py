# Generated by Django 2.0 on 2020-12-30 12:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201217_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votinguser',
            name='candidatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voting.Candidatura', verbose_name='Candidature'),
        ),
        migrations.AlterField(
            model_name='votinguser',
            name='curso',
            field=models.CharField(choices=[('PRIMERO', 'First'), ('SEGUNDO', 'Second'), ('TERCERO', 'Third'), ('CUARTO', 'Fourth'), ('MASTER', 'Master')], default='PRIMERO', max_length=7, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='votinguser',
            name='dni',
            field=models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='El formato debe ser 8 digitos y una letra mayuscula.', regex='^\\d{8}[A-Z]{1}$')], verbose_name='NIF'),
        ),
        migrations.AlterField(
            model_name='votinguser',
            name='sexo',
            field=models.CharField(choices=[('HOMBRE', 'Man'), ('MUJER', 'Woman'), ('OTRO', 'Other')], default='OTRO', max_length=6, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='votinguser',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Grade'),
        ),
    ]
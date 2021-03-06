# Generated by Django 3.2.3 on 2021-07-20 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_Fuente_Dinero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoGasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'TipoGasto',
            },
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_Registro', models.DateField()),
                ('Monto', models.IntegerField()),
                ('Fuente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_Fuente_Dinero.fuentedinero', verbose_name='Fuente')),
                ('Tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Gastos.tipogasto', verbose_name='Tipo')),
            ],
            options={
                'verbose_name_plural': 'Gasto',
            },
        ),
    ]

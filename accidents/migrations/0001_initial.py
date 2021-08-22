# Generated by Django 2.2.18 on 2021-08-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(blank=True, max_length=20)),
                ('fecha_accidente', models.DateField()),
                ('residuo_fisico', models.FloatField()),
                ('residuo_emocional', models.FloatField()),
                ('residuo_intelectual', models.FloatField()),
                ('residuo_intuicional', models.FloatField()),
            ],
            options={
                'verbose_name': 'Accidente',
                'verbose_name_plural': 'Accidentes',
            },
        ),
    ]

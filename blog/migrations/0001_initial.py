# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('numero_bolsas', models.IntegerField()),
                ('sexo', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('diagnostico', models.IntegerField()),
                ('servicio', models.IntegerField()),
                ('hemoglobina', models.FloatField()),
                ('hematocrito', models.IntegerField()),
                ('gs_receptor', models.IntegerField()),
                ('gs_donante', models.IntegerField()),
                ('hiv', models.FloatField()),
                ('hb', models.FloatField()),
                ('anti_hb', models.FloatField()),
                ('anti_hcv', models.FloatField()),
                ('htlv', models.FloatField()),
                ('sifilis', models.FloatField()),
                ('chagas', models.FloatField()),
            ],
        ),
    ]

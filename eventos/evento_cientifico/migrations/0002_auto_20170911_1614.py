# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento_cientifico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='artigocientifico',
            options={'verbose_name': 'Artigo Cientifico', 'verbose_name_plural': 'Artigos Cientificos'},
        ),
        migrations.AddField(
            model_name='publicacao',
            name='artigo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArtigoCientifico', to='evento_cientifico.ArtigoCientifico'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Autor', to='evento_cientifico.Autor'),
        ),
    ]

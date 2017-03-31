# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_bootstrap3.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0014_translations_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='boostrap3imageplugin',
            name='description',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='Caption Text', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3imageplugin',
            name='popup_image',
            field=models.BooleanField(default=False, verbose_name='Popup original image on click (cannot be used with links)'),
        ),
        migrations.AlterField(
            model_name='boostrap3imageplugin',
            name='title',
            field=aldryn_bootstrap3.model_fields.MiniText(default='', verbose_name='Caption Title', blank=True),
        ),
        migrations.AddField(
            model_name='boostrap3imageplugin',
            name='alignment',
            field=models.CharField(default='', choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], max_length=255, blank=True, help_text='Adds a class to the image for left, right or center.', verbose_name='Align Image'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-13 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('seednetwork', '0002_remove_memberinfo_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberinfo',
            name='usda_zone',
            field=models.CharField(choices=[(b'-', b'-'), (b'1a', b'1a'), (b'1b', b'1b'), (b'2a', b'2a'), (b'2b', b'2b'), (b'3a', b'3a'), (b'3b', b'3b'), (b'4a', b'4a'), (b'4b', b'4b'), (b'5a', b'5a'), (b'5b', b'5b'), (b'6a', b'6a'), (b'6b', b'6b'), (b'7a', b'7a'), (b'7b', b'7b'), (b'8a', b'8a'), (b'8b', b'8b'), (b'9a', b'9a'), (b'9b', b'9b'), (b'10a', b'10a'), (b'10b', b'10b'), (b'11a', b'11a'), (b'11b', b'11b'), (b'12a', b'12a'), (b'12b', b'12b')], default=b'-', max_length=3),
        ),
        migrations.AlterField(
            model_name='memberinfo',
            name='phone',
            field=localflavor.us.models.PhoneNumberField(blank=True, max_length=20),
        ),
    ]

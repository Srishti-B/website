# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-03 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0074_auto_20180903_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workeligibility',
            name='eligible_to_work',
            field=models.BooleanField(help_text='<p><b>Student visas</b>: Please note that in some countries, students studying abroad on a student visa may not be eligible to work full-time (40 hours a week). If you are on a student visa, please double check with your school counselors before applying.</p><p><b>Spouse visas</b>: In some countries, spousal visas may not allow spouses to work. Please contact your immigration officer if you have any questions about whether your visa allows you to work full-time (40 hours a week).</p><p><b>International Travel</b>: Outreachy interns are not required to work while they are traveling internationally. If you travel for more than 1 week, you may need to extend your internship. Internships can be extended for up to five weeks.</p>', verbose_name='Are you eligible to work for 40 hours a week in ALL the countries you will be living in for the entire internship period, and five weeks after the internship period ends?'),
        ),
    ]

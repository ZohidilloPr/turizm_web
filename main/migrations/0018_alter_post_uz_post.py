# Generated by Django 4.1.2 on 2022-11-04 11:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_post_uz_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uz_post',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
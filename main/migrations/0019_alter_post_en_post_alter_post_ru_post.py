# Generated by Django 4.1.2 on 2022-11-05 18:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_post_uz_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='en_post',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ru_post',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
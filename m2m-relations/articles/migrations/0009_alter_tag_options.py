# Generated by Django 4.2.4 on 2023-09-23 17:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0008_alter_articlescope_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Тээг", "verbose_name_plural": "Тээги"},
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plan", "0006_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="memo",
            field=models.TextField(blank=True, null=True),
        ),
    ]

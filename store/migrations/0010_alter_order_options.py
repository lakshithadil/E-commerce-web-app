# Generated by Django 4.2.3 on 2023-07-27 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0009_alter_customer_options_remove_customer_email_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"permissions": [("cancel_order", "can cancel order")]},
        ),
    ]

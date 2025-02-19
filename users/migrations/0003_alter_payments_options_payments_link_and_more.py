# Generated by Django 4.2 on 2024-07-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payments",
            options={"verbose_name": "Оплата", "verbose_name_plural": "Оплаты"},
        ),
        migrations.AddField(
            model_name="payments",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=300, null=True, verbose_name=" id сессии"
            ),
        ),
    ]

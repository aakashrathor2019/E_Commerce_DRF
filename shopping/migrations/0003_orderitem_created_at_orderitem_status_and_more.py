# Generated by Django 4.2.8 on 2024-08-27 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shopping", "0002_appuser_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="status",
            field=models.CharField(default="Pending", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shopping.appuser",
            ),
        ),
    ]

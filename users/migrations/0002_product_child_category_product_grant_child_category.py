# Generated by Django 4.0.3 on 2023-04-28 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='child_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.childcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='grant_child_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.grantchildcategory'),
        ),
    ]

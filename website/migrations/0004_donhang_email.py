# Generated by Django 4.0.4 on 2022-05-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_sanpham_anhsp_sanpham_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='donhang',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

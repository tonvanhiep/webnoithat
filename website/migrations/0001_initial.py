# Generated by Django 4.0.4 on 2022-05-10 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=30)),
                ('sodt', models.CharField(max_length=15)),
                ('diachi', models.TextField()),
                ('tongtien', models.IntegerField(default=0)),
                ('ngaytao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anhsp', models.CharField(default='../../static/images/bantra.jpg', max_length=100)),
                ('giasp', models.IntegerField()),
                ('tensp', models.CharField(max_length=100)),
                ('thongtin', models.TextField()),
                ('mota', models.TextField()),
                ('ngaytao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChiTietDH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl', models.IntegerField()),
                ('iddh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.donhang')),
                ('idsp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.sanpham')),
            ],
        ),
        migrations.CreateModel(
            name='BinhLuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('noidung', models.TextField()),
                ('ngaytao', models.DateTimeField(auto_now_add=True)),
                ('idsp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.sanpham')),
            ],
        ),
    ]

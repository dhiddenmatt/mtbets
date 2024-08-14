# Generated by Django 5.1 on 2024-08-14 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('matchedBetting', models.BooleanField()),
                ('casaApuesta', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('cuota', models.DecimalField(decimal_places=2, max_digits=6)),
                ('liquidez', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mercado', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('videoUrl', models.URLField()),
                ('media', models.FileField(upload_to='')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, null=True)),
                ('purchaseDate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MatchedBetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availivableUntil', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product'),
        ),
        migrations.CreateModel(
            name='SureBetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availivableUntil', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
    ]

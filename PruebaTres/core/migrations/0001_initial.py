# Generated by Django 3.2.3 on 2021-06-23 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idPais', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Pais')),
                ('nombrePais', models.CharField(max_length=50, verbose_name='Nombre del Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('idProveedor', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Proveedor')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre Proveedor')),
                ('Fono', models.CharField(max_length=12, verbose_name='Telefóno Proveedor')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Dirección Proveedor')),
                ('Mail', models.CharField(max_length=50, verbose_name='E-mail Proveedor')),
                ('Pass', models.CharField(max_length=20, verbose_name='Password Proveedor')),
                ('IdPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais')),
            ],
        ),
    ]

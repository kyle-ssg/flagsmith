# Generated by Django 2.2.12 on 2020-05-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0002_auto_20200221_2126'),
        ('environments', '0011_auto_20200220_0044'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EnvironmentPermission',
        ),
        migrations.CreateModel(
            name='EnvironmentPermissionModel',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('permissions.permissionmodel',),
        ),
        migrations.AlterField(
            model_name='userenvironmentpermission',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='permissions.PermissionModel'),
        ),
        migrations.AlterField(
            model_name='userpermissiongroupenvironmentpermission',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='permissions.PermissionModel'),
        ),
    ]

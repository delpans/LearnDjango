# Generated by Django 3.1.7 on 2021-03-09 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0004_auto_20210309_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='接口名称', max_length=200, unique=True, verbose_name='接口名称')),
                ('tester', models.CharField(help_text='测试人员', max_length=50, verbose_name='测试人员')),
                ('desc', models.TextField(blank=True, default='', help_text='简要描述', null=True, verbose_name='简要描述')),
                ('project', models.ForeignKey(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, to='projects.projects', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'tb_interfaces',
            },
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-24 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20211024_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Комментарий')),
                ('comment_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('comment_binding', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]

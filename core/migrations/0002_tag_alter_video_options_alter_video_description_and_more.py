# Generated by Django 5.1.3 on 2024-11-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
            ],
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Vídeo', 'verbose_name_plural': 'Vídeos'},
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='video',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Está publicado?'),
        ),
        migrations.AlterField(
            model_name='video',
            name='num_likes',
            field=models.IntegerField(default=0, verbose_name='Número de curtidas'),
        ),
        migrations.AlterField(
            model_name='video',
            name='num_views',
            field=models.IntegerField(default=0, verbose_name='Número de visualizações'),
        ),
        migrations.AlterField(
            model_name='video',
            name='published_at',
            field=models.DateTimeField(verbose_name='Publicado em'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/', verbose_name='Vídeo'),
        ),
    ]

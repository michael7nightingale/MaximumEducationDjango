# Generated by Django 4.2.3 on 2023-08-28 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, unique=True)),
                ('description', models.TextField()),
                ('country', models.CharField(choices=[('RUSSIA', 'Russia'), ('CHINA', 'China'), ('KOREA', 'Korea')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('model', models.CharField(db_index=True, max_length=130)),
                ('description', models.TextField()),
                ('made_in_country', models.CharField(choices=[('RUSSIA', 'Russia'), ('CHINA', 'China'), ('KOREA', 'Korea')], max_length=100)),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='goods.category')),
            ],
        ),
        migrations.CreateModel(
            name='GoodImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.good')),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='images',
            field=models.ManyToManyField(through='goods.GoodImage', to='goods.good'),
        ),
        migrations.AddField(
            model_name='good',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.subcategory'),
        ),
        migrations.CreateModel(
            name='DescriptionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=70)),
                ('value', models.CharField(max_length=100)),
                ('tag', models.CharField(choices=[('SIZE', 'Size'), ('ACCUMUlATOR', 'Accumulator'), ('PROCESSOR', 'processor')], max_length=100)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='description_items', to='goods.good')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='good',
            unique_together={('name', 'model', 'brand')},
        ),
    ]
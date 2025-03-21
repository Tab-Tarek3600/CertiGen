# Generated by Django 5.1.7 on 2025-03-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=255)),
                ('validity_days', models.IntegerField(default=365)),
                ('key_size', models.IntegerField(choices=[(2084, '2048 bits'), (4096, '4096 bits')], default=2048)),
                ('hash_algorithm', models.CharField(choices=[('SHA256', 'SHA-256'), ('SHA512', 'SHA-512')], default='SHA256', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0020_usersubscription_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='user_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]

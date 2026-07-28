from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinrequest',
            name='account',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='website.account',
            ),
        ),
    ]

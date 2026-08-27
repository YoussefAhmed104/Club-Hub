from django.db import migrations, models


def copy_personal_email_to_email(apps, schema_editor):
    CustomUser = apps.get_model('accounts', 'CustomUser')
    CustomUser.objects.filter(email='').update(
        email=models.F('personal_email')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RunPython(copy_personal_email_to_email, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='customuser',
            name='personal_email',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
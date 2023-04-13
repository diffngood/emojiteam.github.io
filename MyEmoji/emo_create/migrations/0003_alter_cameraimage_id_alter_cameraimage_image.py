
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emo_create", "0002_cameraimage_img_date_alter_img_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cameraimage",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="cameraimage",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="webcam"),
        ),
    ]

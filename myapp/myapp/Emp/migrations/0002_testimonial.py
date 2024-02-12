# Generated by Django 5.0.1 on 2024-02-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Emp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("testimonial", models.TextField()),
                ("picture", models.ImageField(upload_to="testimonials/")),
                ("rating", models.IntegerField(max_length=1)),
            ],
        ),
    ]

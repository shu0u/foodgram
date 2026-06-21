import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загружает ингредиенты из CSV-файла'

    def handle(self, *args, **options):
        possible_paths = [
            Path('/data/ingredients.csv'),
            Path(settings.BASE_DIR) / 'data' / 'ingredients.csv',
            Path(settings.BASE_DIR).parent / 'data' / 'ingredients.csv',
        ]

        csv_path = None
        for path in possible_paths:
            if path.exists():
                csv_path = path
                break

        if csv_path is None:
            self.stdout.write(
                self.style.ERROR(
                    f'Файл не найден. Искали в: {possible_paths}'
                )
            )
            return

        self.stdout.write(f'Загружаем из: {csv_path}')

        ingredients_to_create = []
        with open(csv_path, encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    name, measurement_unit = row[0].strip(), row[1].strip()
                    ingredients_to_create.append(
                        Ingredient(name=name, measurement_unit=measurement_unit)
                    )

        Ingredient.objects.bulk_create(
            ingredients_to_create,
            ignore_conflicts=True,
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Загружено {len(ingredients_to_create)} ингредиентов'
            )
        )

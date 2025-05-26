from django.core.management.base import BaseCommand
from django.core.management import call_command

from catalog.models import Products, Category

class Command(BaseCommand):

    help = 'Add products to the database'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Products.objects.all().delete()


        call_command('loaddata', 'catalog.json')
        self.stdout.write(self.style.SUCCESS('Выполнено'))


        category3, _ = Category.objects.get_or_create(name='Сладости', description='Всякая всячина',)

        product3 = [{'name': 'Шоколад', 'description': 'Молочный шоколад', 'category': category3, 'purchase_price': 85, 'created_at': '2025-05-25',
        'updated_at': '2025-05-25'},
                    {'name': 'Конфеты', 'description': 'Конфеты на развес', 'category': category3, 'purchase_price': 50, 'created_at': '2025-05-25',
        'updated_at': '2025-05-25'},]

        for prod_data in product3:
            prod, created = Products.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Выполнено успешно: {prod.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Уже имеется: {prod.name}'))
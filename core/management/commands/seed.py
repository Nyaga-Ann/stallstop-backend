import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

from vendors.models import VendorProfile, VendorFavorite, VendorReview
from customers.models import CustomerProfile
from items.models import Item, ItemFavorite
from orders.models import Order

User = get_user_model()
faker = Faker("en_US")

CATEGORIES = {
    "clothing": ["Official Top", "Official Trouser", "Sundress", "Skirt", "Long Sleeve"],
    "shoes": ["Nike Low Dunks", "New Balance 550", "Canvas Shoes", "Sneakers", "Loafers"],
    "bags": ["Handbag", "Backpack", "Sling Bag", "Laptop Bag", "Tote Bag"],
    "accessories": ["Watch", "Necklace", "Belt", "Cap", "Sunglasses"]
}

class Command(BaseCommand):
    help = "Seed database with fake data for testing"

    def handle(self, *args, **kwargs):
        self.stdout.write("🌱 Seeding database...")

        # Clear old data
        Order.objects.all().delete()
        ItemFavorite.objects.all().delete()
        Item.objects.all().delete()
        VendorFavorite.objects.all().delete()
        VendorReview.objects.all().delete()
        VendorProfile.objects.all().delete()
        CustomerProfile.objects.all().delete()
        User.objects.all().delete()

        # Create Users (20)
        users = []
        for i in range(20):
            user = User.objects.create_user(
                username=faker.user_name() + str(i),
                email=faker.email(),
                password="password123",
            )
            users.append(user)

        # Assign Vendors (10)
        vendors = []
        for i in range(10):
            vendor_user = users[i]
            vendor = VendorProfile.objects.create(
                user=vendor_user,
                business_name=faker.company(),
                location=f"{faker.city()}, Kenya",
                latitude=float(faker.latitude()),
                longitude=float(faker.longitude()),
                description=faker.sentence(),
                contact_phone=f"+254{random.randint(700000000, 799999999)}",
                shop_type=random.choice(["physical", "online"]),
                whatsapp_number=f"+254{random.randint(700000000, 799999999)}",
            )
            vendors.append(vendor)

        # Assign Customers (10)
        customers = []
        for i in range(10, 20):
            c = CustomerProfile.objects.create(user=users[i])
            customers.append(c)

        # Create Items (50)
        items = []
        for i in range(50):
            category = random.choice(list(CATEGORIES.keys()))
            name = random.choice(CATEGORIES[category])
            vendor = random.choice(vendors)
            item = Item.objects.create(
                vendor=vendor,
                name=name,
                description=faker.sentence(),
                price=random.randint(500, 5000),
                category=category,
                image_url="https://picsum.photos/200",  # placeholder image
            )
            items.append(item)

        # Vendor Reviews
        customers = CustomerProfile.objects.all()
        for i in range(30):
            customer_profile = random.choice(customers)  
            vendor = random.choice(vendors)
            review, created = VendorReview.objects.get_or_create(
                vendor=vendor,
                customer=customer_profile.user,
                defaults={
                    "rating": random.randint(1, 5),
                    "comment": faker.sentence(),
                }
            )
            if not created:
                review.rating = random.randint(1, 5)
                review.comment = faker.sentence()
                review.save()

        # Vendor Favorites
        for i in range(30):
            customer = random.choice(customers)
            vendor = random.choice(vendors)
            VendorFavorite.objects.get_or_create(
                customer=customer_profile.user,
                vendor=vendor
            )

        # Item Favorites
        for i in range(30):
            customer = random.choice(customers)
            item = random.choice(items)
            ItemFavorite.objects.get_or_create(
                customer=customer_profile.user,
                item=item
            )

        # Orders
        for i in range(30):
             customer_profile = random.choice(customers)
             item = random.choice(items)  
             vendor = item.vendor         

             order = Order.objects.create(
                 customer=customer_profile.user,
                 vendor=vendor,  
                 total_price=item.price,
                 status=random.choice(["pending", "accepted", "shipped", "cancelled"]),
             )
             order.items.add(item)

        self.stdout.write(self.style.SUCCESS("✅ Database seeded with sample data"))

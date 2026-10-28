"""
Script to populate rich sample data for the ShopEase E-Commerce platform.
Creates categories, products, superuser, sample customer, reviews, and demo orders.
"""

import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product, Review
from orders.models import Order, OrderItem

def run():
    print("=" * 60)
    print("Populating ShopEase Database with Rich Sample Data...")
    print("=" * 60)

    # 1. Create Superuser / Admin
    admin_user, created = User.objects.get_or_create(username='admin', defaults={
        'email': 'admin@shopease.local',
        'first_name': 'Store',
        'last_name': 'Administrator',
        'is_staff': True,
        'is_superuser': True
    })
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print(" [+] Superuser created: admin / admin123")
    else:
        print(" [i] Superuser already exists: admin")

    # 2. Create Demo Customers
    demo_user, created = User.objects.get_or_create(username='alex_rivers', defaults={
        'email': 'alex.rivers@example.com',
        'first_name': 'Alex',
        'last_name': 'Rivers',
    })
    if created:
        demo_user.set_password('password123')
        demo_user.save()
        print(" [+] Customer created: alex_rivers / password123")

    customer2, created = User.objects.get_or_create(username='sarah_connor', defaults={
        'email': 'sarah.c@example.com',
        'first_name': 'Sarah',
        'last_name': 'Connor',
    })
    if created:
        customer2.set_password('password123')
        customer2.save()
        print(" [+] Customer created: sarah_connor / password123")

    # 3. Create Categories
    categories_data = [
        {
            'name': 'Electronics & Gadgets',
            'slug': 'electronics-gadgets',
            'description': 'Latest smartphones, noise-canceling headphones, smartwatches, and computing accessories.'
        },
        {
            'name': 'Fashion & Apparel',
            'slug': 'fashion-apparel',
            'description': 'Trendy clothing, stylish jackets, formal footwear, and premium everyday wear.'
        },
        {
            'name': 'Home & Living',
            'slug': 'home-living',
            'description': 'Modern home appliances, kitchen essentials, ergonomic furniture, and cozy decor.'
        },
        {
            'name': 'Books & Learning',
            'slug': 'books-learning',
            'description': 'Bestselling novels, programming guides, design masterclasses, and productivity books.'
        },
        {
            'name': 'Sports & Fitness',
            'slug': 'sports-fitness',
            'description': 'Workout equipment, yoga gear, athletic shoes, and hydration flasks.'
        }
    ]

    category_objs = {}
    for cat_data in categories_data:
        cat, _ = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name'], 'description': cat_data['description']}
        )
        category_objs[cat.slug] = cat
        print(f" [+] Category ready: {cat.name}")

    # 4. Create Realistic Products
    products_data = [
        # Electronics
        {
            'category': 'electronics-gadgets',
            'name': 'SonicPro Wireless ANC Headphones',
            'slug': 'sonicpro-wireless-anc-headphones',
            'description': 'Industry-leading active noise canceling wireless headphones with 40-hour battery life, ultra-comfortable memory foam earcups, and crystal clear studio acoustics.',
            'price': Decimal('199.99'),
            'original_price': Decimal('249.99'),
            'stock': 25,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'electronics-gadgets',
            'name': 'PulseFit Ultra Smartwatch GPS',
            'slug': 'pulsefit-ultra-smartwatch-gps',
            'description': 'Next-generation fitness smartwatch with AMOLED display, continuous heart-rate & SpO2 tracking, onboard GPS, and 50m water resistance.',
            'price': Decimal('149.50'),
            'original_price': Decimal('189.00'),
            'stock': 18,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'electronics-gadgets',
            'name': 'Mechanical RGB Gaming Keyboard',
            'slug': 'mechanical-rgb-gaming-keyboard',
            'description': 'Tactile mechanical blue-switch gaming keyboard with custom RGB backlighting, braided USB-C cable, and durable aircraft-grade aluminum top plate.',
            'price': Decimal('79.99'),
            'original_price': Decimal('99.99'),
            'stock': 30,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'electronics-gadgets',
            'name': 'Ultra-Slim 4K Portable Monitor 15.6"',
            'slug': 'ultra-slim-4k-portable-monitor',
            'description': 'Crystal clear IPS 4K portable display with USB-C and Mini-HDMI inputs. Perfect dual-screen companion for laptop workflows and mobile gaming.',
            'price': Decimal('229.00'),
            'original_price': Decimal('279.00'),
            'stock': 12,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=700&auto=format&fit=crop&q=80'
        },

        # Fashion
        {
            'category': 'fashion-apparel',
            'name': 'Classic Maverick Leather Jacket',
            'slug': 'classic-maverick-leather-jacket',
            'description': 'Handcrafted genuine lambskin leather jacket with smooth quilted interior lining, heavy-duty YKK zippers, and timeless motorcycle styling.',
            'price': Decimal('189.00'),
            'original_price': Decimal('240.00'),
            'stock': 14,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'fashion-apparel',
            'name': 'Heritage Canvas Everyday Backpack',
            'slug': 'heritage-canvas-everyday-backpack',
            'description': 'Vintage waterproof waxed canvas backpack featuring padded 15-inch laptop compartment, genuine leather straps, and brass buckle hardware.',
            'price': Decimal('64.99'),
            'original_price': Decimal('79.99'),
            'stock': 22,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'fashion-apparel',
            'name': 'Urban Minimalist Polarized Sunglasses',
            'slug': 'urban-minimalist-polarized-sunglasses',
            'description': 'Unisex UV400 polarized shades with lightweight titanium alloy frame, scratch-resistant mirrored lenses, and protective hard leather case.',
            'price': Decimal('45.00'),
            'original_price': Decimal('60.00'),
            'stock': 40,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=700&auto=format&fit=crop&q=80'
        },

        # Home & Living
        {
            'category': 'home-living',
            'name': 'Barista Touch Espresso Coffee Maker',
            'slug': 'barista-touch-espresso-maker',
            'description': 'Commercial 15-bar Italian pressure pump espresso machine with integrated conical burr grinder, digital PID temperature control, and steam wand for latte art.',
            'price': Decimal('349.99'),
            'original_price': Decimal('399.99'),
            'stock': 9,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'home-living',
            'name': 'Aroma Ultrasonic Essential Oil Diffuser',
            'slug': 'aroma-ultrasonic-essential-oil-diffuser',
            'description': 'Ceramic modern minimalist ultrasonic diffuser with 7 ambient LED colors, whisper-quiet operation, and automatic safety shut-off.',
            'price': Decimal('32.50'),
            'original_price': Decimal('42.00'),
            'stock': 35,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'home-living',
            'name': 'Ergonomic Breathable Mesh Desk Chair',
            'slug': 'ergonomic-breathable-mesh-desk-chair',
            'description': 'Adjustable lumbar support ergonomic executive desk chair with 3D armrests, smooth rollerblade wheels, and breathable high-tensile mesh back.',
            'price': Decimal('210.00'),
            'original_price': Decimal('260.00'),
            'stock': 15,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1580481077195-c95697623306?w=700&auto=format&fit=crop&q=80'
        },

        # Books & Learning
        {
            'category': 'books-learning',
            'name': 'Django 5 Enterprise Web Architecture Guide',
            'slug': 'django-5-enterprise-web-guide',
            'description': 'Master professional web development using Python and Django. Covers REST APIs, asynchronous channels, caching strategies, Docker deployment, and database scaling.',
            'price': Decimal('39.99'),
            'original_price': Decimal('49.99'),
            'stock': 50,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'books-learning',
            'name': 'The Pragmatic System Architect',
            'slug': 'the-pragmatic-system-architect',
            'description': 'A comprehensive handbook on distributed microservices, fault tolerance, event-driven design patterns, and engineering high-throughput software systems.',
            'price': Decimal('44.50'),
            'original_price': Decimal('55.00'),
            'stock': 28,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1532012164546-f432f2e3777f?w=700&auto=format&fit=crop&q=80'
        },

        # Sports & Fitness
        {
            'category': 'sports-fitness',
            'name': 'ProGrip Hex Dumbbell Set (Pair 20 lbs)',
            'slug': 'progrip-hex-dumbbell-set-20lbs',
            'description': 'Commercial rubber-encased hexagonal dumbbells with knurled ergonomic chrome handles to prevent rolling and protect home gym flooring.',
            'price': Decimal('69.99'),
            'original_price': Decimal('85.00'),
            'stock': 20,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'sports-fitness',
            'name': 'HydroVolt Vacuum Insulated Steel Flask 32oz',
            'slug': 'hydrovolt-vacuum-insulated-flask-32oz',
            'description': 'Double-wall vacuum insulated stainless steel water bottle. Keeps drinks icy cold for 24 hours or steaming hot for 12 hours. Sweat-free powder coat finish.',
            'price': Decimal('28.00'),
            'original_price': Decimal('35.00'),
            'stock': 45,
            'featured': False,
            'image_url': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=700&auto=format&fit=crop&q=80'
        },
        {
            'category': 'sports-fitness',
            'name': 'EcoAlign Non-Slip Natural Rubber Yoga Mat',
            'slug': 'ecoalign-non-slip-yoga-mat',
            'description': 'Premium 6mm high-density eco-friendly natural tree rubber yoga mat with laser-etched alignment body lines and extra joint cushioning.',
            'price': Decimal('55.00'),
            'original_price': Decimal('70.00'),
            'stock': 19,
            'featured': True,
            'image_url': 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=700&auto=format&fit=crop&q=80'
        }
    ]

    created_products = []
    for item in products_data:
        cat = category_objs[item['category']]
        prod, created = Product.objects.get_or_create(
            slug=item['slug'],
            defaults={
                'category': cat,
                'name': item['name'],
                'description': item['description'],
                'price': item['price'],
                'original_price': item['original_price'],
                'stock': item['stock'],
                'is_available': True,
                'featured': item['featured'],
                'image_url': item['image_url']
            }
        )
        created_products.append(prod)
        print(f" [+] Product ready: {prod.name} (${prod.price})")

    # 5. Create Reviews
    reviews_data = [
        {
            'product_slug': 'sonicpro-wireless-anc-headphones',
            'user': demo_user,
            'subject': 'Best noise canceling headphones I have owned!',
            'review': 'The soundstage is exceptional. Battery lasted the entire flight across continents. Very comfortable even after wearing for 6 straight hours.',
            'rating': 5
        },
        {
            'product_slug': 'sonicpro-wireless-anc-headphones',
            'user': customer2,
            'subject': 'Crisp sound and fast Bluetooth pairing',
            'review': 'Mic quality during Zoom meetings is remarkably clear. Fast USB-C charging too. Highly recommended for remote workers.',
            'rating': 5
        },
        {
            'product_slug': 'pulsefit-ultra-smartwatch-gps',
            'user': demo_user,
            'subject': 'Great fitness tracking companion',
            'review': 'Accurate heart rate sensor and beautiful AMOLED display. Syncs seamlessly with my phone.',
            'rating': 4
        },
        {
            'product_slug': 'barista-touch-espresso-maker',
            'user': customer2,
            'subject': 'Cafe quality espresso right at home',
            'review': 'Extracts rich golden crema consistently. The milk steam wand produces silky microfoam in under 30 seconds.',
            'rating': 5
        },
        {
            'product_slug': 'django-5-enterprise-web-guide',
            'user': demo_user,
            'subject': 'Essential book for every Python web developer',
            'review': 'Clear, deep explanations of Django ORM, query optimization, and architectural patterns. Top tier technical guide.',
            'rating': 5
        }
    ]

    for r in reviews_data:
        prod = Product.objects.filter(slug=r['product_slug']).first()
        if prod:
            Review.objects.get_or_create(
                product=prod,
                user=r['user'],
                defaults={
                    'subject': r['subject'],
                    'review': r['review'],
                    'rating': r['rating'],
                    'status': True
                }
            )
            print(f" [+] Review added for: {prod.name} by {r['user'].username}")

    # 6. Create Demo Past Orders for Alex Rivers
    order_data = {
        'user': demo_user,
        'order_number': 'ORD-20261025-DEMO01',
        'first_name': 'Alex',
        'last_name': 'Rivers',
        'phone': '+1 (555) 890-1234',
        'email': 'alex.rivers@example.com',
        'address_line_1': '742 Evergreen Terrace',
        'address_line_2': 'Apt 4B',
        'city': 'Seattle',
        'state': 'Washington',
        'country': 'United States',
        'postal_code': '98101',
        'order_note': 'Please ring doorbell on arrival.',
        'status': 'Delivered',
        'order_total': Decimal('229.99'),
        'tax': Decimal('10.00'),
        'shipping_cost': Decimal('0.00'),
        'is_ordered': True,
    }

    order_obj, created = Order.objects.get_or_create(
        order_number=order_data['order_number'],
        defaults=order_data
    )
    if created:
        prod1 = Product.objects.get(slug='sonicpro-wireless-anc-headphones')
        OrderItem.objects.create(
            order=order_obj,
            product=prod1,
            quantity=1,
            product_price=prod1.price,
            ordered=True
        )
        print(f" [+] Sample order created: {order_obj.order_number}")

    print("=" * 60)
    print("All sample data successfully populated!")
    print("=" * 60)

if __name__ == '__main__':
    run()

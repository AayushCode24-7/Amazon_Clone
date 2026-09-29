from django.shortcuts import render


def home(request):
    hero = {
        'title': 'Upgrade your home with fresh finds',
        'button': 'Shop now',
        'image': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1600&q=80',
    }

    promo_cards = [
        {'title': 'New arrivals', 'image': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80', 'link_text': 'See more'},
        {'title': 'Home essentials', 'image': 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80', 'link_text': 'Shop now'},
        {'title': 'Smart gadgets', 'image': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80', 'link_text': 'Explore'}
    ]

    product_cards = [
        {'name': 'Smart Watch', 'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80', 'price': '₹2,499'},
        {'name': 'Wireless Audio', 'image': 'https://images.unsplash.com/photo-1546868871-7041f2a55e12?auto=format&fit=crop&w=900&q=80', 'price': '₹1,799'},
        {'name': 'Desk Setup', 'image': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=80', 'price': '₹3,299'},
        {'name': 'Fitness Picks', 'image': 'https://images.unsplash.com/photo-1491553895911-0055eca6402d?auto=format&fit=crop&w=900&q=80', 'price': '₹2,099'},
        {'name': 'Laptop Stand', 'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=900&q=80', 'price': '₹1,499'},
        {'name': 'Minimal Lamp', 'image': 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80', 'price': '₹899'},
        {'name': 'Office Chair', 'image': 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80', 'price': '₹4,199'},
        {'name': 'Travel Bag', 'image': 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=900&q=80', 'price': '₹2,799'},
    ]

    context = {
        'hero': hero,
        'promo_cards': promo_cards,
        'product_cards': product_cards,
        'product_section_title': 'Popular items',
    }

    return render(request, 'home/home.html', context)

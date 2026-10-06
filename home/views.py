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
        {'name': 'Minimal Lamp', 'image': 'https://imgs.search.brave.com/eaQxbLyPCmMvJhd_IRkKCS-raAhDmaYHNPAIYXzqTWg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS1waG90by9t/aW5pbWFsaXN0LXdo/aXRlLWZsb29yLWxh/bXBfMjMtMjE0ODIz/ODUyOC5qcGc_c2Vt/dD1haXNfaHlicmlk', 'price': '₹899'},
        {'name': 'Office Chair', 'image': 'https://imgs.search.brave.com/Q76_9muYR2QrAi3dGkOp0XwFxhcj_3e1NdZNjCNVq_Q/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9yb3lh/bG9ha2luZGlhLmd1/bWxldC5pby9tZWRp/YS9jYXRhbG9nL3By/b2R1Y3QvYy9yL2Ny/ODAxN18xXy5qcGc_/b3B0aW1pemU9aGln/aCZiZy1jb2xvcj0y/NTUsMjU1LDI1NSZm/aXQ9Ym91bmRzJmhl/aWdodD0zMDAmd2lk/dGg9NDgwJmNhbnZh/cz00ODA6MzAwJnc9/NDgw', 'price': '₹4,199'},
        {'name': 'Travel Bag', 'image': 'https://imgs.search.brave.com/gkRlWfL-ZVbzVdFiB07VPzRIOzhcnpWj10jYk0LXyB0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wNjgv/NTgzLzIyMy9zbWFs/bC9hLXdlbGwtb3Jn/YW5pemVkLXRyYXZl/bC1zZXR1cC1mZWF0/dXJpbmctYS1sZWF0/aGVyLWJhZy1jYW1l/cmEtY2xvdGhlcy1h/bmQtYS1tYXAtb24t/YS13b29kZW4tc3Vy/ZmFjZS1waG90by5q/cGc', 'price': '₹2,799'},
    ]

    context = {
        'hero': hero,
        'promo_cards': promo_cards,
        'product_cards': product_cards,
        'product_section_title': 'Popular items',
    }

    return render(request, 'home/home.html', context)

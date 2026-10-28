# 🛒 ShopEase - Full-Stack E-Commerce Web Application

[![Django Version](https://img.shields.io/badge/Django-6.1%20%7C%205.x-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

> **GeeksforGeeks Reference Project**: Selected from the **[GeeksforGeeks Django Projects List](https://www.geeksforgeeks.org/python/django-projects/)** under *E-commerce Website using Django*, *E-commerce Product Catalog*, and *Cart & Checkout Systems*.

---

## 📌 1. Project Overview

**ShopEase** is a modern, production-ready, full-stack E-Commerce web platform built using **Python** and the **Django Framework**. The application follows Django's clean **MVT (Model-View-Template)** architecture and adheres to the **DRY (Don't Repeat Yourself)** software engineering principle.

### Key Functional Highlights
- 🏬 **Dynamic Product Catalog**: Browse products across hierarchical categories with pricing, discount badges, and stock indicators.
- 🔍 **Live Search, Filter & Sorter**: Multi-parameter search by keyword, category filtering, min/max price bounds, and sorting (Newest, Price: Low-to-High, High-to-Low, Alphabetical).
- 🛍️ **Hybrid Shopping Cart**: Dual-state cart supporting guest users via Django sessions and logged-in users with persistent database records. When a guest logs in, their cart automatically merges into their user account!
- 💳 **Complete Checkout & Order Management**: Atomic database transactions handle shipping address capture, unique order ID generation (`ORD-YYYYMMDD-XXXX`), line-item creation, and inventory stock deduction.
- 🧾 **Printable Order Invoices**: Clean printable invoice view with customer details and line-item totals (`window.print()` formatted CSS).
- 👤 **Customer Authentication & Dashboard**: Secure registration, login/logout, profile updates, and order history tracking.
- ⭐ **Product Reviews & Ratings**: Authenticated users can write subject titles, comments, and assign 1–5 star ratings with live average calculation.
- 🛡️ **Custom Django Admin**: Full back-office dashboard with search, tabular inline items, status filters, prepopulated slugs, and editable listings.

---

## 🏗️ 2. Architectural Design (Django MVT)

```
                            [ User Web Browser ]
                                     │
                                HTTP Request
                                     ▼
                            [ Django urls.py ]
                             (URL Dispatcher)
                                     │
                                     ▼
                            [ Django views.py ]
                             (Business Logic)
                               │           ▲
                Query / Save   │           │   Render Data
                               ▼           │
                       [ models.py (ORM) ] │
                               │           │
                       [ SQLite Database ] └─────► [ templates/ (HTML5) ]
                                                            │
                                                       HTTP Response
                                                            │
                                                            ▼
                                                    [ Browser Display ]
```

### Modular App Structure
1. **`store` App**: Handles product catalog, categories, product details, stock tracking, and user reviews.
2. **`cart` App**: Manages session-based & user-based shopping cart items, quantity increments/decrements, and tax/shipping calculations.
3. **`orders` App**: Handles order placement, inventory reduction, unique order sequence generation, and printable invoice rendering.
4. **`accounts` App**: Manages user registration with password confirmation, authentication, profile dashboard, and session-to-user cart merging.

---

## 🗄️ 3. Database Schema & Model Relationships

```
┌─────────────────┐       1:N       ┌──────────────────┐
│    Category     ├────────────────►│     Product      │
└─────────────────┘                 └────────┬─────────┘
                                             │
                       ┌─────────────────────┼─────────────────────┐
                   1:N │                 1:N │                 1:N │
                       ▼                     ▼                     ▼
               ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
               │    Review     │     │   CartItem    │     │   OrderItem   │
               └───────▲───────┘     └───────▲───────┘     └───────▲───────┘
                       │                     │                     │
                       │ N:1                 │ N:1                 │ N:1
               ┌───────┴───────┐     ┌───────┴───────┐     ┌───────┴───────┐
               │     User      │     │     Cart      │     │     Order     │
               │ (auth_user)   │     │ (Session Key) │     │ (Order ID)    │
               └───────────────┘     └───────────────┘     └───────────────┘
```

### Core Entities:
- **`Category`**: Stores name, slug, description, image, and timestamps.
- **`Product`**: Relates to `Category` (`ForeignKey`), tracks name, slug, description, price, original price, stock, availability, and image URL.
- **`Cart` & `CartItem`**: `Cart` tracks session ID. `CartItem` holds product reference, quantity, and user/cart foreign keys with subtotal computation.
- **`Order` & `OrderItem`**: `Order` stores shipping address, order total, tax, shipping fee, status, and unique tracking code. `OrderItem` stores snapshot prices and quantities tied atomically to the order.
- **`Review`**: Links `Product` and `User` with rating (1-5 stars) and review text.

---

## 🚀 4. Quick Start & Setup Guide

### Prerequisites
- Python 3.10+ installed
- Git installed (optional, for version control)

### Step 1: Clone or Open the Repository
```bash
git clone <your-repository-url>
cd ecommerce_project
```

### Step 2: Create and Activate Virtual Environment
**On Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
python manage.py migrate
```

### Step 5: Seed Rich Sample Data
Run the automated population script to create categories, 15+ products, customer reviews, superuser, and sample customer accounts:
```bash
python populate_data.py
```

### Step 6: Start the Development Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your web browser.

---

## 🔑 5. Pre-Configured Demo Credentials

| Role | Username | Password | Purpose |
| :--- | :--- | :--- | :--- |
| **Superuser / Admin** | `admin` | `admin123` | Access Django Admin Panel (`/admin/`) |
| **Customer 1** | `alex_rivers` | `password123` | Pre-existing orders & reviews |
| **Customer 2** | `sarah_connor` | `password123` | Product reviews & testing purchases |

---

## 🧪 6. Automated Unit Tests

The project includes an automated test suite verifying all critical business logic:
```bash
python manage.py test
```
**Test Coverage Includes:**
- Category creation, URL slug routing, and string representations
- Product property calculations (discount percentages, stock checks, average ratings)
- Catalog search by keyword and category filters
- Cart workflows (adding, incrementing quantity, removing, deleting items)
- Order placement, atomic inventory deduction, and cart cleanup
- Review submission and rating aggregation

---

## 📚 7. Project Viva & Examination Q&A Guide

Be prepared to answer these common questions during your project demonstration:

### Q1: What is the MVT pattern in Django, and how did you implement it?
> **Answer**: MVT stands for **Model-View-Template**:
> - **Model** (`store/models.py`, `orders/models.py`): Defines the data structures and business rules, mapped to SQLite via Django ORM.
> - **View** (`store/views.py`, `cart/views.py`): Contains the business logic, handles HTTP requests, interacts with the models, and renders templates with context dictionaries.
> - **Template** (`templates/`): Presentation layer using Django Template Language (DTL) with HTML5 and Bootstrap 5 to render dynamic data to the user.

### Q2: How does the shopping cart work for both guests and logged-in users?
> **Answer**: 
> 1. For **guests**, we use `request.session.session_key` to identify the cart. Items are saved in `CartItem` linked to a `Cart` object with that session key.
> 2. For **logged-in users**, items are linked directly to `request.user`.
> 3. **Cart Merging**: In `accounts/views.py` (`login_view`), when a guest with items in their session logs in, the system iterates over their session cart items and transfers them into their user account (`item.user = user; item.cart = None; item.save()`).

### Q3: How do you prevent overselling or race conditions during checkout?
> **Answer**: Checkout is wrapped inside `with transaction.atomic():` in `orders/views.py`. Before placing the order, the system validates `item.quantity <= item.product.stock`. If valid, it deducts the stock (`product.stock -= item.quantity`), creates `OrderItem`s, and clears the cart inside a single atomic database transaction. If any error occurs, all database changes are rolled back automatically.

### Q4: How is search and filtering implemented?
> **Answer**: In `store/views.py`:
> - Keyword search uses Django's `Q` objects: `Q(name__icontains=keyword) | Q(description__icontains=keyword)`.
> - Price filtering uses ORM field lookups: `products.filter(price__gte=min_price, price__lte=max_price)`.
> - Sorting uses `.order_by('price')` or `.order_by('-created_at')`.
> - Pagination is handled cleanly using Django's built-in `Paginator` class (6 products per page).

### Q5: What security features does the application have?
> **Answer**:
> - **CSRF Protection**: All forms include `{% csrf_token %}` to prevent Cross-Site Request Forgery.
> - **Password Hashing**: Django hashes passwords using PBKDF2 with SHA-256 algorithm and salt; passwords are never stored in plain text.
> - **SQL Injection Prevention**: Using Django's ORM parameterized queries prevents raw SQL injection.
> - **XSS Protection**: Django templates automatically escape HTML variables unless explicitly marked `|safe`.

---

## 📁 8. Repository Organization

```
ecommerce_project/
├── manage.py                   # Django CLI management script
├── populate_data.py            # Automated seed script for demo data
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules for Django
├── run.bat                     # Windows single-click run script
├── run.sh                      # Linux/macOS run script
├── README.md                   # Comprehensive documentation (this file)
│
├── ecommerce_project/          # Root project settings
│   ├── settings.py             # App configs, middleware, templates, db
│   ├── urls.py                 # Main URL routing configuration
│   ├── wsgi.py                 # WSGI production server gateway
│   └── asgi.py                 # ASGI asynchronous gateway
│
├── store/                      # Catalog & Product App
│   ├── models.py               # Category, Product, Review
│   ├── views.py                # home, store, product_detail, submit_review
│   ├── urls.py                 # Store URL patterns
│   ├── forms.py                # ReviewForm
│   ├── admin.py                # Custom ModelAdmin with search & filters
│   ├── context_processors.py   # categories_menu for navbar
│   └── tests.py                # Unit & integration tests
│
├── cart/                       # Shopping Cart App
│   ├── models.py               # Cart, CartItem
│   ├── views.py                # cart_view, add_to_cart, remove, delete
│   ├── urls.py                 # Cart URL patterns
│   ├── context_processors.py   # cart_counter badge processor
│   └── tests.py                # Cart tests
│
├── orders/                     # Order Processing & Checkout App
│   ├── models.py               # Order, OrderItem
│   ├── views.py                # checkout, place_order, order_success, history
│   ├── urls.py                 # Orders URL patterns
│   ├── forms.py                # OrderForm (Shipping address)
│   ├── admin.py                # OrderAdmin with inlines
│   └── tests.py                # Checkout tests
│
├── accounts/                   # User Authentication & Profile App
│   ├── views.py                # register, login_view, logout_view, profile
│   ├── urls.py                 # Accounts URL patterns
│   └── forms.py                # RegistrationForm, UserProfileForm
│
├── static/                     # Static styling and scripts
│   ├── css/
│   │   └── style.css           # Modern custom CSS styling
│   └── js/
│       └── main.js
│
└── templates/                  # Bootstrap 5 HTML Templates
    ├── base.html               # Master layout with navbar & footer
    ├── store/
    │   ├── home.html           # Landing page with banners & categories
    │   ├── store.html          # Catalog with filters & pagination
    │   └── product_detail.html # Detail page with reviews
    ├── cart/
    │   └── cart.html           # Shopping cart view
    ├── orders/
    │   ├── checkout.html       # Checkout & address form
    │   ├── order_success.html  # Invoice receipt
    │   ├── order_history.html  # User order history
    │   └── order_detail.html   # Detailed order view
    └── accounts/
        ├── login.html          # Sign-in form
        ├── register.html       # Registration form
        └── profile.html        # User account dashboard
```

---

## 📤 9. Uploading to GitHub

To push this project to your GitHub repository:

1. **Create a new repository on [GitHub](https://github.com/new)** (e.g. `django-ecommerce-shopease`).
2. **Initialize Git and commit**:
   ```bash
   cd ecommerce_project
   git init
   git add .
   git commit -m "Initial commit: Full-featured Django E-Commerce application with sample data and tests"
   ```
3. **Link your remote and push**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```

---

## 🏆 Credits
- Developed following the curriculum specifications of **[GeeksforGeeks Django Projects](https://www.geeksforgeeks.org/python/django-projects/)**.
- Built with Python, Django, SQLite, and Bootstrap 5.

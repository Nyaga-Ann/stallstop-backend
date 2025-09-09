🛍️ Fashion Finder & Ordering API

📖 Project Overview
This project is a **Kenyan fashion marketplace API** that helps customers **find clothes, shoes, and accessories** easily, while vendors can list their shops and manage incoming orders.

The idea came from the common struggle of browsing TikTok/Instagram for clothes where:
- Some posts **lacked prices**,
- Others **didn’t show shop locations**,
- Or it was **difficult to trace sellers**.

👉 This system solves that problem by:
- Allowing vendors to **register shops** (physical or online),
- Enabling customers to **browse items with prices and locations**,
- Supporting **favorites** (vendors & items),
- Adding an **ordering system** for online shops.

⚙️ Tech Stack
- **Backend**: Django REST Framework (DRF)
- **Database**: PostgreSQL / SQLite (development)
- **Authentication**: JWT (JSON Web Tokens)
- **Filtering & Search**: `django-filter`, DRF Search & Ordering
- **Deployment Ready**: Built with modular apps (`auth`, `vendors`, `items`, `orders`)

---
 🚀 Getting Started
 1. Clone Repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2. Setup Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Create Superuser (Admin)
python manage.py createsuperuser

6. Run Server
python manage.py runserver
Your API will now be available at:
http://127.0.0.1:8000/api/

🔑 Authentication
This project uses JWT Authentication.

Register/Login → Get JWT Token

Use it in Postman/HTTP clients as:

Authorization: Bearer <your_token>
📌 API Endpoints
Below are the stepwise endpoints to test (Customer → Vendor → Items → Orders).

1️⃣ Admin (Superuser)
Access Django Admin:
GET http://127.0.0.1:8000/admin/
Use credentials created via createsuperuser.

2️⃣ Customer Endpoints
2.1 Register (Signup)
POST http://127.0.0.1:8000/api/auth/customer/signup/

{
  "username": "Jamie_potter",
  "email": "jpotter@gmail.com",
  "password": "jpotter@12"
}
2.2 Login (Get JWT)
POST http://127.0.0.1:8000/api/auth/login/

{
  "email": "jpotter@gmail.com",
  "password": "jpotter@12"
}
✅ Copy the access token → use in headers.

2.3 Profile (Get/Update)
GET http://127.0.0.1:8000/api/auth/me/

PATCH http://127.0.0.1:8000/api/auth/me/

{
  "username": "jamie_potterW"
}
3️⃣ Vendor Endpoints
3.1 Create Vendor Profile
POST http://127.0.0.1:8000/api/vendors/

{
  "business_name": "Downtown Fashion",
  "location": "Westlands, Nairobi",
  "latitude": -1.2680,
  "longitude": 36.8110,
  "description": "Trendy fashion and accessories.",
  "contact_phone": "+254712345678",
  "shop_type": "physical",
  "whatsapp_number": "+254798765432"
}
3.2 Get Vendor Details
GET http://127.0.0.1:8000/api/vendors/1/

3.3 Update Vendor Profile
PATCH http://127.0.0.1:8000/api/vendors/1/

{
  "description": "Latest clothes, shoes and bags."
}
3.4 Favorite Vendor (as Customer)
POST http://127.0.0.1:8000/api/vendors/favorites/

{
  "vendor": 1
}
3.5 Review Vendor
POST http://127.0.0.1:8000/api/vendors/1/reviews/

{
  "rating": 5,
  "comment": "Great collection and timely delivery!"
}
4️⃣ Items Endpoints
4.1 Add Item (Vendor)
POST http://127.0.0.1:8000/api/items/
{
  "name": "Leather Handbag",
  "category": "accessories",
  "price": 3200.00,
  "description": "Elegant leather handbag perfect for office wear.",
  "image_url": "https://example.com/images/leather-handbag.jpg"
}
4.2 List Items
GET http://127.0.0.1:8000/api/items/

Supports filters:

/api/items/?category=shoes

/api/items/?search=handbag

/api/items/?ordering=price

4.3 Get Single Item
GET http://127.0.0.1:8000/api/items/1/

4.4 Update Item (Vendor)
PATCH http://127.0.0.1:8000/api/items/1/

{
  "price": 3000.00
}
4.5 Favorite Item (as Customer)
POST http://127.0.0.1:8000/api/items/favorites/

{
  "item": 1
}
5️⃣ Orders Endpoints
5.1 Create Order (Customer)
POST http://127.0.0.1:8000/api/orders/me/

{
  "vendor": 1,
  "items": [1],
  "quantity": 2,
  "note": "Please deliver by tomorrow"
}
5.2 List My Orders
GET http://127.0.0.1:8000/api/orders/me/

5.3 Get Order Detail
GET http://127.0.0.1:8000/api/orders/me/1/

5.4 Vendor Incoming Orders
GET http://127.0.0.1:8000/api/orders/vendor/

5.5 Update Order Status (Vendor)
PATCH http://127.0.0.1:8000/api/orders/1/status/

{
  "status": "shipped"
}
🛡️ Permissions
Customers: Can signup, login, favorite vendors/items, create orders, review vendors.

Vendors: Can create/update vendor profile, add/update items, manage incoming orders.

Admin: Full control via Django Admin.





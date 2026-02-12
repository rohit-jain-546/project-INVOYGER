

🧾 INVOYGER

Invoice Billing & Product Management System (Django)

Invoyger is a role-based invoice billing and product management web application built using Django.
The system provides separate workflows for administrators and customers, enabling secure authentication, product management, cart handling, and invoice-ready billing architecture.

This project follows clean multi-app Django architecture, proper role separation, and scalable backend design principles.


---

🚀 Features

🔐 Authentication & Roles

User and Admin registration

Secure login & logout using Django Auth

Role-based access control

Unauthorized route protection



---

🛠️ Admin Panel

Admin-only access

Add products

Update products

Delete products

View all products

Search products

Activate / deactivate products

Image upload support


(Planned Enhancements)

Accept orders

Reject orders

Mark orders as completed

View and download invoices

Search invoices by invoice number



---

🛒 Customer (Shop)

View available products

Product price with tax calculation

Database-based cart system

Checkout-ready architecture


(Planned Enhancements)

Invoice generation after checkout

Invoice history

Search invoices

Download invoices (PDF)



---

📄 Invoice & Billing System

Unique invoice number generation

Permanent invoice storage

Invoice item snapshot (product name, price, tax at purchase time)

Accurate tax-inclusive billing


(Upcoming)

PDF invoice generation using ReportLab

Download invoice option for both admin and customer



---

🧱 Tech Stack

Layer	Technology

Backend	Python, Django
Database	SQLite (development)
Frontend	HTML, CSS (Django Templates)
Authentication	Django Auth
Cart System	Database-based
File Handling	Django Media
Version Control	Git, GitHub



---

🗂️ Project Structure

project-invoyger/
└── authsys/
    ├── manage.py
    ├── invoyger/            # Project configuration
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── accounts/            # Authentication & roles
    ├── adminpanel/          # Admin operations
    ├── shop/                # Products, cart, invoices
    ├── templates/
    ├── static/
    ├── media/
    └── db.sqlite3


---

📦 App Responsibilities

accounts

User registration

Admin registration

Login & logout

Role verification


Models

Customer

AdminUser



---

👨🏻‍💼adminpanel

Product CRUD operations

Product search

Product activation control

Admin-only route protection



---

🛍️shop

Product display for users

Database-based cart

Invoice & invoice items

Billing logic


Models

Product

Cart

CartItem

Invoice

InvoiceItem



---

🧮 Database Design Highlights

Product

Name

Description

Price

Tax percentage

Stock

Active status

Image



---

🛒Cart (Database-Based)

One cart per user

Persistent until checkout

Supports quantity updates

Cleared after invoice generation



---

🧾Invoice

Auto-generated unique invoice number

Linked to user

Immutable billing record

Stores total amount



---

🧾InvoiceItem

Stores product snapshot

Preserves billing accuracy even if product data changes later



---

🔒 Security & Best Practices

Django authentication system

Role-based access decorators

Secure session handling

No sensitive data stored in sessions

Clean app separation

Warning-free configuration



---

🧪 Current Project Status

✅ Completed

Multi-app Django refactor

Authentication system

Admin product CRUD

Role-based access control

Product listing

Cart & invoice database design

Media & static file handling

Git version control with clean commits



---

🔜 Planned Features

Checkout workflow

Invoice creation from cart

PDF invoice generation (ReportLab)

Invoice search (Admin & Customer)

Invoice download

Admin order lifecycle management

Accept

Reject

Complete orders


Deployment-ready configuration



---

📚 Learning Outcomes

Django multi-app architecture

Secure authentication & authorization

Database modeling for billing systems

Cart & invoice design

Backend scalability concepts

Git & GitHub workflow

Debugging and refactoring skills



---

📌 Conclusion

Invoyger is a structured Django project that demonstrates real-world backend concepts, including authentication, role-based access, product management, and invoice billing system design.
The project is scalable, maintainable, and ready for advanced features like PDF billing and order management.


---

🧑‍💻 Author

Rohit Jain

Linked in- https://www.linkedin.com/in/546-rohit-jain 

Aspiring Backend / Full-Stack Developer

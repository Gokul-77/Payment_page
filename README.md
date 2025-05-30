  README.md
# 💳 Payment Page

A secure and responsive payment form built using **Django** and **Tailwind CSS**. This project collects and stores payment-related details such as card information, billing address, and user contact info securely in a PostgreSQL database. It includes frontend validation and admin panel access via Django's built-in admin interface.

## 🚀 Features

- Secure payment form with CSRF protection  
- Tailwind CSS for a modern and responsive UI  
- Card brand detection (Visa, MasterCard, RuPay, Amex)  
- Validation for card number, expiry date, and CVV  
- Stores user input to PostgreSQL via Django models  
- Admin interface to view submitted payment data  

## 🛠️ Tech Stack

- **Backend:** Django  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **Database:** PostgreSQL  

## 📁 Project Structure

\`\`\`
project/
├── student_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── templates/
│   └── payment.html
├── student_details/
│   └── settings.py
\`\`\`

## ⚙️ Setup Instructions

1. Clone the repo:
\`\`\`bash
git clone https://github.com/Gokul-77/Payment_page.git
cd Payment_page
\`\`\`

2. Create and activate a virtual environment:
\`\`\`bash
python -m venv env
source env/bin/activate  # On Windows: env\\Scripts\\activate
\`\`\`

3. Install requirements (if you have a requirements.txt):
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Run migrations and start the server:
\`\`\`bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
\`\`\`

5. Visit \`http://127.0.0.1:8000/\` to test the payment page.

## 📌 Future Enhancements

- Add real-time payment gateway integration (e.g., Stripe, Razorpay)  
- User authentication and login  
- Responsive error messages and success confirmation  
- Deploy the project online (e.g., Render, Heroku, Vercel)  


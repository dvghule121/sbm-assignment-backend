# 💰 Expense Tracker - Django REST API (Social Booster Media Assignment)


## 📂 Project Structure

```
expense_tracker/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── expense_tracker/        # Project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── expenses/               # Main app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── auth_views.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── tests.py
```

## 🛠 API Endpoints

### CRUD Operations

| Method | Endpoint              | Description              |
| ------ | --------------------- | ------------------------ |
| GET    | `/api/expenses/`      | List user's expenses     |
| POST   | `/api/expenses/`      | Create new expense       |
| GET    | `/api/expenses/<id>/` | Retrieve expense details |
| PUT    | `/api/expenses/<id>/` | Update expense           |
| DELETE | `/api/expenses/<id>/` | Delete expense           |

### Special Endpoints

| Method | Endpoint                     | Description                           |
| ------ | ---------------------------- | ------------------------------------- |
| GET    | `/api/expenses/summary/`     | Get user's expense summary by category |

### API Response Examples

**Expense List/Detail:**
```json
{
  "id": 1,
  "user": "john_doe",
  "title": "Lunch at restaurant",
  "amount": "500.00",
  "category": "Food",
  "date": "2024-01-15",
  "description": "Team lunch",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

**Summary Report:**
```json
[
  {
    "category": "Food",
    "total_amount": "1200.00",
    "count": 5
  },
  {
    "category": "Transport",
    "total_amount": "800.00",
    "count": 3
  }
]
```

## 🔧 Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL (or use SQLite for development)
- pip (Python package manager)

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd expense-tracker-sbm

# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Configuration

**For PostgreSQL (Recommended for production):**

1. Create a PostgreSQL database:
```sql
CREATE DATABASE expense_tracker_db;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE expense_tracker_db TO postgres;
```

2. Update `expense_tracker/settings.py` with your database credentials: .env file recommended
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME'),
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "HOST": os.getenv('DB_HOST'),
        "PORT": os.getenv('DB_PORT'),
    }
}
```

### 3. Run Migrations

```bash
# Create and apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Create superuser for admin access
python3 manage.py createsuperuser
```

### 4. Start Development Server

```bash
python3 manage.py runserver
```

The application will be available at:
- **API**: http://127.0.0.1:8000/api/expenses/
- **Admin**: http://127.0.0.1:8000/admin/

## 📊 Using the Application

### 1. Adding Expenses via API

```bash
# Create a new expense
curl -X POST http://127.0.0.1:8000/api/expenses/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Grocery Shopping",
    "amount": 1500.00,
    "category": "Food",
    "date": "2024-01-15",
    "description": "Weekly groceries"
  }'
```

### 2. View Summary Reports

```bash
# Get expense summary by category
curl http://127.0.0.1:8000/api/expenses/summary/ \
  -H "Authorization: Bearer <your-token>"
```

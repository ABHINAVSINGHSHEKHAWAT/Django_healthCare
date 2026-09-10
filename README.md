# Healthcare Backend API

A secure RESTful backend for a healthcare application built with Django, Django REST Framework, JWT authentication, and PostgreSQL.

The API provides user authentication, patient management, doctor management, and patient-doctor relationship management with authentication, authorization, validation, and secure database access.

---

## 🚀 Features

- User registration and JWT authentication
- Secure login using JSON Web Tokens
- Patient CRUD operations
- Doctor CRUD operations
- Patient-doctor mapping management
- Patient ownership and access control
- Authentication-protected APIs
- Request data validation
- Duplicate patient-doctor mapping prevention
- PostgreSQL database integration
- Django ORM for database operations
- Environment-based configuration
- RESTful API architecture
- Proper HTTP status codes and error responses

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web framework |
| Django REST Framework | REST API development |
| PostgreSQL | Relational database |
| Simple JWT | JWT authentication |
| Django ORM | Database interaction |
| python-dotenv | Environment variable management |

---

## 📁 Project Structure

```text
healthcare-backend/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── patients/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── doctors/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── mappings/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

> `.env` is intentionally excluded from version control because it contains sensitive configuration.

---

## 🔐 Authentication

The application uses JWT (JSON Web Token) authentication.

Users can:

1. Register an account.
2. Login using their email and password.
3. Receive an access token.
4. Use the token to access protected APIs.

Protected requests require the following HTTP header:

```text
Authorization: Bearer <access_token>
```

---

# 📌 API Documentation

## Authentication APIs

### Register User

**POST**

```text
/api/auth/register/
```

Example request:

```json
{
    "name": "Abhinav",
    "email": "abhinav@example.com",
    "password": "SecurePassword123"
}
```

---

### Login

**POST**

```text
/api/auth/login/
```

Example request:

```json
{
    "email": "abhinav@example.com",
    "password": "SecurePassword123"
}
```

The API returns JWT tokens that can be used to access protected endpoints.

---

# 👤 Patient APIs

All patient endpoints require authentication.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | Get authenticated user's patients |
| GET | `/api/patients/<id>/` | Get patient details |
| PUT | `/api/patients/<id>/` | Update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

### Patient Data

A patient contains:

- Name
- Age
- Gender
- Phone
- Address
- Creation timestamp
- Update timestamp

Patients are associated with the authenticated user who created them.

---

# 👨‍⚕️ Doctor APIs

All doctor endpoints require authentication.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | Get all doctors |
| GET | `/api/doctors/<id>/` | Get doctor details |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

### Doctor Data

A doctor contains:

- Name
- Specialization
- Phone
- Email
- Creation timestamp
- Update timestamp

---

# 🔗 Patient-Doctor Mapping APIs

Mappings establish a relationship between patients and doctors.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | Get mappings |
| GET | `/api/mappings/<patient_id>/` | Get doctors assigned to a patient |
| DELETE | `/api/mappings/detail/<id>/` | Delete a mapping |

### Example

To assign Doctor `2` to Patient `2`:

```json
{
    "patient": 2,
    "doctor": 2
}
```

The API prevents the same doctor from being assigned to the same patient more than once.

---

# ✅ Validation

The API implements request validation using Django REST Framework serializers.

### Patient validation

- Age must be greater than `0`
- Age cannot exceed `120`
- Gender must be `Male`, `Female`, or `Other`
- Phone number must contain exactly `10` digits

### Doctor validation

- Phone number must contain exactly `10` digits

### Mapping validation

- A doctor cannot be assigned to the same patient multiple times
- Database-level unique constraint prevents duplicate relationships

---

# 🔒 Security

Security is an important part of the application.

### JWT Authentication

Protected APIs require a valid JWT access token.

### Patient Ownership

Users can only access and manage patients that they created.

### Mapping Ownership

Users can only create or delete mappings associated with their own patients.

### Environment Variables

Sensitive database configuration is stored in `.env` rather than directly in the source code.

### Password Security

Passwords are securely hashed using Django's authentication system rather than being stored as plain text.

---

# 🗄️ Database

The project uses PostgreSQL as its relational database.

Django ORM is used for database operations.

### Main database entities

```text
User
 │
 └── Patient
       │
       └── PatientDoctorMapping
                    │
                    └── Doctor
```

The patient-doctor relationship is implemented using a dedicated mapping model.

A database-level unique constraint ensures that the same patient-doctor relationship cannot be created twice.

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/ABHINAVSINGHSHEKHAWAT/Django_healthCare.git
```

Navigate into the project:

```bash
cd Django_healthCare
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=localhost
DB_PORT=5432
```

Replace the database credentials with your local PostgreSQL configuration.

> Never commit the `.env` file to GitHub.

---

## 5. Create the database

Create a PostgreSQL database named:

```text
healthcare_db
```

Make sure PostgreSQL is running before starting Django.

---

## 6. Run migrations

```powershell
python manage.py migrate
```

---

## 7. Start the development server

```powershell
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🧪 Testing

The API can be tested using:

- Postman
- PowerShell
- Any REST API client

### Recommended testing flow

```text
1. Register user
       ↓
2. Login
       ↓
3. Obtain JWT access token
       ↓
4. Add Authorization header
       ↓
5. Create patient
       ↓
6. Create doctor
       ↓
7. Create patient-doctor mapping
       ↓
8. Test GET / PUT / DELETE operations
       ↓
9. Test validation and authentication
```

Example authorization header:

```text
Authorization: Bearer <access_token>
```

---

# 📋 API Security Testing

The API rejects requests to protected endpoints when no authentication credentials are provided.

Example:

```text
GET /api/patients/
```

Without a JWT:

```json
{
    "detail": "Authentication credentials were not provided."
}
```

This confirms that protected resources require authentication.

---

# 📦 Dependencies

Project dependencies are maintained in:

```text
requirements.txt
```

Install them with:

```powershell
pip install -r requirements.txt
```

---

# 🚧 Future Improvements

Potential improvements for future versions include:

- API documentation using Swagger/OpenAPI
- Refresh token rotation
- Pagination
- Search and filtering
- More granular permissions
- Automated unit and integration tests
- Production deployment configuration
- Docker support
- CI/CD pipeline

---

# 👨‍💻 Author

**Abhinav Singh Shekhawat**

GitHub:

https://github.com/ABHINAVSINGHSHEKHAWAT

---

## 📄 License

This project was developed as a healthcare backend development assignment.

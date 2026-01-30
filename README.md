# Auth0 Demo — Flask Backend + React Frontend

This repository demonstrates how to integrate **Auth0 Authentication** with a
**React frontend** and a **Flask backend** using **JWT Access Tokens**.

---

## 📁 Project Structure

```
AUTH0/
│
├── Flask_backend_auth0/
│ ├── app.py
│ └── venv/
│
├── React_frotend_auth0/
│ ├── src/
│ │ ├── components/
│ │ │ ├── LoginButton.jsx
│ │ │ ├── LogoutButton.jsx
│ │ │ ├── Profile.jsx
│ │ │ ├── SendRequest.jsx
│ │ ├── App.jsx
│ │ └── main.jsx
│ └── README.md
│
└── README.md

```

---

## 🔐 Authentication Flow

1. User clicks **Login** in React
2. Auth0 authenticates the user
3. Auth0 returns a **JWT Access Token**
4. React sends token to Flask in request headers
5. Flask verifies token using Auth0 **JWKS**
6. Protected data is returned

---

## 🚀 How to Run

### Backend

cd Flask_backend_auth0
python app.py

### Frontend

cd React_frotend_auth0
npm install
npm run dev

Frontend → http://localhost:3000  
Backend → http://localhost:5000

---

## ✅ Technologies Used

- React + Vite
- Flask (Python)
- Auth0
- JWT (RS256)
- Flask-CORS
- python-jose

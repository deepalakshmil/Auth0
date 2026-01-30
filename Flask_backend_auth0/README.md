# Flask Backend — Auth0 JWT Verification

This Flask backend verifies **Auth0 JWT Access Tokens** using RS256 encryption.
All authentication logic is implemented in a **single file (`app.py`)**.

---

## 📁 File Overview

| File   | Description                        |
| ------ | ---------------------------------- |
| app.py | Flask app + Auth0 JWT verification |

---

## 📦 Install Requirements

pip install flask python-jose flask-cors

---

## 🔐 Auth0 Configuration (Inside app.py)

- AUTH0_DOMAIN
- API_IDENTIFIER
- ALGORITHMS = ["RS256"]

---

## 🔎 How Token Verification Works

1. Flask receives token from Authorization header
2. Fetches JWKS from Auth0
3. Matches `kid`
4. Verifies signature, audience, issuer
5. Allows or rejects request

---

## 🔒 Protected Route

GET /protected

Requires:
Authorization: Bearer <JWT>

---

## ▶ Run Backend

python app.py

Backend runs at:
http://localhost:5000

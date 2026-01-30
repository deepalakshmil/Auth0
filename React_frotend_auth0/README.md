# React Frontend — Auth0 Authentication

This React application handles user authentication using **Auth0** and sends
secure JWT access tokens to a Flask backend.

---

## 📁 Components

| File             | Description                   |
| ---------------- | ----------------------------- |
| LoginButton.jsx  | Redirects user to Auth0 login |
| LogoutButton.jsx | Logs the user out             |
| Profile.jsx      | Displays user profile data    |
| SendRequest.jsx  | Sends JWT to Flask backend    |

---

## 🔐 Auth0 Setup

Create an Auth0 **Single Page Application** and set:

- Allowed Callback URLs  
  http://localhost:3000

- Allowed Logout URLs  
  http://localhost:3000

- Allowed Web Origins  
  http://localhost:3000

---

## ⚙ Environment Variables (.env)

VITE_AUTH0_DOMAIN=your-domain.auth0.com
VITE_AUTH0_CLIENT_ID=your-client-id
VITE_AUTH0_AUDIENCE=your-api-identifier

---

## ▶ Run Frontend

npm install
npm run dev

App runs on:
http://localhost:3000

---

## 🔗 Calling the Backend

The `SendRequest.jsx` component sends the token as:

Authorization: Bearer <ACCESS_TOKEN>

If the token is valid, Flask returns protected data.

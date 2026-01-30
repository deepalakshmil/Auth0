<<<<<<< HEAD
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
=======
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
>>>>>>> auth0-fix

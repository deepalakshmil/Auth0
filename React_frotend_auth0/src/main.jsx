import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import { Auth0Provider } from "@auth0/auth0-react";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Auth0Provider
      domain="dev-qu6otuqqqbbpnzih.us.auth0.com"
      clientId="ONeU2LZUjda98slHnEU5z0UES1TgtPVT"
      authorizationParams={{
        redirect_uri: window.location.origin,
        audience: "this-is-my-super-awesome-project-api", // 👈 backend API identifier (or)  matches your Flask Auth0 API
        scope: "read:user",
      }}
    >
      <App />
    </Auth0Provider>
  </StrictMode>
);

// SendRequest.tsx
import { useAuth0 } from "@auth0/auth0-react";

const SendRequest = () => {
  const { getAccessTokenSilently } = useAuth0();

  const fetchProtectedData = async () => {
    const token = await getAccessTokenSilently(); // 🪪 get access token from Auth0
    console.log("Token:", token);
    const response = await fetch("http://127.0.0.1:5000/protected", {
      headers: {
        Authorization: `Bearer ${token}`, // 🛡 send token to Flask
      },
    });
    const data = await response.json();
    console.log("RESPONSE:", data);
  };

  return <button onClick={() => fetchProtectedData()}>SendRequest</button>;
};

export default SendRequest;

//This is perfect for testing communication with your Flask backend’s protected route.

/*
How It Works

Auth0 SDK (useAuth0) silently gets an access token for the current logged-in user.

You send the token in your API request headers:

Authorization: Bearer <token>


Flask backend verifies this token using Auth0’s public keys (JWKS).

If valid → returns protected data.

If invalid → returns 401 (Unauthorized).
*/

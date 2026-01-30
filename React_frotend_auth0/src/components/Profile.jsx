//Show logged-in user info (name, email, picture):

// profile.jsx
import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

const Profile = () => {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <p>Loading...</p>;
  }

  return (
    isAuthenticated && (
      <div style={{ textAlign: "center" }}>
        <img
          src={user.picture}
          alt={user.name}
          width="80"
          style={{ borderRadius: "50%" }}
        />
        <h2>{user.name}</h2>
        <p>{user.email}</p>
      </div>
    )
  );
};

export default Profile;

/*
✅ How it works:

Displays the user profile only if logged in.

Automatically gets user info from Auth0.
*/

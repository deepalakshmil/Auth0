// import React from "react";
// import { useAuth0 } from "@auth0/auth0-react";
import LoginButton from "./components/LoginButton";
import LogoutButton from "./components/LogoutButton";
import Profile from "./components/Profile";
import SendRequest from "./components/SendRequest";

function App() {
  // const { isAuthenticated } = useAuth0();

  return (
    <div>
      {/* This is also working */}
      {/* {!isAuthenticated ? (
        <LoginButton />
      ) : (
        <>
          <LogoutButton />
          <Profile />
          <SendRequest /> {/* this will call your Flask backend 
        </>
      )}*/}
      <LoginButton />
      <LogoutButton />
      <Profile />
      <SendRequest />
    </div>
  );
}

export default App;
// React side done! It logs in via Auth0 and can fetch a token to call your Flask API.
/*
This structure:

Shows Login button if logged out

Shows Logout, Profile, and SendRequest when logged in
*/

/*
✅ Summary
File	Purpose
login.jsx	Auth0 login button
logout.jsx	Auth0 logout button
profile.jsx	Shows logged-in user info
sendRequest.jsx	Calls Flask /protected API with token
App.jsx	Combines them logically
Flask /protected route	Validates token and returns secure data
*/

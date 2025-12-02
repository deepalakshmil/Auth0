import { useAuth0 } from "@auth0/auth0-react";

const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();

  return <button onClick={() => loginWithRedirect()}>Log In</button>;
};

export default LoginButton;

/*
✅ How it works:

When clicked, it redirects the user to Auth0’s login page.

After login, the user is redirected back to your app.
*/

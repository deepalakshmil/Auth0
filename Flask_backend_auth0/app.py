'''

Decrypting Auth0 Tokens in our Backend
For this demonstration I'm going to create a very basic Single Page backend that will include:
• Flask App instantiation
• @token_required function decorator
• verify_token() function
• Single protected route.

Flask App Set up
In VS Code Terminal

• Create your virtual environment
##windows
python -m venv venv

##Mac
python3 -m venv venv
• Activate venv
##windows
venv\Scripts\activate

##Mac
source venv/bin/activate

• Install Requirements
pip install flask python-jose flask-cors


'''
# Instantiating Flask App and adding Auth0 config


from flask import Flask, jsonify, request
from flask_cors import CORS
from jose import jwt
from urllib.request import urlopen
import json

app = Flask(__name__)
<<<<<<< HEAD
CORS(app)
=======
#CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})
>>>>>>> auth0-fix

# Auth0 configuration
AUTH0_DOMAIN = "dev-qu6otuqqqbbpnzih.us.auth0.com" #The same domain used in your Front-end
API_IDENTIFIER = "this-is-my-super-awesome-project-api" #The same as the audience for your Fron-end 
ALGORITHMS = ["RS256"] #Encoding Algorithm that was set in the API creation.

'''
• CORS: Cross Origin Resource Sharing, this will allow us to communicate with our Front-end
• jose: JSON Object Signing Encryption; Which is designed to decrypt tokens signed with algorithms like RS256.
• AUTH0_DOMAIN: Can be found in the Auth0 Application interface for the front-end app
• API_IDENTIFIER: Can be found in the Auth0 API interface, this value should be the same as the audience that was set in the <Auth0Provider> component in the react app.
• ALGORITHMS: The RS256 algorith is being used to encode our Auth0 tokens and required to decode the tokens.

'''

#Creating verify_token() to decrypt our Tokens.
##Previous code, However this function needs to be defined before token_required

# Function to verify the JWT
def verify_token(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json") # 1.Fetch JWKS from Auth0
    jwks = json.loads(jsonurl.read())
     
    unverified_header = jwt.get_unverified_header(token) # 2. Extract the key that matches the JWT's 'kid'

    rsa_key = {}

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"], # Key type (usually RSA)' 
                "kid": key["kid"],  # Key ID (matches the one in your JWT header)'
                "use": key["use"], # Usage (signature)'
                "n": key["n"], # n and e: Parts of the public key'
                "e": key["e"],
            }
            
# 3️. Verify the token
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key, # Public key from Auth0
                algorithms=ALGORITHMS,
                audience=API_IDENTIFIER,
                issuer=f"https://{AUTH0_DOMAIN}/",
            )
            print('PAYLOAD:', payload)
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token is expired.")
        except jwt.JWTClaimsError:
            raise ValueError("Incorrect claims. Check the audience and issuer.")
        except Exception:
            raise ValueError("Unable to parse authentication token.")
    raise ValueError("No matching RSA key.")

'''
Explanation:
Fetch JWKS (JSON Web Key Set):
• Retrieves the public JSON Web Key Set from Auth0 by making an HTTPS request to https://{AUTH0_DOMAIN}/.well-known/jwks.json.
• These keys are used to verify the authenticity of the token's signature.
Decode the Token Header:
• Extracts the unverified header from the JWT using jwt.get_unverified_header(token).
• This step helps identify the key ID (kid) that matches the token.
Find the Matching RSA Key:
• Loops through the keys in the JWKS to find the one whose kid matches the kid in the unverified token header.
• Constructs an rsa_key dictionary with key details (kty, kid, use, n, e) if a match is found.
Verify and Decode the Token:
• If an rsa_key is found:
• Calls jwt.decode to validate the token's signature and decode its payload.
• The jwt.decode function checks:
• The token’s algorithm (via algorithms).
• The intended audience (audience).
• The issuer (issuer), which must match the expected Auth0 domain.
• If successful, the payload (claims) is returned.

Error Handling:
• ExpiredSignatureError: Raised if the token is expired.
• JWTClaimsError: Raised if the claims (audience or issuer) are invalid.
• Generic Exception: Catches any other errors while parsing the token.

'''

#Creating the @token_required Function Decorator
    ## This decorator can be applied to all routes we wish to protect with token authentication

#Middleware to protect routes

def token_required(f):
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization", None)
        if not auth:
            return jsonify({"message": "Authorization header is missing"}), 401
        
        if "Bearer" not in auth:
            return jsonify({"message": "Bearer <Token> requied"}), 401 
   
        try:
     	    #Authorization: "Bearer <token>"
            token = auth.split()[1]
            print("tokenbackend",token)
            payload = verify_token(token) #Sending token to be decrypted
        except ValueError as e:
             return jsonify({"message": str(e)}), 401

        return f(payload, *args, **kwargs)

    return decorated

'''
Explanation:
• token_required(f) is the decorator that takes in a function that will be ran after our decorator executes
• decorated(*args, **kwargs) contains the code that runs before calling the function the decorator is being applied to.
• auth = request.headers.get("Authorization", None) attempts to grab the Authorization value from the headers of the request.
• If no value is returned, we response with {"message": "Authorization header is missing"}
• If we do get a value we'll split the "Bearer <token>" string and grab just the token
• We will then pass the token to a helper function to be decrypted
If that route returns data correctly when called with a valid token — your SendRequest button will log it in the console 🎉.

'''

#Creating a Protected Route
#We're now going the create a route and user our @token_required decorator to require a token 

# Protected route example:

@app.route("/protected", methods=["GET"])
@token_required
def protected(payload):
    return jsonify({"message": "You accessed a protected route!", "user": payload})

#this should be at the bottom of the page always
if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    # app.run(debug=True)
    app.run(host="127.0.0.1", port=5000, debug=True)
>>>>>>> auth0-fix




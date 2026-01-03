## Unsigned JWT
### Challenge: Forge an essentially unsigned JWT token that impersonates the (non-existing) user jwtn3d@juice-sh.op.

1. Log in as any user.
2. Copy the JWT token from the Authorization header.
3. Decode the JWT token.
4. Under the `payload` property, change the `email` attribute in the JSON to `jwtn3d@juice-sh.op`.
5. Under the `header` property, change the value of the `alg` property from `RS256` to `none`.
6. Encode the JWT token.
7. Change the Authorization header of a subsequent request to the new JWT token.
8. Submit the request to solve this challenge.

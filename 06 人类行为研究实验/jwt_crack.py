# Author: Xzonn
# Date: 2021-05-23

import jwt
print(jwt.encode({"identity":"teacher"}, "", algorithm="HS256"))
import hashlib
from typing import Optional

from starlette.requests import Request
from starlette.responses import Response

auth_key = 'pypi_account'  # the key-value pair in the browser storage


def set_auth(res: Response, user_id: int) -> None:
    digest = __hash_text(str(user_id))
    value = f'{user_id}:{digest}'
    # set secure True for ssl connection
    # It's never sent with unsecured HTTP (except on localhost)
    # A cookie with the HttpOnly attribute is inaccessible to the JavaScript Document.cookie API; it's only sent to the server on each request
    # For example, cookies that persist in server-side sessions don't need to be available to JavaScript and should have the HttpOnly attribute. This precaution helps mitigate cross-site scripting (XSS) attacks.
    res.set_cookie(auth_key, value, secure=True, httponly=True)


# should be jwt library instead of this crap
def __hash_text(text: str) -> str:
    text = 'salty_' + text + '_text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_id_from_auth_cookie(req: Request) -> Optional[int]:
    if auth_key not in req.cookies:
        return None
    value = req.cookies[auth_key]
    if len(value.split(':')) != 2:
        return None
    user_id, digest = value.split(':')
    if __hash_text(user_id) != digest:
        print('Warning: Hash mismatch, invalid cookie value')
        return None

    return int(user_id)


def logout(response:Response)->None:
    response.delete_cookie(auth_key)
import hashlib

USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
STRING = 'function(d){var r = M(V(Y(X(d),8*d.length)));return r.toLowerCase()};function M(d){for(var _,m="0123456789ABCDEF",f="",r=0;r<d.length;r++)_=d.charCodeAt(r)'
HEADERS = {
    "authority": "apidisplaypurposes.com",
    "user-agent": USERAGENT,
    "dnt": "1",
    "api-token": None,
    "accept": "*/*",
    "origin": "https://displaypurposes.com",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://displaypurposes.com/",
    "accept-language": "en-US,en;q=0.9",
}


def generate_token(hashtag: str) -> str:
    """Generates the required 'api-token' to send request to DisplayPurposes.

    Args:
        tag: Hashtag to generate token for.

    Returns:
        dict: Dictionary representation of the request headers.
    """
    value = "{}|{}|{}".format(USERAGENT, hashtag, STRING).encode("utf-8")
    md5 = hashlib.md5(value)
    return md5.hexdigest()


def generate_header(hashtag: str = None) -> dict:
    """Generates specific headers that DisplayPurposes requires.

    Args:
        tag: Hashtag to generate headers for.

    Returns:
        dict: Dictionary representation of the request headers.

    Note:
        'map' request does not use a generated 'api-token'
        header, and instead uses the string "test".
    """
    headers = HEADERS.copy()

    if hashtag:
        headers["api-token"] = generate_token(hashtag)
    else:
        headers["api-token"] = "test"

    return headers

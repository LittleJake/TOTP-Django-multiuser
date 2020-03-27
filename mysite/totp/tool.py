import pyotp, qrcode, io, base64, random, hashlib, json


def create_token():
    return pyotp.random_base32()


def make_qr_base64(content):
    img = qrcode.make(content)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    image_stream = buf.getvalue()
    heximage = base64.b64encode(image_stream)
    return 'data:image/png;base64,' + heximage.decode()


def check(token, code):
    return 1 if pyotp.totp.TOTP(token).verify(code) else 0


def gen_uri(token, name = 'test', issuer_name = "LittleJake"):
    return pyotp.totp.TOTP(token).provisioning_uri(name, issuer_name=issuer_name)


def rand_str(n = 64):
    s = "ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789"
    s1 = ''
    for i in range(0,n):
        s1 += s[random.randint(0, len(s) - 1)]

    return s1


def check_sum(data, secret):
    d = data.copy()
    d['secret'] = secret
    return hashlib.sha256(json.dumps(d).encode("utf8")).hexdigest()
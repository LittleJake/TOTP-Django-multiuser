import pyotp, qrcode, io, base64, random


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
    return pyotp.totp.TOTP(token).verify(code)


def gen_uri(token, name = 'test', issuer_name = "LittleJake"):
    return pyotp.totp.TOTP(token).provisioning_uri(name, issuer_name=issuer_name)


def rand_str(n = 32):
    s = "ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789"
    s1 = ''
    for i in range(0,n):
        s1 += s[random.randint(0, len(s) - 1)]

    return s1
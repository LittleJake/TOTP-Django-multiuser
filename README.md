# TOTP-Django-multiuser
Cloud based TOTP Authentication checker.

## Feature
1. Mitigate hardware(IOT) workloads.
2. SHA256 checksum enable.

## Requirements 

Python 3.x, Django >3.0.4, MySQL >5.7

## Installation
### Install Utils
``` bash
pip install django qrcode pyotp
git clone https://github.com/LittleJake/TOTP-Django-multiuser.git totp
```

**(Production) Turn off Debug Mode in `totp/TOTP/settings.py` Line 26.**

**Change MySQL setting in `totp/TOTP/settings.py` Line 76.**


### Migration
``` bash
cd totp/
python manage.py migrate
```

### Run Server
``` bash
python manage.py runserver.py 0.0.0.0:80
```
## How to Use
### Create User

GET `http://YOUR-URL/api/create`



**Response**

HTML



QR code、Secret Key、User ID、Base32 Token、Client IP



**Notice**

User can be created only once per Client IP.



### Check Code

GET `http://YOUR-URL/api/check`

**Query String**

| Query String | Description                         | Example |
| ------------ | :---------------------------------- | :------ |
| user         | User ID                             | 1       |
| code         | Code shows in the Authenticator APP | 123456  |

**Response**

JSON

``` json
{
    "code": 1,
    "msg": "OK",
    "data": {
        "pass": 0,
        "time": 1585297157
    },
    "integrity": "26dff70923f5cdb3c495a89c2a1a15cdf657c528e46bcb89f507e81d44f5b58c"
}
```

| Key       | Description                                             | Example                                   |
| --------- | ------------------------------------------------------- | ----------------------------------------- |
| code      | Response code                                           | 1                                         |
| msg       | Message for response                                    | OK                                        |
| data      | JSON Object. pass: 1-valid, 0-invalid. time: timestamp. | {"pass": 0,"time":1585297157}             |
| integrity | Checksum                                                | 26dff70923f5cdb3c495a8......7e81d44f5b58c |



### Checksum

JSON Object data and your secret key to JSON String with alphabetic order. Then use Hash256 to encrypt the output.

**Example**

```json
{"pass":0,"time":1585297157,"secret":"A40OHVICNET2C16R1GKU1193WH5O53B9USN0B2B5WNUROK593ZQBFVKLJVE0DTM1"}
```

**SHA-256 Output**

```
26dff70923f5cdb3c495a89c2a1a15cdf657c528e46bcb89f507e81d44f5b58c
```


## Utils

1. qrcode (https://github.com/lincolnloop/python-qrcode)
2. pyotp (https://github.com/pyauth/pyotp)


## License

[Apache2.0](LICENSE)


## Other

[中文README](README.CN.md)

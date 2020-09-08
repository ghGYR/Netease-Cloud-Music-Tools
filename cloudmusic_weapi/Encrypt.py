import base64
import binascii
import json
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import urllib.parse
# AES参数
# 随机产生16个字符长度的字符串密钥
secKey = 'a' * 16
# RSA参数(网易云的公钥)
pubKey = '010001'
modulus = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b7251\
52b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c\
93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b\
97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
key = '0CoJUm6Qyw8W8jud'


# 对明文AES加密
def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey.encode("utf-8"), AES.MODE_CBC, '0102030405060708'.encode("utf-8"))
    ciphertext = encryptor.encrypt(text.encode("utf-8"))
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext.decode("ascii")

# 对钥匙加密
def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    text = binascii.b2a_hex(text.encode('utf-8')).decode('ascii')
    i_text = int(text, 16)
    i_pubKey = int(pubKey, 16)
    i_modulus = int(modulus, 16)
    rs = (i_text**i_pubKey) % i_modulus
    return format(rs, 'x').zfill(256)


def Encrypt_post(dict_text):
    # 转换为json字串
    text = json.dumps(dict_text)
    #用客端钥加密信息(d对称加密）)
    encText = aesEncrypt(aesEncrypt(text, key), secKey)
    #用服端公钥加密客端私匙（非对称加密）
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {
        "params": encText,
        "encSecKey": encSecKey
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    return data

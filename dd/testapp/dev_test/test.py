from Cryptodome.Cipher import AES
import base64
import re
import time
from datetime import datetime
print(time.strftime('%Y-%m-%d %H:%M:%S'))
now = datetime.now()
a = now.strftime('%Y-%m-%d %H:%M:%S')
print(type(a), a)





class Encrypt:
    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')

    def pkcs7padding(self, text):
        """明文使用PKCS7填充 """
        bs = 16
        length = len(text)
        bytes_length = len(text.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        self.coding = chr(padding)
        return text + padding_text

    def aes_encrypt(self, content):
        """ AES加密 """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 处理明文
        content_padding = self.pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result

    def aes_decrypt(self, content):
        """AES解密 """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content = base64.b64decode(content)
        text = cipher.decrypt(content)
        return text.decode('utf-8').rstrip("\x04")


if __name__ == '__main__':
    key = 'JXU5NkM2JXU1NkUyJXU4RkQw'
    iv = '1234567812345678'
    p_json = '4vQ1xetAoRorheOkx+L8sDlKkja7NKnQmlKErcwj/ZupMn0Cejkk+WdyIe6Fxl5XH8C1eNzSSUPr2nM1RfGM3sfHI1ie2jfRdtDS9I+plv/LGPeaDmtq9uORfJnBW5GRUZqSTNajKSSfdLoR87vBMgYUM2IfikOF6/OeAMki/wPquYnvDyAwTAsyLaewvgNl4LnvW8Rr7QVK1rIRZL6mg8S4GdJVgXPqtkvcvfax6MoDdQN4SHAswhjcrpgFAaBKxon0zyCsnu9rdFcPCVrEgNaMKrMLLnvZ8/YOaVqgPH3P8m2DPxjq8Jrh2w5PB2KlASeqZApkW5nupogzdDrowhs8LLLzW//9cuRJkZXQBSs='
    a = Encrypt(key=key, iv=iv)
    # e = a.aes_encrypt(p_json)  # 加密
    d = a.aes_decrypt(p_json.encode())  # 解密
    print(d)

    try:
        pass
    except Exception as e:
        pass
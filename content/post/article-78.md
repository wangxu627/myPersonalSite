
---
title: base64的纯python实现
date: 2019-11-21 15:42:11.957836
Description: ""
Tags: []
Categories: []
DisableComments: false
---

    import unittest  
    import base64  
      
    def b64encode_sp(s):  
        base64_table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";    
        b = []  
        result = []  
        step = 3  
        cur = 0  
        for c in s:  
            bin_str = bin(c)  
            b.append(bin_str[2:].rjust(8, "0"))  
            cur += 1  
            if(cur == step):  
                content = "".join(b)  
                for i in range(0, len(content), 6):  
                    val = int(content[i:i+6], base=2)  
                    val = base64_table[val]  
                    result.append(val)  
                cur = 0  
                b = []  
      
        if(0 < cur < step):  
            content = "".join(b)  
            content = content.ljust(6 * (cur + 1), "0")  
            for i in range(0, len(content), 6):  
                val = int(content[i:i+6], base=2)  
                val = base64_table[val]  
                result.append(val)  
            for i in range(step - cur):  
                result.append("=")  
        return "".join(result).encode()  
      
    def b64decode_sp(s):  
        base64_table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"  
        s = s.decode()  
        s = s.rstrip("=")  
        result = bytearray()  
        b = []  
        step = 4  
        cur = 0  
        for c in s:  
            idx = base64_table.index(c)  
            b.append(bin(idx)[2:].rjust(6, "0"))  
            cur += 1  
            if(cur == step):  
                content = "".join(b)  
                for i in range(0, len(content), 8):  
                    val = int(content[i:i+8], base=2)  
                    result.append(val)  
                cur = 0  
                b = []  
      
        if(0 < cur < step):  
            content = "".join(b)  
            content = content[:8 * (cur - 1)]  
            for i in range(0, len(content), 8):  
                val = int(content[i:i+8], base=2)  
                result.append(val)  
        return bytes(result)  
      
    class TestBase64Func(unittest.TestCase):  
        def test_encode(self):  
            a = b"ffasdfaerafdasfsdfsadsa"  
            self.assertEqual(b64encode_sp(a), base64.b64encode(a))  
            a = b"1212121214667909"  
            self.assertEqual(b64encode_sp(a), base64.b64encode(a))  
            a = b"12121212146671111909"  
            self.assertEqual(b64encode_sp(a), base64.b64encode(a))  
            a = "你好".encode()  
            self.assertEqual(b64encode_sp(a), base64.b64encode(a))  
              
        def test_encode(self):  
            a = b"a123456"  
            a = base64.b64encode(a)  
            self.assertEqual(b64decode_sp(a), base64.b64decode(a))  
            a = b"1212121214667909"  
            a = base64.b64encode(a)  
            self.assertEqual(b64decode_sp(a), base64.b64decode(a))  
            a = b"12121212146671111909"  
            a = base64.b64encode(a)  
            self.assertEqual(b64decode_sp(a), base64.b64decode(a))  
            a = "你好".encode()  
            a = base64.b64encode(a)  
            self.assertEqual(b64decode_sp(a), base64.b64decode(a))  
      
    if __name__ == "__main__":  
        unittest.main(verbosity=2)

  



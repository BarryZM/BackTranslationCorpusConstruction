#-*- coding:utf-8 -*-

import re
import requests
import execjs
from .translator import Translator

class Baidu(Translator):
    def __init__(self,from_lan_id,to_lan_id,trans_engine,max_bytes_length):

        self.lan_dict={
            '中文':'zh',
            '英文': 'en',
            '俄文': 'ru',
            '法文': 'fra',
            '日文': 'jp',
            '韩文': 'kor'
        }
        super(Baidu, self).__init__(from_lan_id, to_lan_id, self.lan_dict, trans_engine, max_bytes_length)
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        self.header = {
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://fanyi.baidu.com',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
            'x-requested-with': 'XMLHttpRequest',
            'cookie': 'BIDUPSID=D3290C65C03AEF0E98D97B8641DFFB15; PSTM=1570785944; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=0CC6F13854E81A68D3C564D36E7C8A03:FG=1; APPGUIDE_8_2_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=wt_OJeC626EDLgju-c_JbHce7gSxbKcTH6aoxbIy4_AgXmAxrp74EG0PJf8g0Ku-dWitogKKBmOTHg-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JJkO_D_atKvjDbTnMITHh-F-5fIX5-RLf5TuLPOF5lOTJh0RbtOkjnQD-UL82bT2fRcQ0tJLb4DaStJbLjbke6cbDa_fJ5Fs-I5O0R4854QqqR5R5bOq-PvHhxoJqbbJX2OZ0l8KtDQpshRTMR_V-p4p-472K6bML5baabOmWIQHDPnPyJuMBU_sWMcChnjjJbn4KKJxWJLWeIJo5Dcf3PF3hUJiBMjLBan7056IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbRO4-TF-D5jXeMK; delPer=0; PSINO=2; H_PS_PSSID=1435_21104_18560_26350; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1580216234,1580216243,1580458514,1580458537; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1580458539; __yjsv5_shitong=1.0_7_ed303110bee0e644d4985049ba8a5cd1f28d_300_1580458537306_120.10.109.208_66a3b40c; yjs_js_security_passport=630340c0505f771135167fa6df3e5215699dcf0b_1580458538_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22vie%22%2C%22text%22%3A%22%u8D8A%u5357%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D'
        }

        self.data = None

    def get_sign_ctx(self):
        ctx = execjs.compile(
            r"""

             function n(r, o) {
                for (var t = 0; t < o.length - 2; t += 3) {
                    var a = o.charAt(t + 2);
                    a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                    a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                    r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                    }
                return r
                 }

            function e(r) {
        var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
        if (null === o) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
        } else {
            for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
            var g = f.length;
            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
        }
        var u = void 0
          , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        u =' """ + str(self.get_gtk()) + r""" ';
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
            S[c++] = A >> 6 & 63 | 128),
            S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
            p = n(p, F);
        return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
    }
            """
        )
        return ctx

    def get_sign(self, text):
        ctx = self.get_sign_ctx()
        sign = ctx.call("e", text)
        #print(sign)
        return sign

    def get_token(self):
        s = requests.session()
        url = 'https://fanyi.baidu.com/'
        try:
            html = requests.get(url, headers=self.header)
            html = html.text
            raw_tk_str = re.search('token:.*,', html).group(0)
            #print(raw_tk_str,'  ',raw_tk_str.split('\''))
            token = raw_tk_str.split('\'')[1]
            #print(token)
            return token
        except Exception:
            return None

    def get_gtk(self):
        url = 'https://fanyi.baidu.com/'
        try:
            html = requests.get(url)
            html = html.text
            # print(html)
            raw_gtk_str = str(re.search('window.gtk = .*;', html))
            gtk = raw_gtk_str.split('\'')[1]
            #print('gtk ' + gtk)
            return gtk
        except Exception:
            return None

    def get_data(self, from_lan, to_lan, text):
        data = {}
        data['from'] = from_lan
        data['to'] = to_lan
        data['query'] = text
        data['simple_means_flag'] = 3
        data['transtype'] = 'realtime'
        data['sign'] = self.get_sign(text)
        while True:
            tk = self.get_token()
            if tk:
                break
            #print('get tk error, continue')
        data['token'] = tk
        #   '372a653a84ba137c63c4d87461d5736e'
        return data

    def translate(self, from_lan,to_lan,text):
        #self.data = self.get_data('zh', 'en', text)
        self.data = self.get_data(from_lan, to_lan, text)
        s = requests.session()
        ans = []
        try:
            result = requests.post(self.url, headers=self.header, data=self.data).json()
            for i in result['trans_result']['data']:
                ans.append(i['dst'])
            return ans
        except Exception:
            print('error')
            return None

if __name__ == '__main__':
    # 语种id对应关系 1: '中文', 2: '英文', 3: '日文', 6: '俄文'
    # aim_lan = [1,2,3,6]

    aim_lan = [2]
    for i in aim_lan:
        if i == 1:
            bd = Baidu(from_lan_id=i, to_lan_id=2,trans_engine='百度',max_bytes_length=5000)
            bd.run()
        else:
            bd = Baidu(from_lan_id=i,to_lan_id= 1,trans_engine='百度',max_bytes_length=5000)
            bd.run()
        del bd
    # bd = Baidu(from_lan_id=1, to_lan_id=2, trans_engine='百度', max_bytes_length=5000)
    # print(bd.translate('zh','en','你好\n哈哈\n嘻嘻'))
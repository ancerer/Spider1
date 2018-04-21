import urllib.request as request
import urllib.parse as parse
import json

if __name__ == '__main__':
    # 访问的地址
    Request_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # 存储Form Data
    Form_Data = {}
    Form_Data['i'] = 'jack'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1523883643394'
    Form_Data['sign'] ='b570f5a9836e86b385e4ed6046190c94'
    Form_Data['action'] ='FY_BY_REALTIME'
    Form_Data['typoResult'] ='false'
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(Request_url, data)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    # 使用json
    translate_results = json.loads(html)
    # 找到翻译结果
    translate_results = translate_results['translateResult']
    # 打印翻译信息
    print("翻译的结果是：%s" % translate_results)





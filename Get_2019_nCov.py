import requests
import json
import urllib.parse

url_China = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"

Headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

# 获取全国数据
def get_2019_nCov_China():
    html = requests.get(url_China,headers=Headers)
    # json.dumps()将字典转换为字符串
    # json.loads()将字符串转换为字典
    res = json.loads(html.text)
    # print(html.text)
    # print(res)
    res_data = json.loads(res['data'])
    return res_data

# 获取海外数据
def get_2019_nCov_World():
    country = str(input("请输入国家:"))
    country = urllib.parse.quote(country)
    url_World = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?country=" + country + "&"
    html = requests.get(url_World,headers=Headers)
    res = json.loads(html.text)
    res_data = res['data']
    return res_data

# 全国
def get_China():
    data = get_2019_nCov_China()
    list = ['截止时间：' + str(data['lastUpdateTime']) + '\n',
            '全国累计确诊：' + str(data['chinaTotal']['confirm']) + '\n',
            '全国新增确诊：' + str(data['chinaAdd']['confirm']) + '\n',
            '全国累计疑似：' + str(data['chinaTotal']['suspect']) + '\n',
            '全国新增疑似：' + str(data['chinaAdd']['suspect']) + '\n',
            '全国累计治愈：' + str(data['chinaTotal']['heal']) + '\n',
            '全国新增治愈：' + str(data['chinaAdd']['heal']) + '\n',
            '全国累计死亡：' + str(data['chinaTotal']['dead']) + '\n',
            '全国新增死亡：' + str(data['chinaAdd']['dead']) + '\n'
    ]
    # 将 '' 里面的内容进行连接
    result = ''.join(list)
    print(result)

# 省份
def get_province():
    data = get_2019_nCov_China()['areaTree'][0]['children']
    province = str(input("请输入省份："))
    for i in data:
        if province in i['name']:
            for item in i['children']:
                list = [
                    ' 地区: ' + str(item['name']) + '\n',
                    ' 累计确诊：' + str(item['total']['confirm']) + '\n',
                    ' 新增确诊：' + str(item['today']['confirm']) + '\n',
                    ' 累计治愈：' + str(item['total']['heal']) + '\n',
                    ' 累计死亡：' + str(item['total']['dead']) + '\n'
                ]
                result = ''.join(list)
                print(result)

# 海外
def get_World():
    data = get_2019_nCov_World()
    for i in range(len(data)):
        list = ['日期：' + str(data[i]['date']) + '\n',
                '新增确诊：' + str(data[i]['confirm_add']) + '\n',
                '累计确诊：' + str(data[i]['confirm']) + '\n',
                '累计治愈：' + str(data[i]['heal']) + '\n',
                '累计死亡：' + str(data[i]['dead']) + '\n',
        ]
        result = ''.join(list)
        print(result)

print("1.全国   2.省份   3.海外")
choice = int(input("请输入你想要查询的选项："))
if choice == 1:
    get_China()
elif choice == 2:
    get_province()
elif choice == 3:
    get_World()
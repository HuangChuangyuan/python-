# 导入数据请求模块
import requests

# # 导入格式化输出模块
# from pprint import pprint

# 导入csv模块
import csv

#导入时间模块
import time

#导入随机模块
import random

# 创建文件对象
f = open('data.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '职位',
    '公司名称',
    '薪资',
    '城市',
    '区域',
    '经验要求',
    '学历要求',
    '领域',
    '性质',
    '规模',
    '职位详情页',
    '公司详情页',
])
csv_writer.writeheader()


# 请求链接
url='https://we.51job.com/api/job/search-pc'
for page in range(1, 10):
    time.sleep(random.randint(1, 2))
    #请求参数
    data = {
        'api_key':'51job',
        'timestamp':'1701683756',
        'keyword':'',
        'searchType':'2',
        'function':'',
        'industry':'',
        'jobArea':'000000',
        'jobArea2':'',
        'landmark':'',
        'metro':'',
        'salary':'',
        'workYear':'',
        'degree':'',
        'companyType':'',
        'companySize':'',
        'jobType':'',
        'issueDate':'',
        'sortType':'0',
        'pageNum':page,
        'requestId':'',
        'pageSize':'20',
        'source':'1',
        'accountId':'',
        'pageCode':'sou | sou | soulb',
    }
    # 模拟浏览器<请求头>
    # 字典数据类型->构建完整键值对
    headers = {
        'Cookie': 'guid=b2e2305ac4c5e3c02d346746353e6c08; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22b2e2305ac4c5e3c02d346746353e6c08%22%2C%22first_id%22%3A%2218c2f4c28001148-0b7364a4e854d78-4c657b58-1327104-18c2f4c280112d8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThjMmY0YzI4MDAxMTQ4LTBiNzM2NGE0ZTg1NGQ3OC00YzY1N2I1OC0xMzI3MTA0LTE4YzJmNGMyODAxMTJkOCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6ImIyZTIzMDVhYzRjNWUzYzAyZDM0Njc0NjM1M2U2YzA4In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22b2e2305ac4c5e3c02d346746353e6c08%22%7D%2C%22%24device_id%22%3A%2218c2f4c28001148-0b7364a4e854d78-4c657b58-1327104-18c2f4c280112d8%22%7D; acw_tc=ac11000117016969540968475e00d2796cb4268fa121df462cb5aaaf80c7b8; NSC_ohjoy-bmjzvo-200-159=ffffffffc3a0d61945525d5f4f58455e445a4a423660; acw_sc__v2=656dd5bcd070f278868be29c45bfb4501ddec9dd; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60030200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C9%EE%DB%DA%D0%C2%C1%AA%B4%EF%CD%F8%C2%E7%BF%C6%BC%BC%D3%D0%CF%DE%B9%AB%CB%BE%A1%FB%A1%FA1%A1%FB%A1%FA1%7C%21; JSESSIONID=B4306CA4572AAFEF3C71A82765C86BCE; ssxmod_itna2=7uDtDKBKY5GKAIP0LKYKO=1fwaVOaZYP6DnIo0Q5dDlam4Yq03Na5ua+r6D6W=LHfOql=l5U32lxjHwCdVPlxrsnmfjPUzWTA=B0jkEoKCc6DdywF2cxLj7Fjx=/bu9y4glbLxUKPnb7oahGuAHGNPHGqp0QcZmwOPgw6lnTT/7=6iPIr6GwVQ0s=nirBmeTxZWW5oOW==ipkEHF4PWCEA8NcfLkYagX2OMaSZGaXrYRZBAXHokP/9mwc6PafcgHZDZbk=WcL4p9DavW7cZkuIU6=cyB+kz86rTxZKP=EeFLepIH7oM2mbQb4S+r68DSbRER2zjTtCrbIr44mk/KRbu/UeRYTWSW0ARc++wAINFelU2Q+TgRi3NonDbDOEtCOt0hnGKxO+wnu3wu0U5tQIa300Rr3+DPvoXIhX3aiQArZreDqNZhKFPymS7SGC+xsQfB0ASW+BYASfPSfS6iLWNW0KKK6fCGi=Fb7Rf+fea7LjYEwUIUiEjbhoD075=xzxpEGUzPYYF2NU2oDYnEPdz+RE47fDwSRNtu27ueEtAmxjOtegxPOIvIYE9RAjD=0ruOizZu5+9RODsudLiycUygAW44YuFBq2qD7=DY9xeD; ssxmod_itna=euGQqjxfOGkiD=DXGqEqDT4mq8q0OLDx7ILdD/KWmDnqD=GFDK40oE7ANQE4j4P7/nDaiTLYhDcvYfWWBq3Y7GG4wa3bDCPGnDBKE4HiYxiicDCeDIDWeDiDG4Gml4GtDpxG=DjBIt/lGqDEDYPVDitUD7Ux=eDjUu=nteG0DDUHB4G2WQtQDDNQep3e3qxqxGYUtlt=LweWo0=DjTrD/bxk20=dX=HQSqa7oGiWiqGytKGuRdbSneDH+MNZYjvf374zGb4PWhmx4OfmIGeQW7wK9DlK7hDnPpxP/BezjDqxD===',
        'Referer': 'https://we.51job.com/pc/search?jobArea=030200&keyword=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    # 发送请求
    response = requests.get(url=url, params=data, headers=headers)
    # <Response [200]]> 响应对象
    print(response)
    # 获取响应json数据-> 字典数据类型
    json_data = response.json()
    # 提取职位列表的数据
    items = json_data['resultbody']['job']['items']
    for index in items:
        print(index)
        # 处理城市信息 区分城市和区域
        area_info = index['jobAreaString'].split('·')
        if len(area_info) == 2:
            city = area_info[0]
            area = area_info[1]
        else:
            city = area_info[0]
            area = '未知'

        # index --> 字典数据类型 提取具体职位信息内容
        job_info = {
            '职位': index['jobName'],
            '公司名称': index['companyName'],
            '薪资': index['provideSalaryString'],
            '城市': city,
            '区域': area,
            '经验要求': index['workYearString'],
            '学历要求': index['degreeString'],
            '领域': index['industryType1Str'],
            '性质': index['companyTypeString'],
            '规模': index['companySizeString'],
            '职位详情页': index['jobHref'],
            '公司详情页': index['companyHref']
        }
        # 写入数据
        csv_writer.writerow(job_info)
        print(job_info)

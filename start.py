import os
import requests
import pandas as pd
from lxml import html
import time

session = requests.Session()

while True:
    # 현재 시간 가져오기
    current_time = time.strftime('%Y%m%d_%H%M')
    current_date = time.strftime('%Y%m%d')
    
    # 폴더 이름 설정
    folder_name = f'gmarket_{current_date}'
    
    # 폴더가 존재하지 않으면 폴더 생성하기
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 파일 이름 설정
    file_name = f'{folder_name}/gmarket_{current_time}.xlsx'

    # URL 설정
    url = "https://corners.gmarket.co.kr/superdeals"

    # 세션 객체를 이용해 HTML 내용 가져오기
    response = session.get(url)
    tree = html.fromstring(response.content)

    # Xpath를 이용해 데이터 추출하기
    data_quantity = []
    data_name = []
    data_link = []
    data_price = []
    for i in range(1, 300):
        fullxpath_quantity = f"/html/body/div[3]/div/div[2]/ul/li[{i}]/div/div/span[3]/span/strong"
        fullxpath_name = f"/html/body/div[3]/div/div[2]/ul/li[{i}]/div/a/span"
        fullxpath_link = f"/html/body/div[3]/div/div[2]/ul/li[{i}]/div/a/@href"
        fullxpath_price = f"/html/body/div[3]/div/div[2]/ul/li[{i}]/div/div[1]/span[1]/strong"

        # Xpath가 존재하는지 확인하기
        if tree.xpath(fullxpath_quantity):
            # 데이터 추출하기
            data_quantity_i = tree.xpath(fullxpath_quantity)[0].text.replace(',', '')
            if "만+" in data_quantity_i:
                data_quantity_i = data_quantity_i.replace("만+", "0000")
            if data_quantity_i == 'NEW':
                data_quantity_i = '0'
            data_quantity.append(int(data_quantity_i))

            # 상품명 데이터 추출하기
            data_name_i = tree.xpath(fullxpath_name)[0].text
            data_name.append(data_name_i)
            # 링크 데이터 추출하기
            data_link_i = tree.xpath(fullxpath_link)[0]
            data_link.append(data_link_i)
            # 가격 데이터 추출하기
            data_price_i = tree.xpath(fullxpath_price)[0].text.replace(',','')
            try:
                data_price.append(int(data_price_i))
            except ValueError:
                data_price.append(int(0))
        else:
            break

    # 추출한 데이터를 이용해 pandas 데이터프레임 생성하기
    df = pd.DataFrame({'순위': [i for i in range(1, len(data_name)+1)],
                '상품명': data_name,
                '판매수': data_quantity,
                '링크': data_link,
                '가격': data_price})

    # 데이터프레임을 숫자 형식으로 엑셀 파일로 저장하기
    with pd.ExcelWriter(file_name) as writer:
        df.to_excel(writer, index=False, float_format='0')

    print(f"{file_name} 이라는 이름으로 저장되었습니다 =)")

    # 다시 반복문을 실행하기 전 5분간 대기하기
    time.sleep(300)

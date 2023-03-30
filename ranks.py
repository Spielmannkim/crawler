import os
import pandas as pd

# 파일 경로 설정
folder_path = './'

# 파일들의 경로 및 이름 설정
file_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if 'gmarket' in file_name and file_name.endswith('.xlsx')]

# 데이터를 담을 빈 딕셔너리 생성
data_dict = {}

# 파일들을 순회하며 데이터 추출
for file_path in file_paths:
    # 엑셀 파일 읽어오기
    df = pd.read_excel(file_path)

    # 각 상품에 대해 데이터 추출
    for i in range(len(df)):
        product = df.loc[i, '상품명']
        link = df.loc[i, '링크']
        price = df.loc[i, '가격']
        ranks = df.loc[i, '순위']

        # 해당 상품명이 이미 딕셔너리에 있는 경우, 해당 상품명의 리스트에 데이터 추가
        if product in data_dict:
            data_dict[product]['링크'].append(link)
            data_dict[product]['가격'].append(price)
            data_dict[product]['순위'].append(ranks)
        # 해당 상품명이 딕셔너리에 없는 경우, 새로운 딕셔너리 생성 후 데이터 추가
        else:
            data_dict[product] = {
                '링크': [link],
                '가격': [price],
                '순위': [ranks]
            }

# 데이터를 담을 빈 데이터프레임 생성
result_df = pd.DataFrame(columns=['상품명', '링크', '가격', '순위1', '순위2', '순위3'])

# 딕셔너리의 데이터를 데이터프레임에 추가
for i, (product, data_dict) in enumerate(data_dict.items()):
    # 상품명, 링크, 가격 추가
    result_df.loc[i, '상품명'] = product
    result_df.loc[i, '링크'] = data_dict['링크'][0]
    result_df.loc[i, '가격'] = data_dict['가격'][0]

    # 순위 데이터 추가
    for j, ranks in enumerate(data_dict['순위']):
        result_df.loc[i, f'순위{j+1}'] = ranks

# 결과 데이터프레임을 엑셀 파일로 저장
result_df.to_excel('순위모음.xlsx', index=False)

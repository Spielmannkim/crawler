import requests
import pandas as pd
from lxml import html
import time

# Create a session object
session = requests.Session()

while True:
    # Get current time
    current_time = time.strftime('%Y%m%d_%H%M')
    
    # Set file name
    file_name = current_time + '.xlsx'

    # Set URL
    url = "https://corners.gmarket.co.kr/superdeals"

    # Get HTML content using session object
    response = session.get(url)
    tree = html.fromstring(response.content)

    # Extract data using Xpath
    data_quantity = []
    data_name = []
    for i in range(1, 301):
        fullxpath_quantity = f"/html/body/div[3]/div/div[2]/ul/li[{i}]/div/div/span[3]/span/strong"
        fullxpath_name = f"/html/body/div[3]/div/div[2]/ul/li[{i}]/div/a/span"

        # Check if the xpath exists
        if tree.xpath(fullxpath_quantity):
            # Extract data_quantity
            
            data_quantity_i = tree.xpath(fullxpath_quantity)[0].text.replace(',', '')
            if "만+" in data_quantity_i:
                data_quantity_i = data_quantity_i.replace("만+", "0000")
            if data_quantity_i == 'NEW':
                data_quantity_i = '0'
            data_quantity.append(int(data_quantity_i))

            # Extract data_name
            data_name_i = tree.xpath(fullxpath_name)[0].text
            data_name.append(data_name_i)
        else:
            break

    # Create a pandas dataframe with extracted data
    df = pd.DataFrame({'순위': range(1, len(data_name)+1),
                    '상품명': data_name,
                    '판매수': data_quantity})

    # Write dataframe to an excel file with numeric format
    with pd.ExcelWriter(file_name) as writer:
        df.to_excel(writer, index=False, float_format='0')

    print(f"{file_name} 이라는 이름으로 저장되었습니다 =)")

    # Wait for 1 minute before running the loop again
    time.sleep(60)

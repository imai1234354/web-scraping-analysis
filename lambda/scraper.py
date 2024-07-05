import json
import requests
from bs4 import BeautifulSoup
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # ウェブサイトからデータをスクレイピング
    url = "http://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 必要なデータを抽出（例としてタイトルを抽出）
    data = []
    for item in soup.find_all('h2'):
        data.append({
            'title': item.get_text(),
            'timestamp': datetime.utcnow().isoformat()
        })
    
    # データをJSON形式に変換
    data_json = json.dumps(data)
    
    # Amazon S3にデータを保存
    s3 = boto3.client('s3')
    bucket_name = "your-s3-bucket-name"
    file_name = f"scraped_data_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=data_json,
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data scraped and stored successfully')
    }

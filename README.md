# web-scraping-analysis
# 自動化ウェブスクレイピングとデータ分析

このプロジェクトは、AWSサービスを使用して定期的にウェブサイトをスクレイピングし、データを分析して可視化する方法を示します。

## 使用技術

- AWS Lambda
- Amazon S3
- Amazon Athena
- Amazon QuickSight

## プロジェクトフォルダ構造

## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd web-scraping-analysis
    ```

2. Lambda関数のデプロイ:
    - AWS Lambdaコンソールで新しい関数を作成します。
    - `scraper.py`のコードを関数にコピーします。
    - `requests`, `beautifulsoup4`, `boto3`ライブラリを含むLambdaレイヤーを作成して関数にアタッチします。
    - S3バケット名を`scraper.py`のコード内で指定します。

3. スケジュール設定:
    - AWS CloudWatch Eventsを使用して、Lambda関数を定期的にトリガーします。

4. データ分析と可視化:
    - Amazon AthenaでS3に保存されたデータをクエリします。
    - Amazon QuickSightを使用してデータを可視化します。

## 使用方法

- CloudWatch Eventsで設定されたスケジュールに従ってLambda関数が実行され、ウェブサイトからデータがスクレイピングされてS3に保存されます。
- Amazon Athenaを使用してデータをクエリし、Amazon QuickSightで可視化します。





# api-write-blog-every-week

Write-Blog-Every-Weekのサイト用に、メンバーのブログをクロールし、NetlifyにJSONファイルを出力し簡易的にAPIサーバとするプログラムです。

This program crawls a member's blog for Write-Blog-Every-Week site and outputs a JSON file to Netlify as a simple API server.

# 使い方 / How To Use

dataディレクトリ配下に存在するCSVファイルに巡回させるメンバーのブログURLを入力します。
そのCSVファイルの情報をもとに`python src/feeds/cli.py`を実行します。その後、プログラムがメンバーのブログを巡回し必要な情報を出力します。

Enter the blog URL of the member to be patrolled in the CSV file under the data directory.
Run `python src/feeds/cli.py` with the information in the CSV file. The program will then circulate the member's blog and output the necessary information.

# 参考情報 / Reference information
フロントエンドのプログラムはこちらです。

The front-end program is here.

https://github.com/yoshitaku-jp/write-blog-every-week
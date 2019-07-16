# youtube-dl-automate
`Selenium`でYouTubeの「後で見る」リストの動画をダウンロードするのを自動化するスクリプト。

# How to use

## webdriverをインストール
```
pip3 install selenium
```

## ブラウザに合ったwebderiverをダウンロード

- [Chrome](https://sites.google.com/a/chromium.org/chromedriver/)
- [Firefox](https://github.com/mozilla/geckodriver/)


## PATHにwebdriverを通す
割愛


## 実行
```
python3 automate.py
```
-  Googleログイン画面が出るので、認証をする
-  スクリプトに認証情報を書いておくと自動で入力されるので便利。取り扱い注意。

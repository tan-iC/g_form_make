# g_form_make

## 概要

1. Google Forms API [[1](https://developers.google.com/forms/api)] を利用し、PythonでGoogle formを作成する
1. csvファイルとして得られる回答結果を集計する

## リポジトリ説明

1. data

    - 以下のファイルを格納する場所として想定
        1. Google Cloud Platform [[2](https://console.developers.google.com/)] のcredentialファイル（json）
        1. 回答結果（csv）

1. examples

    - 実行用のPythonソースコード（py）

1. result

    - 集計結果（csv）

1. src

    - 各機能を実装したファイル（py）

## 備考

1. VPNなどを使っている状態だとサーバまでたどり着かないことがある

## 参考文献

1. <https://developers.google.com/forms/api>
1. <https://console.developers.google.com/>
1. <https://developers.google.com/forms/api/reference/rest/v1/forms>
1. <https://github.com/googleworkspace/python-samples/tree/main/forms/snippets>
1. <https://www.ka-net.org/blog/?p=14488>
1. <https://omohikane.com/python_no_module_oauth2client/>
1. <https://www.tdi.co.jp/miso/google-forms-api-2>


## Google Forms API

- API paramater

    1. 公式 [[3](https://developers.google.com/forms/api/reference/rest/v1/forms)] [[4](https://github.com/googleworkspace/python-samples/tree/main/forms/snippets)]

- Google Cloud Platform

    1. OAuth認証が必要 [[2](https://console.developers.google.com/)]
        - 概略

            1. Google Cloud Platformで認証情報を作成
            1. ```client_secret_***.json```を取得

## 備考

1. フォーム作成を行うためにはOAuth認証 [[2](https://console.developers.google.com/)] が必要
1. VPNなどを使っている状態だとサーバまでたどり着かないことがある

## 参考文献

1. <https://developers.google.com/forms/api>
1. <https://console.developers.google.com/>
1. <https://developers.google.com/forms/api/reference/rest/v1/forms>
1. <https://github.com/googleworkspace/python-samples/tree/main/forms/snippets>
1. <https://www.ka-net.org/blog/?p=14488>
1. <https://omohikane.com/python_no_module_oauth2client/>
1. <https://www.tdi.co.jp/miso/google-forms-api-2>

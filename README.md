# django_demo

## Getting Started
**用 Django REST framework 實作文章的 CRUD API，並以 simple-jwt 控管權限，以下會以 docker-compose 安裝環境並執行。**

### Prerequisites
* python 3.7
* pip
* docker
* docker-compose

### Installing
**1.clone repository 到 local。**

### Usage
**1.命令列輸入 :**
```shell
docker-compose up -d
```
以建立容器

**2.建立使用者**
```shell
docker exec -it server python manage.py createsuperuser
```
根據輸入框提示輸入即可建立

**3.初始頁面**
[demo](http://127.0.0.1:8000/swagger/)

**4.取得 token 並使用**

在 Swagger 頁面中，先進行 login，即可取得 access token 及 refresh token

之後再到網頁上方的 authorize 裡的輸入框輸入 Bearer [access token]

之後即可使用任一 API

**錯誤處理**

若運行 docker 發生以下錯誤
```shell
server      | /usr/bin/env: ‘bash\r’: No such file or directory
```
麻煩將 dbsetup.sh 的換行符號從 windows 換成 unix 即可

## Running the tests

運行測試

### Break down into end to end tests

在專案底下的命令列執行

```
python manage.py test
```
即可觀看測試結果

### And coding style tests

想分析測試專案程式碼，可另外使用pylint進行分析

首先
```
pip install pylint
```

之後針對要分析的py檔執行:

```
python -m pylint ./articles/views.py
```
即可觀看測試結果

## Authors

* **ZheWei** - *Initial work* - [ZheWei](https://github.com/zzhewei)

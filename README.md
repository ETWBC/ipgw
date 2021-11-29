# Safetely login ipgw(NEU) with QRcode

**在服务器上使用二维码安全地登录东北大学校园网**

通常在服务器上想要远程连接登录校园网账号时，需要使用账号密码，而目前GitHub上面的方法都需要在本地存储账号和明文密码，安全性较弱，因此我们通过模拟浏览器行为写了这个利用二维码登录校园网的项目。

## 贡献者

[Bingchao Wang](https://github.com/ETWBC); [Ming Wang](https://github.com/wangming1785)

### 需求库

- numpy
- pillow
- selenium

此外，还需要下载[geckodriver](https://github.com/mozilla/geckodriver/releases)并将其路径加入PATH。

## 如何使用

### 登录

下载本项目，进入`ipgw.py`的路径下，使用python运行该文件：

```shell
python ipgw.py
```

默认情况下是登录，运行后会显示一个二维码，如下图所示：

![image-20211129125929546](https://github.com/ETWBC/ipgw/blob/main/QRcode-sample.png)

使用微信扫码，进行授权，即可登录。

### 注销

注销与登录操作类似，只需要在运行时加`logout`参数：

```shell
python ipgw.py --logout
```

运行并扫码验证即可注销当前登录的账号。

### 全局使用方式

使用`chmod +x ipgw.py`为其添加可执行权限。
将用户目录下的 `.bashrc` 文件后加入两行
···shell
alias login='该py文件所在文件夹/ipgw.py'
alias logout='该py文件所在文件夹/ipgw.py --logout'
```
然后可以在全局使用`login`进行登录，`logout`进行登出。

## 说明

该项目为了方便校内同学在不需要输入明文密码的情况下安全登录校园网账号，也欢迎各位同学和我们一同优化这一项目。


# TANet-iTW-LoginTool
一個可以自動登入`TANetRoaming`與`iTaiwan`網路的Python工具

> 我恨 TANetRoaming(花蓮的) 現在為啥不能用 iTaiwan 登入(雖然現在 iTaiwan 也不能註冊/登入)

## 原理

這是登入網址:
```url
https://wlan.hlc.edu.tw/tanet/index.php?loginurl=http://[ip位置]:8003/login&user_name=username&pass_name=password&umac=[裝置的MAC地址]
```

然後可以發現有一個很神奇的東西: `loginurl`(然後其他都是幌子)
去解析了一下`wlan.hlc.edu.tw`的原始碼，可以發現他是間接把登入資訊送到`loginurl`的

所以我就把登入資訊直接送到`loginurl`裡，然後... 就登入成功了!

## 使用方法

 1. 需要安裝 `Requests`、`beautifulsoup4`(`pip install requests beautifulsoup4`)
 2. 修改
```python
iTaiwansPhoneNumber = "09xxxxxxxx" #必須是要有註冊過iTaiwan帳號的手機號碼
iTaiwansPassword = "xxxxxxxxxxxxx" #此手機號的iTaiwan密碼
```
 3. 執行
 4. 免費網路可以用了

## 題外話

你可以透過我的網站讀取這個repo，也可以留言網站: <https://muisnow.3zh-studio.com/git/TANetLoginTool>

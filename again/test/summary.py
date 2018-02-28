#coding:utf-8

'''
学习网页：http://blog.csdn.net/column/details/12694.html
用来练习的网页：http://sahitest.com/demo/clicks.htm
http://sahitest.com/demo/index.htm
非常好的练习网站

前提条件：
1、熟练掌握xpath\CSS 定位的使用，这样在遇到各种难以定位的属性时才不会变得束手无策。
2、准备一份Slenium Python Bindings，及时查阅WebDriver 所提供的方法。
3、学习掌握JavaScript 语言，掌握JavaScript 好处前面已经有过阐述，可以让我们的自动化测试工作
更加游刃有余。
4、自动化测试归根结底是与前端打交道，多多熟悉前端技术，如http 请求，HTML 语言，cookie、session
机制等。


出现的问题：
1.模拟鼠标操作，click，right click都生效，但是double click在firefox上无效，同样的代码，有人在chrome上有效果
2.prompt confirmation不能识别editbox
3.下载时，需要浏览器的参数，可以在firefox的浏览器输入about:config来查，search一下browser.download即可。不同的浏览器，效果不同
    fp = webdriver.FirefoxProfile()
    fp.set_preference(xxxxxxxxxxxxxxxxxx)配置这里
    browser.download.dir：指定下载路径
    browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
    browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器
    browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问
4.调用js


目前学习到201页,第九章，未学习如何使用邮箱，使用stmplib模块，第十章未练习（分布式）
目前继续学习到284，进程/线程部分


Link Test

Form Test

Table Test

Select Test

Frames Test

IFrames Test

ShadowRoot Test

Window Open Test

Window Open Test With Title

Show Modal Test
Span and Div Page

Label Page

Headings Test

Visible Test

Strict Visible Test

Contain Test

Prompt Page

Js Popup

Save As Test

Break Frames

Close Self

Close Self

Blank Page

Different Domains

Different Domains External

Iframe Different Domains

OnBeforeUnload

Error Pages

204 Response

Delayed Load page

IFrame via doc write

Head request with 204 Response

Clicks Page

Combo Clicks Page

Mouse over

Key Press

Drag Drop Test

Drag Drop DataTransfer

Wait For Condition

Clear Timeout All

Google

HTTPS Google

Temp test

Timer

Performance

Responsive Page

Silverlight

Element On Top Test














'''
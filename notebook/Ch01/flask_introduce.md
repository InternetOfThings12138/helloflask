##一  介绍
Flask是使用python编写的Web微框架(micro framework)。 
 
主要包含两个依赖：  

- WSGI工具集：[Werkzeug](http://werkzeug.pocoo.org)  
WSGI:Web Server Gateway Interface,Web服务器网关接口  
处理请求与响应，内置WSGI开发服务器、调试器和重载器
- [Jinja2模板引擎](http://jinja.pocoo.org/)  
模板渲染引擎

补充：  
1.Web框架可以让开发者不用关心底层的请求响应处理
2.Flask只保留了Web开发的核心功能，其他功能由外部扩展实现


## 二 注册路由  
路由： route，负责管理URL和函数之间的映射，这里的函数称为视图函数(view function)    
URL: Uniform Resource Lacator, 统一资源定位符。 指向网络中某个资源的地址
Web应用中，客户端和服务器上的Flask程序交互步骤：  
1. 用户在浏览器输入URL  
2. Flask接收用户请求并解析URL  
3. 找到URL对应函数（app.route()装饰器）  
4. 执行函数内容并生成响应，返回给浏览器  
5. 浏览器接收并解析响应，页面显示


## 三 启动开发服务器  
Flask通过依赖包Click内置CLI系统(Command Line Interface, 命令行交互界面)  
### 1. 启动方式       
(1) 命令行  
在Terminal中打开项目路径，利用`$ flask run`启动  
- 程序主模块命名为app.py，命令会自动在其中寻找实例。  
- 主模块是其他名称(例如hello.py)，需要设置环境变量FLASK_APP  
    `Linex&macOS: $ export FLASK_APP=hello`  
    `windows: set FLASK_APP=hello`  
- ctrl+C 退出  
（2）Pycharm  
！[Pycharm设置](D:\learn\Code\flask_web_development\notebook\Ch01\Pycharm启动服务器设置.jpg)

### 2.环境变量配置  
环境变量在新创建命令行窗口或重启电脑后清除，在根目录下创建.env与.flaskenv  
- .flaskenv存储和Flask相关的公开环境变量，如FLASK_APP
- .env用来存储包含敏感信息的环境变量，如Email服务器的账户名和密码。   

*注：.env包含敏感信息不能上传git*

### 四  python shell  
许多操作需要在python shell（Python交互式解释器）里执行  
1.基本操作命令：
`启动： flask shell  
退出：ctrl+z / exit() / quit()  
app 查看实例  
app.name 查看实例名称`

### 五 项目配置  
配置名称必须是全大写模式，小写变量不会被读取  
`app.config["ADMIN_NAME"] = 'PETER' # 字典配置`   
`app.config.update(
TESTING=TRUE,SECRET_KEY="*(&)") # update() 方法更新`
`value = app.config["ADMIN_NAME"]`


### 六 模板与静态文件  
模板文件存放在项目根目录中的templates文件夹中，包含HTML文件。  
静态文件存放在static文件夹下，包含HTML文件中加载的CSS和JavaScript文件。

`注：扩展资源在开发环境下使用本地资源，可以提高加载速度。最好下载到static目录下统一管理  
在过渡到生产环境时，手动管理所有本地资源或者设置CDN，避免使用扩展内置的资源`




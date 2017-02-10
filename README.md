## 安装和配置步骤：

1. 下载AnyLibrary并解压到C:\;
2. 安装C:\AnyLibrary V1.0.0\Tools\python-2.7.12.msi;

	2.1 双击python-2.7.12.msi;  

	2.2 点击Next;

	2.3 点击Next.默认Python27安装路径为C:\Python27\;

	2.4 点击Next;

	2.5 点击Finish.完成安装Python;

3. 设置AnyLibrary和Python的系统环境变量;

    4.1 点击"新建"，变量名:AnyLibrary_Home，变量值:C:\AnyLibrary V1.0.0\Bin,点击确定;
    
    4.2 点击"新建"，变量名:Python_Home，变量值:C:\Python27,点击确定;
    
    4.3 选择环境变量"Path",加入%AnyLibrary_Home%;%Python_Home%;
    
4. 输入CMD命令,"python -V",出现“Python2.7.27”即为Python环境变量设置成功;
5. 输入CMD命令:"InstallPlugin.py";
 
   

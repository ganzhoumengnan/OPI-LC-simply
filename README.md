# OPI-LC-simply
Quickly and easily build OPI-LC
一键搭建OPI轻节点

# step 1
下载python和PostgreSQL  
python下载地址（适用于windows64位）：https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe  
（切记在安装的时候在第一页把add path选上，也就是把python加入系统全局）  
PostgreSQL下载地址：https://www.enterprisedb.com/downloads/postgres-postgresql-downloads   

# step 2
下载https://github.com/bestinslot-xyz/OPI-LC  
并解压  
如图  
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/523a3d22-d15e-4238-a083-033e1c610ba4)   

# step 3
把main.py文件放到解压后的OPI-LC/brc20/sqlite目录  
如图  
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/059d9de6-51bc-44bc-9f7d-c9fc0ac58dcd)   

# step4
在OPI-LC/brc20/sqlite目录点击导航栏  
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/d0466a7c-1a9b-411c-8f2d-0aa57d93ef4e)  
输入CMD  按回车

![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/7b18c23c-95b6-486f-ba82-dcfa567b462e)  


# step 5
在cmd中输入：python main.py

![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/02ea7911-2463-4690-9a12-c5058facdc6d)  


# step 6 
等待安装各种依赖包，安装完成后按回车
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/2c301387-1213-40d2-a530-31c220a1fdef)  

# step 7
在这一步可以停留等候下，如果你嫌麻烦就直接1，脚本自动下载数据库，如果你嫌慢就去说明里的地址下载，然后把文件粘贴到这个脚本同目录下  
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/b3fb6609-4c7f-4fe2-8f1c-df3c83cbcc6f)  

# step 8 
如果你是再次打开脚本请输入0，要不然会删点已经解压的文件重新解压，如果是第一次用就输入1  
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/d81490fe-d1ff-409f-b641-c46ea7887043)  

# step 9 
如果已经配置过.env就按提示跳过，没有就按回车继续  
![image](https://github.com/ganzhoumengnan/OPI-LC-simply/assets/109869629/acd90e5b-7806-41c1-9e36-cbcf7267f12e)  

# step 10
开始同步节点了，如果关闭了 下次要继续同步就在当前目录 打开cmd 输入 python brc20_light_client_sqlite.py

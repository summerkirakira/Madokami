<div align="center">
  <img width=200 src="images/logo.png"  alt="项目标题"/>
  <h1 align="center">Madokami</h1>
</div>

<div align="center">

_✨ 可扩展的番剧订阅平台 ✨_

</div>

<div align="center">
<img title="docker build version" src="https://img.shields.io/docker/v/summerkirakira/madokami" alt="">
  <img src="https://img.shields.io/badge/python-3.10+-blue" alt="python">
  <img src="https://img.shields.io/badge/npm-17+-yellow" alt="servertap">
</div>


<!-- <div align="center">
<img src="https://img.shields.io/badge/QQ%E7%BE%A4-277828146-green?style=flat-square" alt="QQ Chat Group">
</div> -->

<p align="center">
  <a href="https://image.biaoju.site/madokami/">文档</a>
  ·
  <a href="https://image.biaoju.site/madokami/startup/">快速上手</a>
</p>


![](images/main_screenshot.png)


## 简介
Madokami是一个现代、跨平台的，可扩展的番剧订阅工具。它基于Python，只需单次订阅，即可从[Mikan Project](https://mikanani.me/)等番剧更新源处自动定时下载并重命名为人类易读且能被主流媒体管理软件([Emby](https://emby.media/), [jellyfin](https://jellyfin.org/), [Plex](https://www.plex.tv/)...)识别的文件，从而实现全自动追番体验。

## 特色
+ 功能强大：内置的Bangumi、TMDB刮削器与Mikan Project RSS解析器让Madokami能做到自动搜索并生成订阅规则，全程无需人工干预。
+ 插件机制：系统调度基于插件系统，支持导入符合[madokami-core](https://github.com/summerkirakira/Madokami-core)规范的本地插件，可以轻松为Madokami添加新功能。订阅+下载机制的任务(如直播流下载，网页抓取epub电子书等)均可轻松实现。
+ 稳定下载：默认下载器实现基于[Aria2](https://aria2.github.io/), 支持下载http, FTP, BT, 磁链等资源。
+ 状态监控: 内置下载状态查询器，当前下载项的名称，大小，进度，速度等将在WebUI实时显示，拒绝下载焦虑。
+ 易于开发: 100% 类型注解覆盖，配合编辑器的类型推导功能，能将绝大多数的 Bug 杜绝在编辑器中。

| 插件名称 | 状态 | 简介                             |
| :-----  |:---:|:-------------------------------|
| Mikan Parser ([仓库](https://github.com/summerkirakira/madokami-plugin-mikan-parser))|✅| 为Madokami项目提供蜜柑计划源的解析，搜索与下载功能。 |
| Danmaku Downloader ([仓库](https://github.com/summerkirakira/madokami-plugin-danmaku))|✅| 为Madokami项目提供B站视频及弹幕下载功能。      |

## 命名格式示例
```
Madokami
    ├── GIRLS BAND CRY
    │   └── Season 1
    │       ├── GIRLS BAND CRY - S1E1 - 东京嘿咻.mkv
    │       ├── GIRLS BAND CRY - S1E2 - 三只夜行动物.mkv
    │       └── GIRLS BAND CRY - S1E3 - 无脑问答.mkv
    │   
    ├── 恋语轻唱
    │   └─── Season 1
```

## 快速安装
推荐通过Docker部署Madokami

注：Madokami WebUI的默认用户名与密码是root, 123456

注意当docker容器被设置为桥接(`bridge`)模式时网络与宿主机隔离，此时无法通过`localhost`访问部署在本地的Aria2实例。此时设置内的Aria2地址应当填为内网地址或者Docker回环地址。

### 使用Docker-cli部署Madokami
```bash
docker run -d \
  --name=Madokami \
  -v your_data_dir:/app/backend/data
  -p 8000:8000 \
  --network=bridge \
  --restart always \
  summerkirakira/madokami
```

### 使用Docker Compose部署Madokami
在目标路径创建data文件夹
```bash
mkdir -p Madokami/data/aria2/downloads 
cd Madokami
```
项目根目录的`docker-compose.yml`中默认打包了Madokami项目, Aria2, Aria2 WebUI，如想使用自己的Aria2实例，删除对应的service即可。
注：docker-compose.yml中的UID和GID需要修改为当前用户。
可以通过`echo $UID`, `echo $GID`获得。
```yml
version: "3.8"

services:
  madokami:
    image: "summerkirakira/madokami:latest"
    restart: always
    network_mode: bridge
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/backend/data

  aria2:
    image: p3terx/aria2-pro
    restart: always
    ports:
      - "6800:6800"
      - "6888:6888"
      - "6888:6888/udp"
    environment:
      - RPC_SECRET=MADOKAMI
      - RPC_PORT=6800
      - LISTEN_PORT=6888
      - UMASK_SET=022
      - PUID=你的UID
      - PGID=你的GID
    volumes:
      - ./data/aria2/downloads:/downloads
      - ./data/aria2/config:/config

  ariang:
      container_name: ariang
      image: p3terx/ariang
      command: --port 6880 --ipv6
      network_mode: bridge
      ports:
        - 6880:6880
      restart: unless-stopped
      logging:
        driver: json-file
        options:
          max-size: 1m
```

### 本地部署
下载Madokami git仓库
```bash
git clone https://github.com/summerkirakira/Madokami.git
cd Madokami/backend
```
安装依赖
```bash
poetry install
```

编译前端
```bash
cd Madokami/frontend
npm install
npm run build
```

运行Madokami
```bash
python -m app.main
```

## Future
- [ ] B站视频、直播及弹幕下载
- [ ] 为本地番剧自动生成B站弹幕ASS字幕
- [ ] 在线已下载视频播放
- [ ] 网页解析生成Epub并自动发送到Calibre
- [ ] 连接[Nonebot2](https://github.com/nonebot/nonebot2)，实现番剧更新发送到QQ, Discord等聊天平台
- [ ] 连接[Home Assistant](https://www.home-assistant.io/)，在WebUI上显示追番状态
  
## Licence

[MIT](https://mit-license.org/)
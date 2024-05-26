---
title: 部署Madokami
icon: cubes
order: 1
category:
  - 使用指南
tag:
  - Docker
  - Docker Compose
  - Python
---

你可以选择以下三种方式安装Madokami

::: tabs#install

@tab Docker

```bash
docker run -d \
  --name=Madokami \
  -v your_data_dir:/app/backend/data
  -p 8000:8000 \
  --network=bridge \
  --restart always \
  summerkirakira/madokami:latest
```

@tab Docker Compose

在目标路径创建data文件夹
```bash
mkdir -p Madokami/data/aria2/downloads 
cd Madokami
```

创建一个名为`docker-compose.yml`的文件，并把以下内容复制到其中。

你可以通过

```bash
echo $UID
echo $GID
```

获得当前用户的UID和GID值，之后把它们复制到下方高亮代码处中，如GID为空，留空即可。

```yml {25-26} title="docker-compose.yml"
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

配置完成后使用

```bash
docker compose up -d
```

即可一键启动Madokami主项目，Aria2服务，Aria2 WebUI。

@tab 本地部署
下载Madokami git仓库
```bash
git clone https://github.com/summerkirakira/Madokami.git
cd Madokami/backend
```
安装依赖
```bash
poetry install
```
运行Madokami
```bash
python -m app.main
```
:::

::: important 注意
Madokami WebUI的默认用户名为`root`, 默认密码为`123456`

别忘了在正常登录后进入设置修改用户名和密码！
:::

如正常启动，即可通过`http://localhost:8000`访问Madokami的WebUI

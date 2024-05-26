---
title: 基础设置
icon: gears
order: 2
category:
  - 使用指南
tag:
  - Basic
---

## 设置Aria2
::: important 注意
当使用Docker部署Madokami时，无法通过`localhost`或`127.0.0.1`访问部署在本地的Aria2实例，请使用宿主机的局域网地址访问Aria2。
:::

Madokami使用RPC与Aria2进行通讯

![alt text](images/aria2.png "Aria2设置" =500x)

为应用Aria2设置，可通过设置界面右上角的重启按钮快速重启Madokami后端。


## 设置代理地址
截止2024.5，蜜柑项目在国内无法正常访问，需要配置代理才能使用番剧搜索服务，请在设置中配置http代理。Madokami仅会使用代理进行种子下载操作，番剧下载并不会使用代理，无需担心流量消耗。
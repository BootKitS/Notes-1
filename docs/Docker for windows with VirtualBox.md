# Docker for windows with VirtualBox

## 安装 Docker 和 Virtualbox

- 使用安装包安装
  - Docker [官网地址](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
  - Virtualbox [官网地址](https://www.virtualbox.org/wiki/Downloads)
- 使用 Chocolatey 
  - 安装 chocolatey [地址](https://chocolatey.org/docs/installation)
  - 命令: `choco install docker-desktop virtualbox`

## 创建 Virtual Machine

- 打开 PowerShell
- 输入 `docker-machine create -d virtualbox default`
  - 如果使用 vmwareworkstation 驱动，请到 [Github](https://github.com/pecigonzalo/docker-machine-vmwareworkstation/releases) 下载，将文件放置在 C:\ProgramData\DockerDesktop\version-bin`
  - 安装 Vmware Workstation Pro 15
  - `docker-machine create -d vmwareworkstation default`

## 设置环境变量（选其一）

### 设置系统环境变量

- 打开 windows 环境变量设置，此电脑->属性->高级系统设置->环境变量
- 分别新建三个环境变量为
  - DOCKER_HOST
    - 值：使用 docker-machine ls 获得 ![dmls](https://user-images.githubusercontent.com/59110636/89162726-0c400b80-d5a7-11ea-8b6f-61cb1d76473d.png)
    - tcp://192.168.99.102:2376

  - DOCKER_TLS_VERIFY
    - 值：1
  - DOCKER_CERT_PATH
    - 值：`%USERPROFILE%/.docker/machine/machines/default`

### 设置 终端环境变量
- docker-machine.exe env default | Invoke-Expression
- code

## 测试
- 打开 PowerShell 输入 `docker run hello-world`
- 无错误即成功

## 设置共享路径
- 打开 VirtualBox 设置共享文件夹
- 如果不设置在启动 docker 容器时不能挂载文件

## 设置端口映射
- 打开 VirtualBox 网络设置，进行端口映射设置
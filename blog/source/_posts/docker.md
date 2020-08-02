# Docker 

## Docker 是什么
- [简单介绍](https://juejin.im/post/5b260ec26fb9a00e8e4b031a)

## 安装 Docker
- 使用脚本安装
    - `curl -fsSL https://get.docker.com | VERSION=19.03.1 bash -s docker --mirror Aliyun`
    - `VERSION=19.03.1` 安装指定版本，不指定为最新版
    - `--mirror Aliyun` 使用阿里云镜像源加速
- 建立 docker 组
    ```shell
    sudo groupadd docker
    sudo usermod -aG docker $USER
    ```
- 启动 Docker CE
    ```sheji
    sudo systemctl enable docker
    sudo systemctl start docker
    ```
- 退出当前终端并注销重新登录
- 配置镜像加速
    ```
    sudo mkdir -p /etc/docker
    sudo tee /etc/docker/daemon.json <<-'EOF'
    {
        "registry-mirrors": ["https://registry.docker-cn.com"]
    }
    EOF
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

# 简单命令
- [官方文档](https://docs.docker.com/engine/reference/commandline/cli/)
- 获取镜像: docker pull `<image>[:<tag>]`
    - example: docker pull mongo:3.6
    - tag 为空，会默认为 latest ，即最新版本
- 运行容器: docker run [-p `[host_ip]:<host_port>:<container_port>] [-v [host_folder:]<container_folder>] [-d] [--rm] [--name <container_name>] <image>[:<tag>]`
    - example: `docker run -p 27017:27017 -d --rm --name my_mongo mongo:3.6`
    - -p 为主机端口和容器端口的映射
    - -v 为挂载主机目录到容器
    - -d 后台运行容器
    - --rm 关闭容器后自动删除
- 进入到容器: docker exec -it <container_name> command
    - example: `docker exec -it my_mongo bash`
- 删除镜像: `docker rmi <image>[:<tag>]`
    - 删除 TAG 为 none 的镜像: `docker images | grep none | awk '{print $3}' | xargs docker rmi`
- 保存镜像: `docker save <image>[:<tag>] -o filename`
    - 压缩保存：`docker save <image>[:<tag>] | gzip > filename`
- 导入镜像: `docker load -i filename`
    - 批量导入镜像: `ls -1 *.tar.gz | xargs --no-run-if-empty -L 1 docker load -i`
- 镜像迁移到另一个机器: `docker save <image>[:<tag>] | bzip2 | pv | ssh <username>@<hostname> 'cat | docker load'`
- 私有仓库登录: docker login
    - [出现错误](https://stackoverflow.com/questions/42211380/add-insecure-registry-to-docker)：`Error response from daemon: Get https://your host/v2/: x509: cannot validate certificate for your host because it doesn't contain any IP SANs`
    - 解决方法: 在 `/etc/docker/daemon.json`(没有此文件自行新建) 添加
    ```json
    {
        "insecure-registries" : [ "your docker hub host" ]
    }
    ```
    - 然后重启 docker
        ```shell
        sudo systemctl daemon-reload
        sudo systemctl restart docker
        ```


## Dockerfile
- [官方文档](https://docs.docker.com/engine/reference/builder/)

- **注意**：
    - 构建过程中优先执行结果不经常变更的内容（例如 安装系统依赖和Python第三方包）
    - Dockerfile 中的每一条命令都会生个可读层 layer ，命令尽量合成一个一并执行
    - 能写到 Docker compose file 中的一些配置，就写到 Docker compose file 里面 (比如 环境变量)
    - 尽量减少镜像大小（1.安装依赖后清除缓存和下载的安装包，2.删除不需要的文件，中间生成文件，等等）
    - 纯粹的数据卷容器，可以是关闭状态，只要有一个容器挂载了数据卷，数据就会一直存在

- `FROM <image>[:<tag>] [AS <name>]`
    - `<image>[:<tag>]` 以 image 作为基底构建镜像，tag 为空，默认为 latest
    - `[AS <name>]` 添加构建别名，如果 Dockerfile 中有多个 `FROM` 即可添加别名，构建时使用 `--target` 参数可以指定构建哪一个 
- ENTRYPOINT 和 CMD
    - 建议使用 exec 格式
    
- 多个 `.dockerignore` 文件 [Link](https://github.com/moby/moby/issues/12886#issuecomment-480575928)
    - Docker 版本 19.03+
    - `export DOCKER_BUILDKIT=1`
    - dockerignore 文件名为 `< Dockerfile name>.dockerignore`



## Docker compose-file
- [官方文档](https://docs.docker.com/compose/compose-file/)

- **注意**：
    - 使用 Docker compose file 可以使用 `-f` 同时指定多个文件，同一个服务的不同配置会自动合并，而相同的配置将会出错

- depends_on
    - 设置容器的依赖关系，控制容器的启动顺序

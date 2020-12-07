

# Docker 版本 < 18
## Docker 修改docker0 网桥的默认IP
- 停止并删除使用docker0网桥的所有容器
- 修改配置文件

- vim /etc/docker/daemon.json
```json
{
    "bip": "172.200.0.1/24"
}
```

 - 使之生效的命令如下：

```bash
systemctl stop docker
ip link set dev docker0 down
brctl delbr docker0
systemctl start docker
```



## 修改 docker 自定义网桥网段
- 停止并删除使用自定义网桥的所有容器
- 删除网桥: `docker network rm <network name>`
- docker-compose 中修改配置

```yaml
networks:
  default:
    driver: bridge
    ipam:
      config:
        - subnet: 172.201.0.0/16
```
- 使用 docker-compose 重新启动容器



# Docker 版本 18+
- 停止并删除使用自定义网桥的所有容器
- 删除网桥: `docker network rm <network name>`
- 修改docker配置文件
- vim /etc/docker/daemon.json

```json
{
    "bip": "172.200.0.1/24",
    "default-address-pools": [
    {
        "base": "172.201.0.0/16",
        "size": 24
        }
    ]
}
```
- 重启docker systemctl restart docker



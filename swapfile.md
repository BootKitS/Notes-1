## swapfile 交换文件 大小修改
- 查看 swapfile 详情：`sudo swapon -s`
- 禁用：`sudo swapoff /swapfile`
- 删除：`sudo rm /swapfile`
- 新建:：`sudo dd if=/dev/zero of=/swapfile bs=1G count=8`
- 设置权限：`sudo chmod 600 /swapfile`
- 设置格式化：`sudo mkswap /swapfile`
- 启用：`sudo swapon /swapfile`
- `/etc/fstab` 增加一行 `/swapfile swap swap defaults 0 0`
- 文件可相应改为分区
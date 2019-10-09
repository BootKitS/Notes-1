## Centos7 安装 PPTP

- 参考: 
  - [链接1](http://www.voidcn.com/article/p-gzwmgmpw-kv.html)
  - [链接2](http://blog.sina.com.cn/s/blog_beebb7590102wqh5.html)
  - [链接3](https://www.alibabacloud.com/help/zh/faq-detail/41345.htm#CentOSVPNclient)
  - [链接4](http://www.linuxdiyf.com/linux/31936.html)
  - [链接5](https://blog.csdn.net/liangxin95/article/details/79733180)

- 安装依赖：yum install -y `ppp pptp pptp-setup`
- 配置：`pptpsetup --create vpn --server <服务器> --username <用户名> --password <密码> --encrypt --start`
  - MPPE加密，pptpsetup时不需要使用–encrypt
  - 出现 `LCP: timeout sending Config-Requests
        Connection terminated.` 可能是防火墙的问题
- 配置路由：
  - `route -n`
  - `ip route replace default dev ppp0` or `route add -net 192.168.1.0/24 gw 192.168.1.1 dev ppp0`

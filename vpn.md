## Centos7 安装 PPTP

- 参考: 
  - [链接一](http://www.voidcn.com/article/p-gzwmgmpw-kv.html)
  - [链接二](http://blog.sina.com.cn/s/blog_beebb7590102wqh5.html)

- 安装依赖：yum install -y `ppp pptp pptp-setup`
- 配置：`pptpsetup --create vpn --server <服务器> --username <用户名> --password <密码> --encrypt --start`
  - MPPE加密，pptpsetup时不需要使用–encrypt
  - 出现 `LCP: timeout sending Config-Requests
        Connection terminated.` 可能是防火墙的问题
- 配置路由：
  - `route -n`
  - `route add -net 0.0.0.0 dev ppp0` (所有对外网络都通过ppp0路由)
  - `ip route replace default dev ppp0` (和上面二选一，设置缺省路由)
  - `route add default dev ppp0`

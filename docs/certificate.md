## 系统安装 CA 证书 [链接](https://www.bounca.org/tutorials/install_root_certificate.html)
- chrome 无法信任 [链接](https://stackoverflow.com/questions/7580508/getting-chrome-to-accept-self-signed-localhost-certificate)

## Centos7 信任证书

- 拷贝证书到目录 `/etc/pki/ca-trust/source/anchors/`
- 然后执行 `update-ca-trust`

## Python 中使用 requests 访问自签名网站时出现错误

- [链接1](https://unix.stackexchange.com/questions/90450/adding-a-self-signed-certificate-to-the-trusted-list)
- [链接2](https://stackoverflow.com/questions/30405867/how-to-get-python-requests-to-trust-a-self-signed-ssl-certificate)

## 使用 openssl 创建 CA 证书和自签名证书 
- [链接](https://docs.azure.cn/zh-cn/articles/azure-operations-guide/application-gateway/aog-application-gateway-howto-create-self-signed-cert-via-openssl#%E5%88%9B%E5%BB%BA%E8%87%AA%E7%AD%BE-ca-%E8%AF%81%E4%B9%A6)


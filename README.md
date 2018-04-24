# 插件式的信息爬虫

本项目运行在可以运行在本地或者服务器端

## Todo
- [ ] Python 插件化信息管理，可拓展
- [ ] 信息保存到 Github 仓库
- [ ] Docker 一键部署到本地或服务器

## Json 格式

```json
{
  "code": 0,
  "type": "weather",
  "date": "2018-04-23 20:18:03",
  "content": {}
}
```

**参数说明**

- `code`: `0` 成功、`-1` 失败
- `type`: [`weather`, `stock`, `news`] 待补充
- `date`: 发起请求的时间
- `content`: 获取的 Json 信息，保存到文件
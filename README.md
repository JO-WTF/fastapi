# FastAPI 示例项目

这是一个最简单的 FastAPI 应用程序，包含一个 GET 接口和一个 POST 接口。

## 运行方法

1. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

2. 使用 Uvicorn 启动服务：

   ```bash
   uvicorn main:app --reload
   ```

3. 接口说明：
   - `GET /`：返回欢迎信息。

     **请求示例：**

     ```bash
     curl http://127.0.0.1:8000/
     ```

   - `POST /items`：接收一个包含 `name` 和可选 `description` 字段的 JSON 对象，并返回该对象。

     **请求示例：**

     ```bash
     curl -X POST http://127.0.0.1:8000/items \
       -H "Content-Type: application/json" \
       -d '{"name": "Sample Item", "description": "An example item."}'
     ```

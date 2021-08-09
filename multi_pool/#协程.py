import asyncio


async def request(url):
    print('正在请求的url是', url)
    print('请求成功', url)
    return url

# async 修饰的函数，调用之后返回一个协程对象
s = request('www.baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(s)

# # task的使用
# loop = asyncio.get_event_loop()
# # 基于loop 创建一个task对象
# task = loop.create_task(s)
# print(task)
# # 注册并启动task对象
# loop.run_until_complete(task)
# print(task)

# #future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(s)
# print(task)
# loop.run_until_complete(task)
# print(task)


def call_back_func(task):
    print(task.result())
# 绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(s)
task.add_done_callback(call_back_func)
loop.run_until_complete(task)


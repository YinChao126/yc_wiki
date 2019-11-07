# json操作大全

作者：尹超

日期：2019-11-7


## dumps 字典变字符串

```
test_dict = {"key": "value"}
print(type(test_dict)， test_dict)
json_str = json.dumps(test_dict)#dumps 将数据转换成字符串
print(type(json_str)， json_str)
```

## loads 字符串变字典

特别注意：此时字符串的key和value必须是双引号，单引号不认识的！！！

```
json_str = "{\"key\":\"value\"}"
print(type(json_str)， json_str)
json_dict = json.loads(json_str)
print(type(json_dict)， json_dict)
```

## dump 将字典数据写入json文件中

    json_str = "{\"key\":\"value\"}"
    print(json_str)
    json_dict = json.loads(json_str)
    with open("test.json", "w") as fh:
        json.dump(json_dict, fh)  #写入文件
## load 打开json文件并读为字典

```
json_str = "{\"key\":\"value\"}"
json_dict = json.loads(json_str)
with open("test.json", "w") as fh:
	json.dump(json_dict, fh)
	
with open("test.json",'r') as load_f: 
    load_dict = json.load(load_f) #读入字典
    print(load_dict)
```

## 注意事项

不支持注释

最后一行的逗号不能留【yaml可以】

推荐总是用双引号
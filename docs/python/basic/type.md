# 数据类型转换

作者：尹超

日期：2019-7-1

描述：本文详细记录了python的各种数据类型转换

## string to bytes

```python
b_var = str_var.encode('utf-8') #方法1
b_var = str.encode(str_var) #方法2
```

## bytes to string

```python
str_var = b_var.decode('utf-8') #方法1
str_var = bytes.decode(b_var) #方法2
```

## list to bytes

```python
b_var = list(list_var)
```

## bytes to list 

```python
list_var = bytes(b_var)
```

## dict to bytes 

```python
def dict_to_bytes(the_dict):
    s = json.dumps(the_dict)
    return s.encode()
```

## bytes to dict 

```python
def bytes_to_dict(the_bytes):
    temp = json.loads(the_bytes.decode())
    return temp
```

## dict to binary 

```python
def dict_to_binary(the_dict):
    t_str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in t_str)
    return binary
```

## binary to dict 

```python
def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d
```

## float to bytes

```
import struct
float_data = 12.908
bytes_data = bytearray(struct.pack("f", float_data))
list_data = list(bytes_data)
```

## bytes to float

```
import struct
bytes_data = b'ffNA'
float_data = struct.unpack("f", bytes_data)[0]
```

## long int to array

```
a = 1570602960
list_a = a.to_bytes(4, byteorder='big')
```

## array to long int

```
a = b']\x9d\x7f\xd0'
int_value = int.from_bytes(a,byteorder='big',signed='True')
```


# makefile demo

描述：一个通用makefile模板，改改就能用

```
OP = -std=c++11 -pthread -O2 -L [./lib/] -l[your_lib1] -l[your_lab2] -L [path2] -l[your_lib3]


TARGET = $(notdir $(CURDIR))
SOURCES = $(wildcard *.cpp)
HEADERS = $(wildcard *.h)

$(TARGET) : $(SOURCES) $(HEADERS)
	g++ -o your_app $(SOURCES) $(OP) 

clean:
	rm *.o your_app
```


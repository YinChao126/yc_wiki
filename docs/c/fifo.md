# FIFO

## keywords

FIFO, c, driver

描述：一个通用的FIFO库

```
#ifndef __GENERIC_FIFO_H
#define __GENERIC_FIFO_H
#include <mutex>

#define DEV_64K_ADDR_WIDTH 18
using namespace std;

template <class T>
class cGenericFIFO
{
public:
	cGenericFIFO();
	~cGenericFIFO();

	void InitSize(uint8_t AddrBitWidth);
	bool Write(T DataIn[], uint32_t DataLen);
	bool Read(T DataOut[], uint32_t DataLen);
	uint32_t ForceRead(T DataOut[], uint32_t DataLen);
	uint32_t BufferSize();
	uint32_t DataCount();

private:
	bool InitFlag;
	uint32_t BufSize;
	uint32_t BufAddrBitMap;

	T *DataBuf;
	uint32_t DataCnt;
	uint32_t RdAddr;
	uint32_t WeAddr;
	mutex Locker;
};

template <class T>
cGenericFIFO<T>::cGenericFIFO()
{
	InitFlag = false;
}

template <class T>
cGenericFIFO<T>::~cGenericFIFO()
{
	if (InitFlag)
	{
		delete[] DataBuf;
	}
}

template <class T>
void cGenericFIFO<T>::InitSize(uint8_t AddrBitWidth)
{
	if (InitFlag == false)
	{
		BufSize = (1 << AddrBitWidth);
		BufAddrBitMap = BufSize - 1;
		DataBuf = new T[BufSize];
		InitFlag = true;
	}
	DataCnt = 0;
	RdAddr = 0;
	WeAddr = 0;
}

template <class T>
bool cGenericFIFO<T>::Write(T DataIn[], uint32_t DataLen)
{
	if (((DataCnt + DataLen) > BufSize) || (InitFlag == false))
	{
		return false;
	}

	Locker.lock();

	for (uint32_t i = 0; i < DataLen; i++)
	{
		DataBuf[WeAddr] = DataIn[i];
		WeAddr = (WeAddr + 1) & BufAddrBitMap;
	}
	DataCnt += DataLen;

	Locker.unlock();
	return true;
}

template <class T>
bool cGenericFIFO<T>::Read(T DataOut[], uint32_t DataLen)
{
	if ((DataLen > DataCnt) || (InitFlag == false))
	{
		return false;
	}

	Locker.lock();

	for (uint32_t i = 0; i < DataLen; i++)
	{
		DataOut[i] = DataBuf[RdAddr];
		RdAddr = (RdAddr + 1) & BufAddrBitMap;
	}
	DataCnt -= DataLen;

	Locker.unlock();
	return true;
}

template <class T>
uint32_t cGenericFIFO<T>::ForceRead(T DataOut[], uint32_t DataLen)
{
	if (InitFlag == false)
	{
		return 0;
	}
	uint32_t OutLen = (DataLen > DataCnt) ? DataCnt : DataLen;

	Locker.lock();

	for (uint32_t i = 0; i < OutLen; i++)
	{
		DataOut[i] = DataBuf[RdAddr];
		RdAddr = (RdAddr + 1) & BufAddrBitMap;
	}
	DataCnt -= OutLen;

	Locker.unlock();
	return OutLen;
}

template <class T>
uint32_t cGenericFIFO<T>::BufferSize()
{
	return BufSize;
}

template <class T>
uint32_t cGenericFIFO<T>::DataCount()
{
	return DataCnt;
}

#endif

```


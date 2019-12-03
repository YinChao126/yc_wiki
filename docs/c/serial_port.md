# Linux SerialPort Driver

## keywords

linux, c++, serial port, com port, driver

## 说明

本模块是搜集来的Linux系统串口驱动，直接可用。

## SerialPort.h

```
#ifndef __LINUX_SERIAL_PORT_H
#define __LINUX_SERIAL_PORT_H

//#define SIM_MODE


#include<stdio.h>

#ifndef SIM_MODE
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<termios.h>
#include<errno.h>
#include<string.h>
#endif

#define PORT_IDLE	0
#define PORT_OPEN	1
#define PORT_READY	2

class cUart
{
public:
	cUart();
	~cUart();

	bool Open(const char* Port);
	void Close();

	bool Init(int Speed, int FlowCtrl, int DataBits, int StopBits, char Parity);
	bool Send(unsigned char *SendBuf, int DataLen);
	int Recv(unsigned char *RecvBuf, int DataLen);

private:
	int fd;
	int fd_flag;
};

#endif

```

## SerialPort.cpp

```
#include "SerialPort.h"


cUart::cUart()
{
	fd_flag = PORT_IDLE;
}

cUart::~cUart()
{
	Close();
}

bool cUart::Open(const char* Port)
{
	if (fd_flag == PORT_IDLE)
	{
#ifndef SIM_MODE
		fd = open(Port, O_RDWR | O_NOCTTY | O_NDELAY);
		if (fd < 0)
		{
			printf("can't open device: %s\n", Port);
			return false;
		}
		//fcntl(fd, F_SETFL, FNDELAY);
		if (fcntl(fd, F_SETFL, 0) < 0)
		{
			printf("fcntl failed!\n");
			return false;
		}
		//if (0 == isatty(STDIN_FILENO))
		//{
		//	printf("standard input is not a terminal device!\n");
		//	return false;
		//}
		printf("UartPort:%d, %s is opened\n", fd, Port);
#endif
		fd_flag = PORT_OPEN;
	}
	return true;
}

void cUart::Close()
{
#ifndef SIM_MODE
	if (fd_flag != PORT_IDLE)
	{
		close(fd);
		printf("UartPort:%d is closed\n", fd);
	}
#endif
	fd_flag = PORT_IDLE;
}

// Init(9600,0,8,1,'N');
bool cUart::Init(int Speed, int FlowCtrl, int DataBits, int StopBits, char Parity)
{
	if (fd_flag == PORT_IDLE)
	{
		return false;
	}

#ifndef SIM_MODE
	int speed_arr[] = { B115200, B19200, B9600, B4800, B2400, B1200, B300, B115200, B19200, B9600, B4800, B2400, B1200, B300 };
	int name_arr[] = { 115200, 19200, 9600, 4800, 2400, 1200, 300, 115200, 19200, 9600, 4800, 2400, 1200, 300 };
	struct termios options;
	
	if (tcgetattr(fd, &options) != 0)
	{
		printf("SetupSerial 1\n");
		return false;
	}

	for (int i = 0; i < sizeof(speed_arr) / sizeof(int); i++)
	{
		if (Speed == name_arr[i])
		{
			cfsetispeed(&options, speed_arr[i]);
			cfsetospeed(&options, speed_arr[i]);
		}
	}
	options.c_cflag |= CLOCAL;
	options.c_cflag |= CREAD;

	switch (FlowCtrl)
	{
	case 0:
		options.c_cflag &= ~CRTSCTS;
		break;
	case 1:
		options.c_cflag |= CRTSCTS;
		break;
	case 2:
		options.c_cflag |= IXON | IXOFF | IXANY;
		break;
	}

	options.c_cflag &= ~CSIZE;
	switch (DataBits)
	{
	case 5:
		options.c_cflag |= CS5;
		break;
	case 6:
		options.c_cflag |= CS6;
		break;
	case 7:
		options.c_cflag |= CS7;
		break;
	case 8:
		options.c_cflag |= CS8;
		break;
	default:
		printf("Unsupported data size!\n");
		return false;
	}

	switch (Parity)
	{
	case 'n':
	case 'N':
		options.c_cflag &= ~PARENB;
		options.c_iflag &= ~INPCK;
		break;
	case 'o':
	case 'O':
		options.c_cflag |= (PARODD | PARENB);
		options.c_iflag |= INPCK;
		break;
	case 'e':
	case 'E':
		options.c_cflag |= PARENB;
		options.c_cflag &= ~PARODD;
		options.c_iflag |= INPCK;
		break;
	case 's':
	case 'S':
		options.c_cflag &= ~PARENB;
		options.c_cflag &= ~CSTOPB;
		break;
	default:
		printf("Unsupported parity!\n");
		return false;
	}

	switch (StopBits)
	{
	case 1:
		options.c_cflag &= ~CSTOPB;
		break;
	case 2:
		options.c_cflag |= CSTOPB;
		break;
	default:
		printf("Unsupported stop bits!\n");
		return false;
	}

	// 屏蔽Linux串口驱动对回车和换行的特殊处理
	options.c_iflag &= ~ (INLCR | ICRNL | IGNCR);
	options.c_oflag &= ~(ONLCR | OCRNL);
	options.c_iflag &= ~(IXON);

	options.c_lflag &= ~(ICANON | ECHO | ECHOE | ISIG);  /*Input*/
	options.c_oflag &= ~OPOST;   /*Output*/

	options.c_cc[VTIME] = 1;
	options.c_cc[VMIN] = 1;

	tcflush(fd, TCIFLUSH);

	if (tcsetattr(fd, TCSANOW, &options) != 0)
	{
		printf("com set error!\n");
		return false;
	}
#endif

	fd_flag = PORT_READY;
	return true;
}

bool cUart::Send(unsigned char *SendBuf, int DataLen)
{
	if (fd_flag != PORT_READY)
	{
		return false;
	}

#ifndef SIM_MODE
	if (write(fd, SendBuf, DataLen) != DataLen)
	{
		tcflush(fd, TCOFLUSH);
		return false;
	}
#endif
	
	return true;
}

int cUart::Recv(unsigned char *RecvBuf, int DataLen)
{
	if (fd_flag != PORT_READY)
	{
		return 0;
	}

#ifndef SIM_MODE
	struct timeval timeout;
	timeout.tv_sec = 0;
	timeout.tv_usec = 500;

	fd_set fs_read;
	FD_ZERO(&fs_read);
	FD_SET(fd, &fs_read);

	int fs_sel = select(fd + 1, &fs_read, NULL, NULL, &timeout);
	if (fs_sel)
	{
		return read(fd, RecvBuf, DataLen);
	}
#endif

	return 0;
}

```


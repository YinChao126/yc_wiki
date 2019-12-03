# Ubuntu 修改开机画面

作者：蒙宇明

日期：2019-11-25

## keywords

linux,  ubuntu, startup

## 开机显示部分

相关文件: `/etc/default/grub`.

### 不显示任何信息(黑屏)

修改配置文件以下内容:

```bash
GRUB_CMDLINE_LINUX_DEFAULT=quiet
GRUB_CMDLINE_LINUX="console=tty12"
```

### 只显示文本信息

修改配置文件以下内容:

```bash
GRUB_CMDLINE_LINUX_DEFAULT=quiet
GRUB_CMDLINE_LINUX=""
```
### 显示指定LOG等级的文本信息

```bash
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=4"
GRUB_CMDLINE_LINUX=""
```

### 显示开机动画

```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
```

### 配置生效

修改完成后输入以下命令:

```bash
sudo update-grub
```
重启后生效.

## 开机动画(ubuntu-logo)

相关文件路径: `/usr/share/plymouth/themes/ubuntu-logo`

### LOGO 替换

替换主题路径下的 `ubuntu-logo.png` 图片.

### 背景色修改

分为两部分: `GRUB` 中一闪而过的背景色和显示进度的背景色.

#### GRUB

相关文件: `ubuntu-logo.grub`

```bash
# 修改前3个参数.
if background_color 0,0,0,0; then
  clear
fi
```

#### 主体部分

相关文件: `ubuntu-logo.script`

修改配置文件以下内容:

```bash
# #ffffff
# 换算: 每个byte除以255.
Window.SetBackgroundTopColor (1.0, 1.0, 1.0);     # Nice colour on top of the screen fading to
Window.SetBackgroundBottomColor (1.0, 1.0, 1.0);  # an equally nice colour on the bottom
```
这两个设置不同颜色时, 会出现渐变色效果;

### 配置生效

修改完成后输入以下命令:

```bash
sudo update-initramfs  -u
```

重启后生效.

## 其他动画主题

### 安装

1. 将其它主题放到 `/usr/share/plymouth/themes` 目录下;
2. 输入以下命令生成选项:
```bash
sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/{your_theme_dir}/{your_theme.plymouth} 100
```

### 选择生效

```bash
sudo update-alternatives --config default.plymouth
```

根据提示选择使用的动画主题.

```bash
sudo update-initramfs  -u
```

重启后生效.
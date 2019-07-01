# 版本回滚

## 1. 本地回滚

### 1.1 返回到前几个版本

```
git reset --hard head^  //回退到head的前一个版本
git reset --hard head~x //回退到head的前x个版本
```

### 1.2 超级回退，回退到任意节点

```python
git reflog  #此处获取想要回滚点的commit id
git reset --hard OldCommitId
```

## 2. 远程回滚

先本地回滚

再强退到远程分支： git push -f
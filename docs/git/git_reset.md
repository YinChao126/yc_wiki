# 版本回滚

## 1. 本地回滚

```python
git reflog  #此处获取想要回滚点的commit id
git reset --hard OldCommitId
```

## 2. 远程回滚

先本地回滚

再强退到远程分支： git push -f
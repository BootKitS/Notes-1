## command

- `rsync -azvhP --delete --exclude .git/ <SRC> <host>:<DST>`
  - `--delete` 删除那些 DST 中 SRC 没有的文件
  - `--exclude` 指定排除不需要传输的文件模式

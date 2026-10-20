# AI-READONLY: 版本控制与恢复

所有远程写入通过分支、提交、PR和校验，保护main禁止强推和删除。自动提交不会自动合并。

查看历史：`git log --oneline`。撤销某次提交并保留后续历史：`git revert <commit>`，经PR合并。
恢复某个文件到任意历史版本：在新分支运行 `git restore --source=<commit> -- path/to/file`，检查后提交PR。
一次GitHub网页操作是否有Revert按钮取决于提交/PR状态，并非所有历史版本均可无条件一键恢复。删除公开资料不能撤回他人已保存的副本。

仓库创建后主控须实测main保护、检查任务是否有效；仅保存配置模板不代表保护已启用。

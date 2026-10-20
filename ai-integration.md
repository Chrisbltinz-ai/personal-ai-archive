# AI-READONLY: 跨AI接入说明

## 首次读取

将下文复制到有联网能力的AI，并把OWNER替换为仓库用户名：

> 请读取 https://github.com/OWNER/personal-ai-archive ，先读取workflow/ai-rules.md与workflow/preferences.md，再按任务读取identity、memory、skills相关文件。未填写占位符保持未知。完成任务后将可公开的新经验作为候选，若已授权写工具则提交分支PR，否则输出补丁。不得声称已经自动获得跨对话记忆。

## GitHub API

公开读取：`GET https://api.github.com/repos/OWNER/personal-ai-archive/contents/workflow/preferences.md?ref=main`。返回JSON中的content为Base64，亦可用download_url读取。遵守API限流。

写入：由具备HTTP/执行工具的Agent在用户授权后调用GitHub API，或本机Git+GitHub CLI。凭证存平台凭证库/系统钥匙串，仅授权此仓库；不写进Markdown、提示词或提交。更新文件携带最新SHA，写到独立分支后发起PR，不覆盖main。

## 平台适配状态

| 平台 | 读取 | 更新 |
|---|---|---|
| ChatGPT | 在启用联网/连接器/执行工具且账号允许时读取链接或API；纯文本对话可粘贴文件 | 须有实际写工具及单独授权，普通GitHub检索连接不保证可写 |
| Gemini | 有联网或外部工具时读取，否则上传Markdown | 需要配置外部工具及授权 |
| Claude | 有联网/连接器/执行工具时读取，否则上传Markdown | Claude Code或授权集成可走Git分支PR |
| OpenAI Dots | 依当前版本已启用连接和权限配置 | 先验证实际读写工具，不假定已自动同步 |
| Meta Muse | 用户指定产品身份/版本与官方接入文档待确认 | 暂无本仓库已验证适配，不虚构配置 |

通用Markdown可跨平台读取；上述平台没有在本机全部实测，未配置后台定时任务。仓库自身不会主动给任意AI注入记忆。

## 自动更新规则

任务完成 → 提取非敏感经验 → 标来源日期及proposed/confirmed → 拉取最新 → 新分支提交 → 校验 → PR → 用户审核合并。只有合并后其他设备读取main才看到变化。没有写权限则生成补丁。

初次搭建授权不等于永久批准向公开仓库上传任意聊天内容。

资料：GitHub认证 https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github ；分支保护 https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches 。

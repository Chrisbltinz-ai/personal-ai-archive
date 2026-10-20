# AI-READONLY: 搭建交付报告

- 日期：2026-10-20
- GitHub账号：Chrisbltinz-ai
- 仓库：https://github.com/Chrisbltinz-ai/personal-ai-archive
- 可见性：public
- identity/：身份与目标占位模板，AI默认只读
- workflow/：习惯、沟通与任务规则、恢复说明
- memory/：偏好、决定、经验模板，带来源和确认状态
- skills/：个人能力计划及6个可移植AI技能通用版
- archive/：历史项目索引与本报告
- 接入：ai-integration.md，AGENTS.md，CLAUDE.md，GEMINI.md
- 原始个人SKILL：没有批量公开，6项通用版不包含店铺资料或依赖；不是原件完整迁移
- 本地检查：必需文件、UTF-8、AI标签与常见密钥格式校验通过
- 首次GitHub Actions：Archive check / validate成功
- main保护：已通过API配置并回读；必需PR、validate成功及分支更新；禁止强推和删除，管理员也受约束
- PR审批：0位额外审批人；单人仓库可在检查通过后自行合并，并非独立双人审核
- 版本恢复：git revert撤销提交，或新分支git restore --source=<commit>恢复文件后PR合并
- 自动写入：仅约定任务后提议分支PR；尚未部署各平台后台同步、定时轮询或自动合并
- ChatGPT/Gemini/Claude/Dots：提供读取与授权写入方法，未在全部平台逐一实测
- Meta Muse：具体产品和官方接入文档待确认，不宣称已接入

快速开始：把本仓库链接发给具有联网读取工具的AI，要求先读workflow/ai-rules.md和workflow/preferences.md。无联网时直接上传相关Markdown文件。内容写入公开仓库前需核对公开适宜性。

核对远程保护：gh api repos/Chrisbltinz-ai/personal-ai-archive/branches/main/protection。

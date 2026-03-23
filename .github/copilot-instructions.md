# Copilot 指引

## 项目简介

本项目是基于 CPM Estuary Mod 修改的 Kodi 皮肤（`skin.cpm.estuary.search`），主要面向运行 CoreELEC/LibreELEC 的 Amlogic 安卓盒子。

## 目录结构

- `xml/` — 所有 UI 界面的 XML 文件（主要修改区域）
- `language/` — 多语言翻译文件（`.po` 格式），皮肤自定义字符串从 `31000` 开始
- `themes/` — UI 主题定义
- `addon.xml` — 插件清单文件

## 电源菜单（DialogButtonMenu.xml）

电源菜单定义在 `xml/DialogButtonMenu.xml`，包含以下操作项：

| 标签字符串 ID | 动作 | 显示条件 |
|---|---|---|
| `$LOCALIZE[13012]` 退出 | `Quit()` | `System.ShowExitButton` |
| `$LOCALIZE[13016]` 关机 | `Powerdown()` | `System.CanPowerDown` |
| `$LOCALIZE[20150]` 定时关机 | `AlarmClock(shutdowntimer,Shutdown())` | `!System.HasAlarm(shutdowntimer)` |
| `$LOCALIZE[13011]` **待机** | **`Suspend()`** | **`System.CanSuspend`** |
| `$LOCALIZE[13010]` 休眠 | `Hibernate()` | `System.CanHibernate` |
| `$LOCALIZE[13013]` 重启 | `Reset()` | `System.CanReboot` |
| Reboot from eMMC/NAND | `System.ExecWait("/usr/sbin/rebootfromnand")` + `Reset()` | `System.PathExist("/dev/system") \| System.PathExist("/dev/userdata") \| System.PathExist("/dev/env")` |
| Restart Kodi | `RestartApp()` | 始终显示 |

### 待机（`$LOCALIZE[13011]`）

- **动作**：`Suspend()`
- **显示条件**：`System.CanSuspend`
- **注意**：在纯 Android 系统上 `System.CanSuspend` 为 `false`，待机按钮不会显示。CoreELEC/LibreELEC 下该条件为 `true`，`Suspend()` 可正常触发系统待机。

同一套待机逻辑也出现在 `xml/script-skinshortcuts-includes.xml` 中的电源子菜单（group `33060`），
可通过搜索 `labelID>13011` 或 `Suspend()` 定位。

## 皮肤自定义字符串

皮肤语言文件位于 `language/resource.language.*/strings.po`，
自定义字符串 ID 范围为 `31000`–`31999`。
Kodi 核心字符串（如 `13011`、`13016` 等）直接使用 `$LOCALIZE[]` 引用，无需在皮肤语言文件中重复定义。

好，下面给你一版 **更像 GitHub 风格、简洁一点、直接可用的 README**：

---

# Get-Your-Lesson-Easily

> For a better school life

一个基于 **Selenium** 的选课捡漏脚本。  
原本用于在第二轮 / 第三轮选课期间监控课程容量，有空位时提醒用户，帮助及时选上目标课程。

## Status

> **Deprecated / 失效项目**

由于教务系统已更新，本项目当前**无法直接使用**，现仅作为旧项目存档与学习参考。

## Features

- 自动打开教务系统页面
- 监控目标课程容量变化
- 检测到空位时发出提醒

## Requirements

- Python 3
- Selenium
- 浏览器驱动（需自行下载并配置）

## Usage

1. 安装依赖
2. 下载对应浏览器驱动
3. 准备项目所需的 **两个 `.txt` 文件**
4. 运行脚本

```bash
pip install selenium
python main.py
```

> 请将 `main.py` 替换为你的实际入口文件名。

## Notes

- **两个 txt 文件是必要的**
- 本项目依赖旧版教务系统页面结构
- 教务系统更新后，原有脚本逻辑已失效

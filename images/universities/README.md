# 大学Logo获取指南

## 📋 需要添加的Logo

您需要将以下两所大学的logo添加到此目录：

1. **pku-logo.png** - 北京大学校徽
2. **jlu-logo.png** - 吉林大学校徽

## 🔍 如何获取Logo

### 方法 1: 官方网站下载（推荐）

#### 北京大学校徽
1. 访问北京大学视觉形象识别系统：
   ```
   https://www.pku.edu.cn/
   ```
2. 在网站底部或"关于北大"部分查找"视觉识别系统"或"VI下载"
3. 下载校徽的PNG格式文件
4. 重命名为 `pku-logo.png`

或者直接使用：
- 北大logo官方色：深红色 #8C1515
- 搜索"北京大学 logo PNG transparent"

#### 吉林大学校徽
1. 访问吉林大学党委宣传部：
   ```
   https://xcb.jlu.edu.cn/
   ```
2. 查找"下载专区"或"视觉识别系统"
3. 下载校徽矢量版或PNG格式
4. 重命名为 `jlu-logo.png`

### 方法 2: 在线资源

您也可以从以下渠道获取：

1. **维基百科**
   - 搜索"北京大学"和"吉林大学"
   - 点击校徽图片，下载高清版本

2. **大学官方公众号**
   - 从学校官方微信公众号保存校徽图片

3. **图片搜索**
   - 使用 Google Images 或百度图片
   - 搜索关键词："北京大学校徽 PNG"、"吉林大学logo PNG"
   - 选择清晰、透明背景的版本

## 📐 Logo规格要求

- **格式**: PNG（推荐，支持透明背景）
- **尺寸**: 建议 200x200 像素或更高（会自动缩放到60x60）
- **背景**: 透明背景最佳（如果是白色背景也可以）
- **文件大小**: 建议小于 500KB

## 📁 如何添加Logo

1. 下载或准备好两个logo文件
2. 确保文件名为：
   - `pku-logo.png` （北京大学）
   - `jlu-logo.png` （吉林大学）
3. 将文件放入此目录：
   ```
   /Users/wangwenxia/code/wenxia.github.io/images/universities/
   ```
4. 提交到 git：
   ```bash
   cd /Users/wangwenxia/code/wenxia.github.io
   git add images/universities/
   git commit -m "添加大学logo"
   git push origin main
   ```

## 🎨 Logo示例位置

Logo将显示在您的学术主页的教育背景部分：
- 每个学位旁边会显示对应大学的校徽
- 尺寸：60x60 像素
- 位置：学位信息左侧

## ✅ 验证

添加logo后，访问您的网站：
```
https://WangWenxia2026.github.io
```

检查教育背景部分是否正确显示logo。

## 💡 提示

- 如果logo不显示，请检查文件名是否完全匹配
- 确保文件格式为 PNG
- 检查文件路径是否正确
- 清除浏览器缓存后重新访问

---

**当前状态**: ⏳ 等待添加logo文件

**已完成**: ✅ 代码已准备好，只需添加图片文件

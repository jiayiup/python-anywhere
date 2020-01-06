# Python期末项目总结
[pythonanywhere](http://jjyy2.pythonanywhere.com/)
- github文档（templates、static、app.py、数据文档）
- 上述文档都存放在github页面中，请上移页面查看。

## 一、HTML档描述
### 此作业共制作了7个页面
- 每一个页面中都运用了<form> 标签中的action属性创建 HTML 表单并提交。
- 同时使用 {{ }} 语法表示变量，替换py中数据列表
  
- P1：显示主题内容：日益变胖的地球人。并定义了首页前端和后端的路径，简单的GRT让页面显示html的内容
- P2：2018年世界人口BMI平均指数，页面显示plotly的可视化世界地图。放置图在前端显示，使用post路径，把成果.html当文字档读入成字符串存入results.html
- P3：图表内容为世界地区肥胖症发生率。在以上的基础上做了下拉选框，让数据内容随着选择框选择变化而变化
- P4：图表主题为：不同发展国家由于超重而引发的患病率分析。用了tab栏，可切换图表内容
- P5：图表主题为：肥胖是早期死亡的主要危险因素之一
- P6：图表主题为：全球肥胖死亡占比分析
- P7：总结，并结束


  
## 二 python档描述
- 在python档中赋予不同html文件不同的跳转地址并且开展出不同功能，实现python文档与html文档的数据交互
- 运用到结构嵌套在页面中嵌套数据交互可视化数据图表。pyecharts的模块画散点、条形图等，并将部分图以html文件的方式导出
- pandas读csv文件（文件内路径与pythonanywhere不同）
- methods (GET、POST) 

## 三 WEBapp动作描述
- 在每一个页面左上角设有一个跳转按钮“下一页”，点击即可跳转至下一页
- 与P2设下拉选择框，选择不同的选项然后点击下拉框下面的“Do it”即可跳转到对应的国家查看可视化图

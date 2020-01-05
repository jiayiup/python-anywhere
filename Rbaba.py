from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import folium
from folium import plugins
import plotly.express as px
import plotly as py
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected='True')
import plotly.graph_objs as go



app = Flask(__name__)
df7 = pd.read_csv('成人肥胖症发生率_country.csv', encoding="utf8", \
                  keep_default_na=False, na_values='na_rep')
regions_available_loaded = list(df7.Region.dropna().unique())
# 准备工作
# pandas 大法读内容, 用dropna()丢缺失值, 用uniqu
# e()取唯一值, 不重覆
df = pd.read_csv('BMI.csv',encoding="utf8",\
                 keep_default_na=False, na_values='na_rep')


@app.route('/',methods=['GET'])
def hu_run_2019():
   return render_template('p1.html')

@app.route('/p2',methods=['POST'])
def hu_run_select() -> 'html':
    df = pd.read_csv('BMI.csv', encoding="utf8", \
                     keep_default_na=False, na_values='na_rep')


    fig = go.Figure(
        data=go.Choropleth(
            locations=df['ISO'],
            z=df['Both sexes'],
            text=df['Country'],
            colorscale='geyser',
            autocolorscale=False,
            reversescale=False,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_tickprefix='%',
            colorbar_title='人口BMI平均指数',
        ))

    fig.update_layout(
        title_text='2018年世界人口BMI平均指数',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='eckert4',
        ),
        annotations=[dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="http://apps.who.int/gho/data/?theme=main">\
                World Health Organization</a>',
            showarrow=False
        )]
    )

    fig.show()

    py.offline.plot(fig, filename="results2.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("results2.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    return render_template('p2.html',
                            the_plot_all = plot_all)





@app.route('/p3',methods=['POST'])
def hu_run_select2() -> 'html':
    df1 = pd.read_csv('成人肥胖症发生率_country.csv', encoding="utf8", \
                      keep_default_na=False, na_values='na_rep')

    import plotly.express as px

    fig = px.scatter(df1, x="Male", y="Female",
                     size="Both sexes", color="Both sexes",
                     hover_name="Country", log_x=True, size_max=60)
    fig.show()

    py.offline.plot(fig, filename="results2.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("results2.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    return render_template('p3.html',
                            the_plot_all2 = plot_all)



@app.route('/p4',methods=['POST'])
def hu_run_select3() -> 'html':
    df2 = pd.read_csv('超重患病率_youth_adult.csv', encoding="utf8", \
                      keep_default_na=False, na_values='na_rep')

    region = list(df2.Region.dropna().unique())

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=region,
            y=list(df2.Youth),
            name='青少年（5-17岁）',
            marker_color='indianred'))

    fig.add_trace(
        go.Bar(
            x=region,
            y=list(df2.Y_Male),
            name='男性（青少年）',
            marker_color='cadetblue'))

    fig.add_trace(
        go.Bar(
            x=region,
            y=list(df2.Y_Female),
            name='女性（青少年）',
            marker_color='lightpink'))

    fig.add_trace(
        go.Bar(
            x=region,
            y=list(df2.Adult),
            name='成年人（18岁以上）',
            marker_color='lightsalmon'))

    fig.add_trace(
        go.Bar(
            x=region,
            y=list(df2.A_Male),
            name='男性（成年人）',
            marker_color='steelblue'))

    fig.add_trace(
        go.Bar(
            x=region,
            y=list(df2.A_Female),
            name='女性（成年人）',
            marker_color='plum'))

    fig.update_layout(
        updatemenus=[
            go.layout.Updatemenu(
                type="buttons",
                direction="right",
                active=0,
                x=0.57,
                y=1.2,
                buttons=list([

                    dict(label="ALL",
                         method="update",
                         args=[{"visible": [True, True, True, True, True, True]},
                               {"title": "不同年龄与性别之间的超重患病率", }]),

                    dict(label="Both",
                         method="update",
                         args=[{"visible": [True, False, False, True, False, False]},
                               {"title": "青少年与成年人超重患病率", }]),

                    dict(label="Youth",
                         method="update",
                         args=[{"visible": [False, True, True, False, False, False]},
                               {"title": "青少年男女不同的超重患病率"}]),

                    dict(label="Adult",
                         method="update",
                         args=[{"visible": [False, False, False, False, True, True]},
                               {"title": "成年人男女不同的超重患病率", }]),

                ]),
            )
        ])

    fig.update_layout(
        title_text="超重引起的患病率",
        xaxis_domain=[0.05, 1.0]
    )

    fig.show()

    py.offline.plot(fig, filename="results2.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("results2.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    return render_template('p4.html',
                            the_plot_all3 = plot_all)




@app.route('/p5',methods=['POST'])
def hu_run_select4() -> 'html':
    df3 = pd.read_csv('不同风险因素造成的死亡人数.csv', encoding="utf8", \
                      keep_default_na=False, na_values='na_rep')

    import plotly.express as px
    fig = px.bar(df3, x="Value", y="Reason", orientation='h', animation_frame="Year")
    fig.update_layout(
        height=700,
        title_text='全球因不同风险因素死亡的数据分析',

    )
    fig.show()

    py.offline.plot(fig, filename="results2.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("results2.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    return render_template('p5.html',
                            the_plot_all4 = plot_all)


@app.route('/p6',methods=['POST'])
def hu_run_select5() -> 'html':
    df4 = pd.read_csv('Five_Region.csv', encoding="utf8", \
                      keep_default_na=False, na_values='na_rep')

    import plotly.express as px
    df = px.data.gapminder()
    fig = px.scatter(df4, x="每10万中因肥胖而死亡的人数", y="肥胖死亡占比", animation_frame="Year", animation_group="Entity",
                     size="肥胖死亡占比", color="Region", hover_name="Entity",
                     log_x=True, size_max=40, range_x=[10, 350], range_y=[0, 40])
    fig.show()
    py.offline.plot(fig, filename="results2.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("results2.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    return render_template('p6.html',
                            the_plot_all5 = plot_all)


@app.route('/p7',methods=['POST'])

def hu_run_select6() -> 'html':
    return render_template('p7.html')


@app.route('/p3',methods=['GET'])
def hu_run_2019_1():
    regions_available = regions_available_loaded#下拉选单有内容

    fig = px.scatter(df7, x="Male", y="Female",
                     size="Both sexes", color="Both sexes",
                     hover_name="Country", log_x=True, size_max=60)
    fig.show()

    py.offline.plot(fig, filename="results2.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("results2.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    return render_template('p3.html',
                           the_select_region=regions_available,
                           the_plot_all = plot_all)


@app.route('/world_BMI',methods=['POST'])
def hu_run_select7() -> 'html':

    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region)

    dfs = df7.query("Region=='{}'".format(the_region))

    fig = px.scatter(dfs, x="Male", y="Female",
                     size="Both sexes", color="Both sexes",
                     hover_name="Country", log_x=True, size_max=60)
    fig.show()

    py.offline.plot(fig, filename="成果.html", auto_open=False)  # 備出"成果.html"檔案之交互圖
    with open("成果.html", encoding="utf8", mode="r") as f:  # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    regions_available =  regions_available_loaded #下拉选单有内容
    return render_template('p3.html',
                            the_plot_all = plot_all,
                            the_select_region=regions_available,
                           )



if __name__ == '__main__':
    app.run(debug=True, port = 8040)


# 基于互联网翻译引擎的平行句对自动构造系统 ✨
## BackTranslationCorpusConstruction 
基于互联网翻译引擎的平行句对自动构造系统，使用数据回译方式利用互联网上公开翻译引擎对大量单语数据进行批量翻译达到数据增强的目的。本项目利用了谷歌翻译、百度翻译和有道翻译三大互联网翻译引擎资源。
### 回译
Back Translation（BT，回译）就是常用的一种基于单语的数据增强方法。
其原理是这样的：首先，利用平行语料训练一个反向模型，如对于英翻中，首先训练一个中翻英的模型；然后，对于目标语言的单语数据，利用反向模型将其翻译成源语言数据，这样我们就得到了一批新的平行语料。

    本项目采取了一种另类的回译思想，借助互联网上的翻译引擎资源，对单语数据进行连续两次翻译，通过比较原文和回译得到
    的文本的相似度决定是否采用该双语句对。如果相似度达到了一定阈值，可以将该句对加入标准库用来训练机器翻译模型。
### 下载安装
- 下载源码

      下载源码:git clone git@github.com:neverneverendup/BackTranslationCorpusConstruction.git
      或者直接到 https://github.com/neverneverendup/BackTranslationCorpusConstruction 下载zip文件
    
- 安装依赖
 
        pip install -r requirements.txt
   
### 使用
- 配置

      配置文件为config.py，参数包括单语数据的文件位置，语料源语种，目标语种以及是否使用ip代理。
      语种id对应关系 1: '中文', 2: '英文', 3: '日文' , 4: '法文', 5: '韩文 , 6: '俄文'
      param =  {   
                'data_file' : 'Data/中文单语语料.txt',    
                'from_lan' : 1,   
                'to_lan' : 2,   
                'use_proxy' : False
       }


- 启动

      main.py会读取配置文件，启动多个爬虫线程进行数据翻译。
      >>>python main.py

- 日志

      Log文件夹下会有每个翻译引擎对应的翻译日志，记录了翻译速度以及可能出现的翻译错误。


### 扩展
- 代理

    系统预留了使用代理的接口。为了保证大规模单语数据的正常翻译，建议使用代理https://github.com/jhao104/proxy_pool。
    设置好代理之后，确保代理port正确，修改配置文件use_proxy参数即可使用代理。
- 相似度计算
     
    现在使用tf算法对文本向量化，然后计算文本的余弦相似度比较相似度。当然有更好的相似度计算方法，建议比较一下效果后使用。
 
- 单语数据

    大家可以再构造一个单语数据库与本项目对接，爬取互联网上丰富的单语数据进行存储，作为本项目的数据源，然后利用本项目的回译算法获得高质量的双语句对。

### 最后
   这是本人大四实习时实践的一个小项目，原项目包含数据库部分，由于涉及私密数据就不公开了。项目很小，只是给大家提供一个思路，谢谢😁。

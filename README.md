# Text_processing
使用自然语言处理相关算法完成对文章相关性的判断
## Synopsis 项目大纲
对于一个给定的目标文件，里面有多篇文章。针对每篇文章，需要在一个给定文章数据库中寻找与之有关联的文章，并且根据其相关性进行正排序。判断相关性的算法使用TF-IDF算法。目标文章与数据库文章中有许多常用词，例如 am，was，very等，使用一个stop_list的一个词汇表进行过滤。具体TF-IDF算法可以通过[TF-IDF与余弦相似性的应用](http://www.ruanyifeng.com/blog/2013/03/tf-idf.html)，[TF-IDF及其算法](http://www.cnblogs.com/biyeymyhjob/archive/2012/07/17/2595249.html)进行了解。
## Motivation 创作动机
此项目是Text Processing课程的课程设计,占总成绩的50%。
## Installation 如何安装
下载此项目，在命令行窗口将文件目标路径定位到此文件夹。执行project.py函数
### HELP 操作
在命令行里面输入python project.py -h，能够在命令行里面显示帮助信息。
### Stoplist 过滤表
在命令行里面输入python project.py -s stop_list.txt，能够导入过滤表的内容，以便于进行下一步的程序操作。
### Queries and Documents 目标文章文件以及数据库文章文件
在命令行里面输入python project.py -c documents.txt -i queries.txt，能够导入目标文章文件以及数据库文章文件。
## Tests 项目运行效果
在程序执行过程中，一共会产生3个文件
### IndexDocuments.txt
这个文件中存放的是针对数据库文件得出的tf-idf的数据结构，根据{word:{id:{’tf’,’id’,’tf*idf’}}}的结构按照每个单词序排列。
![](https://github.com/frayds/Text_processing/raw/master/demo_pictures/IndexDocument.png)
### IndexQueries.txt
这个文件中存放的是针对目标文件得出的tf的数据结构，根据{id:{wd:’tf’}}的结构按照文章顺序排列。
![](https://github.com/frayds/Text_processing/raw/master/demo_pictures/IndexQueries.png)
### DocSort.txt
这个文件中存放的是整个程序的运行结果
![](https://github.com/frayds/Text_processing/raw/master/demo_pictures/DocSort.png)
## Contributors 参与者介绍
濮一帆:advanced Computer Science, Department of Computer Science, University of Sheffield

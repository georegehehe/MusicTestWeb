# Manual
### 整体介绍
> 1. :6musictest-web是一个网页谱曲应用, 技术上采用前后端分离式开发, 合并部署方案.
> 2. Backend采用flask和melodia技术, 实现了音频上传, 音符识别,调用musictest的原有代码完成混音.
> 2. Frontend采用vue技术, 操作H5的canvas实现曲谱绘制与录音和播放
###  部署说明
> 1. 准备好musictest, 确保机器联网.
> 2. Copy musictest-web工程内的代码到musictest.列表如下
>   1.  app.py  web工程的主程序.
>   1.  audio_to_midi_melodia.py 利用melodia为app.py提供音符识别服务, 利用norepeatmusictheory.py为app.py提供混音服务.  
>   1.  norepeatmusictheory.py  只多了一行copy finalversion.wav到static目录的代码.
>   1.  static/**  ui代码的放置目录, 目录里面是npm build之后的vue的html和js还有css.
>   1.  templates/index.html musictest-web唯一的ui页面入口, 引用static/**的代码展示界面.
>   1.  requirements-web.txt 罗列musictest-web依赖的python模组, 只有numpy明确版本1.6.x, 其余模组安装最新版即可.
>   1.  MTG-MELODIA*  音符识别关键技术melodia所依赖的vamp需要额外安装的lib文件, 下文会解释用法. 
> 3. 安装额外的C基础库
>   1. 为了音符识别关键技术melodia正确运行, 除了安装一些python模组以外, 还需要安装一些C语言开发的工具.
>   1. 首先确保osx已经安装了homebrew https://brew.sh
>   1. 用brew install命令分别安装fluidsynth, ffmpeg,sonic-visualiser.
>   1. MTG-MELODIA 1.0 (OSX universal)_0.zip 文件解压后, 内容copy到/Library/Audio/Plug-Ins/Vamp 这一步千万别忘了.
> 4. 安装python的site-packages
>   1. numpy==1.6.1 这个1.7以后的版本要求python3.5环境, 所以只能选择1.6.x安装.
>   1. SoundFile
>   1. resampy
>   1. vamp
>   1. MIDIUtil
>   1. jams
>   1. scipy
>   1. pandas
>   1. flask
> 5. 尝试运行
>   1. 首先用pycharm的代码检查功能, 确保第2步的所有代码编译均通过.
>   2. 运行app.py, 不论是用terminal运行./venv/bin/python app.py 还是利用pycharm打开它鼠标右击选择run都可以.
>   3. 确认console输出* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
>   4. 如果抛出异常, 证明2到4步的步骤有遗漏, 请根据log查找需要安装的site-package或者c库, 补充完整即运行app.py.
>   5. 使用chrome或者firefox访问localhost:5000, 可以看到ui界面, 然后就可以尝试录音和谱曲了.
>   6. ui上一边操作, 一边可以看到pycharm的console输出日志.
###  后台Backend代码开发说明
> 1. 核心代码说明
>   1. app.py 它利用flask的decorator语法@app.route('url'), 发布了/ /humming /mix 三个web接口, 他们分别可以使用浏览器http://localhost:5000/, http://localhost:5000/humming http://localhost:5000/mix来测试.
>   2. /接口没有逻辑, 它只是把templates/index.html的内容传递给浏览器, index.html里面的vue代码会命令浏览器展示曲谱界面和交互按钮.
>   3. /humming接口, 它从浏览器传递回来的audioData参数中获取到音频文件, 并保存在./static/humming.wav(可以试着录音之后播放看看), 然后调用audio_to_midi_melodia.py下的audio_to_midi_notes抽取关键音符列表.
>       1. soundfile组件能将波形文件转化成数据流.
>       1. vamp.collect采样流中的各个HZ值.
>       1. hz2midi Hz值按照h = 12 log2(fm / C0).公式转成音名和音高, 比如440 = A-4
>       1. 收集好所有的音符之后, 按照 [节拍, 时长, 音符名-音高]的格式储存在列表里.
>       1. 调用然后调用audio_to_midi_melodia的notes_to_ui函数, 把格式转化成 [音符名-音高|ui节拍横坐标],列表转json格式传递回浏览器.
>       1. 整体上, humming接口配合ui界面上的"麦克风"按键, 完成了录音->识别音符->展示音符的功能. 
>   4. /mix接口, 它接受浏览器传递过来的[音符名-音高|ui节拍横坐标]列表,把它转化成norepeatmusictheory.determinelefthand的入参.
>       1. 首先,从浏览器的曲谱面板中, 获得notes参数, 这时还是['C-4|16','G-4|32']这样的格式.
>       1. 补充节拍,调用fill_ui_beats如果0,4,8,12,16,20,24,28,32的节拍, 如果为空则补充['None|节拍''].
>       1. 格式转化, 调用ui_beats_to_notes把每个音符节拍改成[节拍, 时长, 音符名-音高].
>       1. 补充节拍2, 根据时长, 把所有空缺的时间填充上None,避免righthand混音截断.
>       1. 利用os.system调用实现准备好的shell, 以shell方式调用norepeatmusictheory.determinelefthand.
>       1. os.system("rm -rf ./musicpiece*")清理musicpiece* 临时目录(避免服务器硬盘装满).
>       1. 调用notes_to_ui把处理好的[节拍, 时长, 音符名-音高]重新转化成[音符名-音高|ui节拍横坐标],返回给浏览器.
> 2. 一些技巧和陷阱
>   1. 为什么用shell调用norepeatmusictheory.determinelefthand而不是直接python调用? 
>       1. 因为python直接调用2次以上, determinelefthand会假死.
>       1. 怀疑fluidsynth的底层代码应该有释放资源的功能, 而而determinelefthand没有处理好造成资源锁死没有处理好造成资源锁死.
>       1. shell在运行结束后强行释放资源, 所以借用shell快速解决了这个问题.
>   1. humming接口和mix接口很"吃网速".
>       1. humming会上传接近4m的wav文件, mix则会命令浏览器下载接近6m左右的wav文件.
>       1. 如果网速不畅, 浏览器的录音和mix都会执行失败.        
###  前端Frontend代码开发说明
> 1. 前端代码开发, 部署概述
>   1. musictest-web的static和templates目录下是经过编译和压缩的代码, 不推荐直接修改. 
>   1. 编译和压缩前的源代码, 在https://github.com/keel2008GitHub/musictest-ui提供下载.
>   1. musictest-ui是vue技术实现的, 它使用typescript语法, 需要使用npm工具管理代码.
>   1. npm可以用homebrew install node来安装, osx默认也有, 但版本比较旧无法完成开发, 推荐升级到12.10版本.
>   1. 下载源代码后, 在musictest-ui目录下运行一次npm install(只需刚下载时运行一次), 然后运行npm run build, 会出现dist子目录, 内部是copy到musictest-web的static目录和Templates目录编译后代码.
> 1. 核心代码说明
>   1. src/components/MusicalNote/index.vue 曲谱绘板, 最重要的ui组件, 绘制纵35,横128的坐标面板, 识别鼠标点击绘制音符.
>       1. export default {props: { 部分,定义绘板内的表格, 音符点, 曲线的颜色和宽度.
>       1.  data() { return { 部分, 定义了dotList, 记录所有音符.
>       1. methods: {部分, 堆放js事件处理代码, 根据drawCoordinateLine, 读取dotList绘制面板, 包括drawDotList鼠标点击添加, 鼠标双机删除, drawCurve绘制点之间的贝塞尔曲线.
>   2. src/App.vue index.html的布局代码, 调用上述MusicalNote绘制面板, 并在下方提供录音, 混音, 清除, about几个按钮.
>       1. export default { 部分主要是布局MusicalNote组件.
>       1. methods: { 部分主要是各种js效果, handlerPlay在展示播放进度条,deleteData调用MusicalNote清空面板, startRecord响应麦克风按钮, 完成录音和上传(调用src/js/record.js), mixHas接受混音按钮把dotList发给后台完成混音.
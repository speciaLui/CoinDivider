# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。
# 遊戲腳本位於此檔案。

# 宣告該遊戲使用的角色。 color 參數
# 為角色的名稱著色。


define xv = Character("???")

define q = Character("齊拉奈")

define qq = Character("齊拉奈", color="#1c28fc")

define h = Character("海町宇恩")

define l = Character("「琉璃」")

define t = Character("樓蘭塔塔")

define sh = Character("「本石黛」")

define flag=0

image trans:
    "images/trans.png"
    zoom 0.5



    

# 遊戲從這裡開始。

label start:
    $ yuen=0
    $ tata=0
    play music tutorial_text volume 0.2
    scene avenue:
        zoom 0.5
    q "今天真是個晴朗的一天。"
    q "但是，襪靠，遲到啦"
    "剛剛中山路日常塞車，1路車又日常操作"
    "難道今天真的要遲到嗎?"
    q "嗚嗚嗚......"
    q "......欸? 那個難不成是?"
    show sui at center
    "是歐日!他也被塞車了!"
    q "看來他正在等電梯，那我還是去爬樓梯好了"
    q "主要是兩個人搭電梯太折磨了，除非有電梯音樂"
    "(祈願蘊真樓電梯音樂實裝)"
    q "......"

    show sui looking:
        xpos 0.5
        ypos 1.2
    
    # stop music
    # renpy.music.set_volume(0.0,0,music)
    play sound vine_boom
    # renpy.music.set_volume(1.0,0,music)
    q "!!!"
    q "難不成...我被發現了!"
    q "不~~~~~~~~~~~~"
    "歐日" ".........?"
    hide sui_looking
    show sui at center
    # play music tutorial_text
    q "呃......"
    q "他好像沒發現我..."
    q "那沒事了，總之，先上去吧"

    # scene black with dissolve
    stop music
    scene trans with dissolve
    pause 1.5
    scene classroom with dissolve
    "就這樣，兩(1.5)堂電腦課過去......"
    

    "早上兩節電腦課太舒服了"
    "如果沒有冗員就更好了就是"
    "{color=#f00}如果有那種可以把冗員都炸死的法術就好了{/color}"
    "......唉，罷了"
    "話說英文課在第八節超級舒服"
    "不過，等等就要上體育課。"
    "更甚如此，體育成績要看800還是太難繃了。"

    q "唉~~~~"
    xv "大清早的，你嘆啥子氣啊?"
    show yuen_n:
        zoom 0.5
        xpos 0.25
        ypos 0.25
    with dissolve
    play music magic_girl volume 0.1
    "眼前出現的是我的摯友 海町宇恩。"
    q "待會就得在操場狂奔三圈，然後滿身大汗精疲力竭\n讓本就渾渾噩噩的一天更加雪上加霜，真是太叫人興奮啦。"

    h "反正你上什麼都是在睡覺，雖然體育課你睡不了覺就是"
    h "不過既然待會兒的兩堂國文課你也必定在睡\n那何不活動一番再睡呢？"
    q "阿但是，先睡和後睡是有差異的阿!"
    q "這就跟吃火鍋先吃冰還是後吃冰，兩者是不一樣的"
    h "但是你睡著了還不是都是睡"
    h "你睡著了也跟掛了有差別，那你要不要把「長眠」一詞給轉型正義掉阿"
    q "別了吧，我又不是那啥【政治狂熱分子｜七英鳥】，幹嘛要搞這種無意義的轉型正義"
    h "是這樣，但不是這樣!!!"
    q "哈哈"

    h "話說、我想問你一個很難問題"
    q "問阿，只要不是農場高中物理考古題裡那種「無尾熊【擲｜赤】石」這種問題都沒事"
    h "沒問題"
    h "(畢竟我也不會)"
    h "總之、有一艘船航行，邊航行邊把他的每一個零件都一一換掉"
    h "那他最後還是原來那艘船嗎?"
    q "呃，要看你換零件的方法吧"
    h "霍、怎麼說?"
    q "你想、假設像人體，我們每天都在飲食與代謝，也就是說我們的身體天天都在換零件"
    q "然而你著實不會注意到你的變化，是故，你還是你"
    q "不過當零件大到足以凌駕或是超過本體的話，那恐怕就不是原來的船了"
    q "因為他有區間不平滑"
    h "所以你是說，重點在於自己有沒有察覺?"
    q "【是的｜sodayo】"
    h "嘛，你還真有那甚麼量子力學天賦"
    h "但我倒是覺得這就像水面上下的白楊樹一般"
    h "比起實體的船，我們對船的認識更像是對他的熟悉與信賴"
    h "就像計程車，你只能認得它的外型卻不會認識車本身，而車主不同"
    h "每輛車對車主都是獨一無二的，也因此再怎麼修理那也依舊是他的愛車"
    h "是故，嘛，我與你的見解其實相似，我覺得重點在於認知"
    q "霍，這麼有認知，這是甚麼形而上學嗎?"
    h "我也不清楚"
    q "話說，是不是該去上體育課了?"
    h "嗯嗯，走吧"
    "於是乎，我自案前起身。"
    "......"

    show red:
        alpha 0.5
    
    stop music
    q "唔!?"
    play music wierd fadein 3 volume 0.25


    "眼前一片腥紅"
    "不知怎麼地，我一從座位上起身，眼前便一陣暈眩，眼前彷彿一波亂訊流經，意識模糊，教室解離重構閃爍無數卡茲"

    q "你咋了???"

    "不行...搞不好是昨天太晚睡了?嘶......"
    menu:
        "該怎麼辦呢?"
        "和宇恩說明狀況":
            $ yuen+=1
            jump A1
        "大丈夫一咬牙就過了":
            jump B1

label A1:
    $ eat = 0
    q "突然眼前有些暈......"
    h "......啊?"
    q "就是，感覺眼前雜訊頻頻，亂碼淅淅零零，兩三點露不成雨，七八個星猶在天。"
    q "而且還聽到神人音樂\n如果神人算神的話，這裡就是天堂了"
    h "我......你先閉上眼睛吧。"
    q "太刺激啦!"
    q "不過閉上還是看的到你欸"
    "......"
    h "總之你先休息一下，幫你量個脈搏"
    h "頃刻便可"

    "我照著做，忽覺腦門一熱"
    "明明閉著雙眼，可我彷彿感受到身體有某種光束貫穿，彷彿身體溢入天聽"
    "......"
    "有些熟悉卻又陌生的畫面此時自意識流中閃過"
    scene black with dissolve
    xv "統領！沙阿已經佔領大半個礦區了！"
    xv "別管我了!快點撤離吧，統領!!!"
    xv "琉璃，快，快些帶走統領...!"
    scene red with fade
    "......"
    "........."
    menu:
        "..."
        "......":
            pass
        "......":
            pass
        "......":
            pass
    "......"
    scene white
    q "嗚、嗚呃!"
    pause 1.0
    scene classroom
    stop music
    show yuen_n:
        zoom 0.5
        xpos 0.25
        ypos 0.25
    with dissolve
    h "怎麼樣，你看到啥子了?"

    q "只是一些奇怪的畫面而已(其實我甚麼都沒看到)"
    q "哈哈，我怎麼會做這樣的夢。"
    h "......"
    h "真的沒什麼事嗎?"
    q "沒事沒事"
    h "內個、話說你今天放學有事嗎?"
    q "沒事啊，怎了?有甚麼事嗎?"
    h "有些事...嘿嘿"
    q "...?事兒事兒的"
    q "行吧，反正也沒事"
    jump S2

label B1:
    $ eat = 1
    q "沒...沒事，大抵是低血糖了"
    h "啊? 行吧，要不要吃塊牛奶糖?"
    "說罷，宇恩從腰間的口袋掏出了一顆"
    h "諾。"
    q "行，謝啦"
    "立刻服用，頓感輕快不少"
    hide red with dissolve
    stop music
    q "豁然開朗"
    h "好吃吧? 要不要再來一顆?"
    q "晚點吧，等等還要跑步呢"
    h "也是"
    jump S2

label S2:
    
    "其他同學" "欸，走了啦，等等又要被記遲到了"
    q "啊? 好的，走吧"
    scene trans with dissolve
    pause 1.5
    scene bg_sports
    with dissolve
    play music magic_girl volume 0.25

    "操場上依舊是那幅熟悉的景象。"
    "太陽夯報了，彷彿在提醒我們這些高中牲："
    "『你們這些gen z 有夠菜，直接給到拉完了。』"
    show yuen_n:
        zoom 0.5
        xpos 0.25
        ypos 0.25
    with dissolve
    h "等一下要4分鐘內喔，你加油啦。"
    q "乾，我會不會來不及跑完阿"
    q "而且，不是4分半嗎"
    h "有差嗎? 你練習兩年半你也不是蔡\n徐坤阿"
    q "6"

    "體育老師吹了哨子。"
    show yuen_n:
        # zoom 0.2
        xpos 0.25
        ypos 0.25
        ease 2 xpos 1.5
    pause 2.0
    hide yuen_n
    "於是我開始向前"
    "............"

    q "哈……哈……這個距離誰設計的……"
    "腿像被灌了鉛，肺在抗議，靈魂已經先跑去排大太屋了。"
    "話說等等午餐要吃甚麼"

    h "呼呼呼~"
    q "......!?"
    show yuen_n:
        zoom 0.2
        offscreenleft
        ease 2 xpos 1.5
    "只見宇恩再次經過我"
    "麻了，他怎麼跑這麼快"
    "......不管了，總之先跑吧"


    scene trans with dissolve
    pause 1.5
    scene campus_path with dissolve
    stop music

    "勉強撐到終點線，我整個人快揮發了。"
    "......"
    "結果就這樣躺著，不知覺光陰稍縱即逝"
    stop music
    play sound bell_ring
    "阿不對，怎麼打鐘了"
    q "……不行，我得去買喝的。"
    q "......?"
    q "宇恩怎麼不見了?"
    q "......算了，我自己先去吧"

    scene aimai:
        zoom 2
    with dissolve
    stop sound
    "我拖著雙腿移入福利社。"
    "兩側有各式飲料"
    "好像來到主題樂園一樣，真令人興奮欸~~~"
    "恩?這個是!?"

    q "（拿起）沃，這不是義大利嗎?還有這般好貨!"
    q "只不過他要25欸……，喝完這個我中午就只能吃土了"
    q "嚶嚶嚶，難不成我只能喝買香了嗎"
    q "......"

    q "算了，不喝也罷……大概……"

    xv "欸？咋了？你不喝了？"

    q "嗯？"

    play music "tata_theme.mp3" volume 0.5
    show roulan_tata at center with dissolve
    "轉過頭，是一個看起來嬌小的學妹，制服袖子稍微捲起，眼神亮晶晶的"

    t "學長你是不是……忘記帶錢？"
    q "……呃……並非……好吧，其實我只是突然想喝點別的啦，哈哈…"
    t "你那個臉，看起來像剛被錢包背刺的人。"
    q "呃...君子固窮..."
    t "說人話。"
    q "沒錢"
    t "嘿嘿，好可憐"
    t "要不，我請你吧？"
    q "!?"
    q "這、這、阿?"

    "什麼？學妹請客？這劇情發展怎麼有點夢幻？"


    menu:
        "要怎麼回答？"
        "A.『...恭敬不如從命』":
            jump T1
        "B.『不行不行，怎麼能讓學妹請我呢？』":
            jump T2

label T1:
    q "那我就選這瓶了，謝啦"
    t "嗯嗯~小事~"
    $ tata+=1
    jump S3

label T2:
    q "不、不行，畢竟素未謀面，再怎麼說這也太突然了"
    t "沒關係啦，看你快倒了，我怕你再多看一眼就會爆炸"
    q "......"
    q "好吧，再做推辭反倒是我的失禮，那麼就謝謝你了"
    t "嘿嘿~學長你真有禮貌"
    q "那必須的"
    jump S3

label S3:
    "Bi--"
    "......"
    scene campus_path:
        zoom 0.5
    
    with dissolve
    show roulan_tata with dissolve
    "塔塔幫我結完帳，把飲料遞過來。"
    q "謝、謝謝你"
    t "不用客氣~總想說之前在哪裡見過你，想說學長是何方神聖"
    q "阿？是這麼一回事嗎？那真是巧"
    t "是的呢~"
    q "話說，你叫甚麼名字呀？"
    t "我叫樓蘭塔塔，西域的樓蘭，巴別的塔塔，是高一的學生喔"
    q "搜嘎"
    q "我是齊拉奈，是......"
    t "313班的齊拉奈學長對吧？"
    q "哇，你怎麼知..."
    "阿這，難不成這是......"
    "{b}豔遇!?{/b}"
    t "呃...我剛剛看到你的飯卡了"
    q "啊?是嗎?"
    "確實我方才有打開皮夾"
    "雖說沒有錢就是了"
    q "話說，你那瓶飲料是甚麼味道的呀"
    t "?"
    t "這是你想喝的意思嗎?"
    q "嗯..."
    q "確實"
    show roulan_tata flush
    t "........."
    t "那..."
    q "不過比起這個，你項鍊上的那顆寶石是啥呀"
    q "從來沒見過呢"
    t "......"
    show roulan_tata sus
    t "{b}KISAMA{/b}"
    q "是"
    t "......"
    t "學長是不是處男呀？"
    q "呃......是這麼一回事，呃，等等，處男似乎不是這麼用的"
    t "那是怎麼用的呢"
    q "........."
    "總覺得亂回答會出事"
    show roulan_tata
    t "...唉、算了"
    
    t "總之，其實我有收集珠寶的興趣，不過這個玉是我家裡傳下來的"
    show roulan_tata plain
    "說罷，塔塔伸手摸了摸項鍊上的玉墜，遂將其取下，婆娑半晌"
    t "......這玉墜的質地很特別"
    t "你想摸摸看嗎?"
    q "欸？甚好"
    q "heheheha"
    "我爰伸手接過玉墜"
    t "小心點喔"
    q ".........!"
    "頗為光滑細膩，黑色的質地卻亮澤如鏡，其中卻又映照出了名黃色的光芒"
    "莫非...這就是所謂的玄色? 不對，其乃更甚於玄色"
    "因為它有......"
    "少女的體溫!?"
    t "學長，你還好嗎？"
    q "欸黑、欸嘿嘿"
    t "呃......【最低｜さいてい】......"
    q "抱歉抱歉，我只是有點激動"
    q "這玉墜真是太美了，那畫面太美了，而我竟有些發暈"
    t "話說，你的臉色怎麼有些發白啊"
    q "啊，沒事的，我只是剛跑完1600有些累罷了"
    q "等等..休息一下就好......"
    # show roulan_tata_found
    t "!!!"
    t "學長，你怎麼了!?"
    "忽然間，我感到一陣暈眩"
    scene black
    "隨之眼前一黑"
    q "......"
    stop music fadeout 3.0
    scene trans with dissolve
    pause 1.5
    scene black with dissolve
    jump Jan1
    return

label Jan1:
    xv "大統領...我們又見面了......"
    q "你、你是誰?"
    play music "wierd.mp3" volume 0.5
    scene night_street with dissolve
    show bernstein:
        zoom 2.0
        xpos 0.3
        ypos 0.3
    with dissolve
    xv "呵..."
    xv "我是舊世界的投影，你可以叫我本石黛"
    sh "你現在身處於世界之外"
    q "世界之外?這是甚麼駭客任務嗎?"
    sh "這並不重要"
    sh "重要的是，你必須做出選擇"
    sh "有人說，命運是掌握在自己手中"
    sh "然而也有人說，命運是早已註定好的"
    sh "今天姑且不討論弦論與圈量子引力論的艱澀問題，只談你的選擇"
    sh "你認為：命運是被注定的嗎？"
    menu:
        "......"
        "{color=#f00}命運是被注定的{/color}":
            $ flag=1
        "{color=#f00}命運不是被注定的(不要選，還沒做){/color}":
            $ flag=2
        "{color=#f00}咕咕嘎嘎（DEATH）{/color}":
            play music bird volume 0.25
            sh "哈哈哈，看來世界線重塑似乎毀了你的智商"
            sh "真是可惜"
            sh "不過沒關係，你很快就會忘記這一切的"
            sh "再見了，我們曾經的領袖"
            hide bernstein with dissolve
            "......"
            scene classroom
            "就這樣，我回到了原本的世界"
            "然後我便忘記了這一切"
            "雖然身旁異樣頻頻，但我依舊過著單身平凡的生活"
            "{b}.:. the End (咕咕嘎嘎end) .:.{/b}"
            return


    if flag==1:
        sh "嗯姆嗯姆，有趣的選擇"
        sh "那麼你便會接受你所面對的一切{cps=*0.5}......{/cps}或許吧"
        sh "這或許是最有責任感的選擇"

    elif flag==2:
        sh "既然你相信命運不是被注定的"
        sh "那麼，你或許可以你逃避你所鑄成的一切"
        sh "這就看你的造化了"
        xv "我是作者，這還沒做，掰掰"
        return

    q "{cps=*0.5}.......?{/cps}"
    q "我實在不太明白..."
    sh "呵呵"
    sh "你以後就會知道了"
    sh "不......你一定會知道，而且很快"
    sh "現在，享受這最後片刻無知的幸福吧"
    # sh "但現在還不是時候"
    # q "選擇?選什麼?"
    # q "zen zen 挖咖奈"
    # sh "待到時機成熟，你就必須做出選擇"
    sh "......就這樣，sayonara"
    q "等、等等!"
    q "這都tm是甚麼神人寫的腳本阿"
    q "WO{cps=*0.1}CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC{/cps}"
    "眼前再度漆黑"
    stop music fadeout 3.0

    if flag==1:
        jump Jan2
    elif flag==2:
        jump Jan3

label Jan2:
    scene trans with dissolve
    pause 1.5
    scene black with dissolve
    "..."
    scene cg11 with dissolve
    play music "tata_theme.mp3" volume 0.5
    "......"
    "........."
    scene cg12
    q "呃、恩......"
    q "我睡了多久...?"
    t "平常的話，或許已經半小時了吧，然而現在我也不確定過了多久"
    q "...?"
    "半邊的天空被遮擋住，頭底下卻有種說不出的溫暖感"
    "這是..."
    scene cg13:
        zoom 1
    q "!!!!????"
    scene cg14:
        zoom 1
    q "襪襪襪襪"
    q "我、我、我怎麼會躺在你的腿上"
    scene cg15
    t "方才你突然就倒下了，情急之下我就趕忙扶住你，接著我也失去意識"
    t "醒來時，發現你就這麼躺在我腿上..."
    scene cg14
    t "~~~~~~~~"
    q "謝謝、欸不是、我是說 對不起"
    q "(雖然我也不清楚這是怎麼回事就是了)"
    t "呃...總之，這不是最重要的"
    t "重點是，我醒來的時候就發現這裡似乎有些不對勁，這裡的時間不會流動"
    q "不會流動? 莫非......!"
    q "你剛剛有沒有做了一個奇怪的夢?"
    scene cg16
    t "夢? 什麼夢?"
    t "我只記得剛剛夢裡出現了一塊和我項鍊上那顆一模一樣的寶石，剛想上手把玩一會兒時就醒了"
    q "是這樣嗎......"
    q "我方才做了一個奇怪的夢，夢中有個叫本石黛的"
    q "她說我身處於世界之外，還問我命運之類的問題"
    q "我都以為她要完成我一個願望，然後把我送去甚麼異世界當勇者之類的"
    t "這麼玄乎?話說，這怎麼感覺是說你有甚麼妄想症比較實際"
    q "嗯......總之，或許這和我們現在的狀況有關"
    t "或許吧，反正現在周圍似乎是沒有別人了"
    q "......"
    q "總之，先起身看看情況吧，也許會有甚麼線索之類的"
    t "......"
    t "行吧"
    t "唉"
    q "咋了?"
    t "沒事沒事"
    q "...!"

    scene corridor:
        zoom 0.75
    with dissolve
    q "這是......學校的走廊?"
    show roulan_tata at left with dissolve
    t "不盡然，你看前面"
    show roulan_tata:
        ease 1 xpos 900
    t "【瞧!｜見て見て】"

    q "......襪"
    q "那些是甚麼玩意!!!"
    image mon1:
        "images/mon.png"
        zoom 0.25
    image mon2:
        "images/mon.png"
        zoom 0.25
    show mon1 at left
    show mon2 at center
    "奇怪的結晶怪物" "Grrrrrrrrrrrrrrrrrr!"
    show roulan_tata:
        ease 0.1 ypos 0.75
        ease 0.1 ypos 1.0
    show roulan_tata found:
        xpos 900
        ypos 1.0
    t "啊啊啊啊啊"
    show roulan_tata -found:
        ease 0.1 xpos 1.0
    t "那是啥東西啊"
    t "快，跟我走!"
    q "!!!"
    stop music
    scene bridge:
        zoom 0.5
    with fade
    show roulan_tata
    play music tata_theme volume 0.5
    t "這裡應該暫時安全了"
    t "畢竟是五樓，怪物總不會搭電梯吧!"
    t "而且那台電梯動不動就過重"
    q "呃"
    q "話雖如此，現在這到底是甚麼回事?"
    q "不但時間被停滯了，到處還遍布著怪物!"
    q "也不知道宇恩去哪了"
    t "宇恩?"
    if eat == 0:
        q "海町宇恩，我朋友"
        q "他還跟我約好放學後有事呢"
        t "襪，還有課後約會!"
        q "我又不是甲!!!"
        t "嗯? 我怎麼記得宇恩學姊是女的?"
        q "呃...會不會是你記錯了?"
        t "...難不成他是......南梁!?"
        q "這可是相當嚴重的指控"
        q "但我喜歡"
    elif eat == 1:
        q "海町宇恩，我朋友"
        q "剛剛上完體育課就沒看到他了"
        t "沒事的，就目前看來，此間應該只有我倆"
        show roulan_tata flush
        q "......"
        q "是這樣..."
    play music tutorial_text volume 0.25
    t "..."
    t "...欸，那裏還有一個人欸!"
    show roulan_tata:
        ease 1 xpos 0.3
    show sui:
        xpos 0.5
        ypos 0.2
    with dissolve
    q "蛤? 沃，是歐日!"
    stop music
    show sui looking
    play sound vine_boom
    "歐日" "........?"
    show sui stand:
        xpos 0.5
        ypos 0.1
    with dissolve
    play music tutorial_text volume 0.25
    "歐日" "歐~~~你不是那個313的"
    "歐日" "{cps=*0.1}呃....................................{/cps}"
    q "【在下｜私は】313班的齊拉奈"
    "歐日" "沒錯!"
    q "啊老師你對現況有甚麼看法"
    "歐日" "呃、沒什麼看法"
    "歐日" "我只是個可憐的研究生兼老師而已，嚶嚶嚶"
    q "難過了"
    "歐日" "好了，沒事的話我就先去工作了"
    "歐日" "掰掰"
    show sui:
        ease 1 xpos 0.7
    pause 1.0
    show sui:
        xpos 0.7
    q "等等，那裏是!!!"
    show roulan_tata sus
    show sui:
        ease 1 ypos 1.0
    pause 1.0
    show sui:
        ypos 1.0
    play sound duang
    t "......."
    show roulan_tata found:
        ease 1 xpos 0.8
    pause 1.0
    show roulan_tata found:
        xpos 0.8
    q "......."
    "我和塔塔俯身去看，只見壯漢歐日直接肘擊地面，產生了極大的衝擊波並震碎了整個育菁樓的怪物"
    "惟見大地滿目瘡痍，而歐日孑然一身，他拂了拂袖就往蘊真樓走去了"
    t "呃...你電腦老師戰力這麼高的嗎?"
    q "當然"
    q "因為他能決定這個作品的分數，戰力難道不高嗎?"
    t "666"
    q "話說，我們要不要趁現在怪物都死光了的情況下先去個安全點的地方?"
    q "你有甚麼提議嗎?"
    t "......"
    show roulan_tata flush at center
    with dissolve
    t "那個..."
    stop music
    t "要不、去我家?"
    q "..........."
    q "我不反對"
    "於是我們邁開步伐"
    "......當然不是跳樓"
    jump Jan4


image TZyuan:
    "images/TZyuan.jpg"
    zoom 2

label Jan4:
    scene trans with dissolve
    pause 1.5

    scene TZyuan
    with dissolve
    play music tata_theme volume 0.5
    q "呃......"
    q "你說這是你家?"
    show roulan_tata with dissolve
    t "對呀"
    q "我...呃...."
    t "別咿咿呀呀的了，快點進去"
    q "是的，大小姐..."
    scene living_room:
        zoom 2.75
    with dissolve
    q "......打擾了"
    t "你先坐沙發上吧，喝不喝點茶?"
    q "甚好"
    "........"
    "........"
    "........"
    show roulan_tata:
        offscreenleft
        ease 1 xpos 0.7
    pause 1
    show roulan_tata:
        xpos 0.7
    "半晌過去，只見塔塔自廚房勻步走出，手上托著剛泡好的茶"
    show roulan_tata:
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.0
    t "喏，給你"
    q "謝謝"
    "我將手指於桌上扣了扣，然後接下了茶杯"
    "一個細品..."
    q "霍、味道香醇，我很喜歡"
    q "冒昧問一下，這甚麼茶?"
    t "沒什麼特別的啦"
    t "嗯......也就是龍井罷了，還是你想喝點別的?\n這裡還有毛尖、普珥、鐵觀音和......"
    q "噗、嗚咳咳.."
    "我拼命忍著咳嗽，生怕口中昂貴的茶水染上身旁更貴的家具"
    q "原、原來是這樣啊.."
    "放下茶杯，先冷靜一下吧"
    t "嗯? 不好喝嗎? 要不換一杯?"
    q "不不不，你的茶藝【超棒的｜素晴らしい】，只是..."
    t "只是...?"
    show roulan_tata found
    t "歐呵，難不成、你來我家是另有目的?"
    show roulan_tata flush
    t "喂，雖說我讓你進我家門，但我可沒有那種意思喔.."
    menu:
        "......"
        "{color=#f00}這倒是提醒我了(DEATH){/color}":
            q "要是...我有那種意思呢?"
            t "......"
            show sui looking:
                xalign 0.5
                ypos -1.0
            play sound vine_boom
            show sui looking:
                ease 0.5 ypos 0.0
            pause 0.5
            show sui looking:
                ypos 0.0
            play music bird volume 0.5 fadein 0.5
            "歐日" "你想做甚麼?"
            q "我、我沒有要做甚麼啊!?"
            "歐日" "作品裡不許出現違反善良風俗的東西!!!\n(雖然我也想看)"
            show sui looking:
                ypos -0.5
                zoom 2
            # with dissolve
            show red:
                alpha 0.5
            play sound vine_boom
            "歐日" "你給我洗內!!!!!!!!!!!!"
            q "呃阿啊啊啊啊啊啊"
            "{b}.:. the End (天罰 end) .:.{/b}"
            return
        "我齊家歷歷代代都是紳士!":
            pass
    q "不是不是!!!我是說，我們應該來談談我們該怎麼回到現實世界!"
    show roulan_tata
    t "哦~~~是這樣"
    t "那麼，齊學長有何高見?"
    q "不知，你有沒有發現，那些結晶怪物又開始往我們這裡聚集了?"
    t "......"
    show roulan_tata found:
        ease 0.1 ypos 0.75
        ease 0.1 ypos 1.0
    t "襪!真的!!!"
    q "我方才思索了一下，那些怪物其實與你的玉珮材質相近"
    q "再加上先前我摸到你的玉珮後暈厥才來到此境，由此可知，那枚玉珮或許是關鍵"
    show roulan_tata
    t "這麼一說好像有道理，不過"
    t "怎麼感覺你的推理過程這麼突兀阿，是偷開了甚麼腳本嗎?"
    q "喂!我又不是只會放空"
    q "況且，玉珮原本在我手上，我一醒來卻又回到你脖子上了，由此可知其之詭譎"
    t "嘻嘻嘻，其實那是我自己戴上的"
    q "......"
    q "總之，再把玉珮借我看看"
    t "行吧"
    q "那個，或許我再度接觸玉珮就會再次陷入某種異樣，那時...就拜託你了"
    t "嗯嗯"
    show roulan_tata plain with dissolve
    t "喏"
    q "哼姆哼姆"
    hide roulan_tata plain
    "......"
    show roulan_tata high with dissolve
    "再一次細看，果然尤物"
    q "..."
    t "怎麼樣，有看出甚麼嗎?"
    q "............"
    stop music
    show red:
        alpha 0.5
    "糟了，又來了"
    "耳邊一直響起一個聲音:"
    "打破他、打破他、打破他......."
    q "......打破他們印象......(語出葛仲珊《打破他》)"
    t "蛤?????"
    q "聽著，塔塔，我們可能必須打破這枚玉珮，因為..."
    show roulan_tata plain
    play music tata_theme volume 0.5
    hide red
    t "打吧"
    q "因為這......等等、這麼爽快?"
    t "我相信學長的判斷"
    t "況且，你應該不會開這種玩笑的，對吧~"
    q "恩恩、謝謝你相信我"
    t "反正你猜錯了頂多就是入贅到我家而已"
    t "......開玩笑地~哈哈"
    q "真可惜"
    q "那麼，就做嘍"
    q "哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
    scene black
    stop music
    play sound duck
    "隨著一聲玉碎，我眼前又再度一黑"
    "深沉於某種深邃的回憶之中，而那彷彿是我的記憶，而我卻不記得..."
    jump S4
label S4:
    play music tutorial_text volume 0.25
    
    "......"
    scene basyo:
        zoom 0.32
    show lioli:
        center
        zoom 0.25
    show gray:
        alpha 0.5
    "....."
    h "齊、齊大人!"
    hide gray with dissolve
    q "宇恩? 你怎麼穿上女裝啦"
    h "宇恩?"
    l "我是琉璃呀，大人，您...還好嗎?"
    stop music
    "琉璃?"
    # show red:
    #     alpha 0.5
    # "{color=#f00}不對，我是誰......?{/color}"
    "{color=#f00}我...................{/color}"
    show black
    "......"
    "............"
    sh "我早就說過你的每一個選擇都會有其意義"
    show berns:
        zoom 2.0
        xpos 0.3
        ypos 0.3
    with dissolve
    "!!!"
    q "宇恩? 為、為什麼你...為甚麼、你就是本石黛?"
    sh "嗯? 原來在你眼中，我竟是琉璃，阿不，宇恩的模樣阿"
    sh "呵，我早就說過了，我只是一個投影罷了，倒是你"
    sh "你是一個確確實實的人類，你有個無法逃避的責任"
    sh "......不過，你還擁有改變一切的能力"
    q "責任? 我..."
    sh "喔! 都忘了琉璃那傢伙把你的記憶都洗掉了，讓你變成如今這副慫樣"
    sh "這樣吧"
    sh "我暫時把你變回舊世界的自己，你會變為舊的你來思考，來行動"
    sh "你會體驗一段世間，雖然可能會感到有點身不由己"
    sh "或許藉由你的選擇，你可能會變回現在的自己吧"
    sh "至於那是福是禍......我只能說，至少舊的你失敗了"
    q "等一下!!!"
    q "我，請允許我問個問題"
    q "你所說的舊世界是甚麼意思? 難不成還有新世界?"
    sh "嗯...你所處的，這個就讀於農場高中的你是新世界的你"
    sh "而你待會會被「奪舍」的是舊世界的你"
    q "那、那麼，是甚麼導致了新舊世界之分? 而「我」的新與舊...都是我嗎?"
    sh "這恐怕得要你自己體會了，不過我可以說，兩者都可以是你，抑或不是"
    sh "至於新舊世界的分水嶺......這我覺得提示非常明顯了"
    sh "那麼，再見"
    hide berns with dissolve

    "......"
    q "奪舍嗎? ...希望不會痛啊"
    if tata > 0:
        q "也不知道塔塔怎麼樣了"
    q ".............."
    "......"
    show white
    "{b}.............!{/b}"
    "{b}我......{/b}"
    "{b}我是...{/b}"
    # "{b}我是樓蘭礦區的領主{/b}"
    # "我......"
    "{b}{color=#1c28fc}我是齊拉奈{/color}{/b}"
    "................"
    # "{b}{color=#1c28fc}......我將縱橫一切{/color}{/b}"
    hide white
    hide red 
    hide black
    with dissolve
    play music checkmate volume 0.25
    "......"
    l "齊大人?您還好嗎?"
    qq "......無妨"
    qq "琉璃，何事相告?"
    l "齊大人，前往樓蘭的班機已經就緒了!"
    qq "..."
    qq "甚好"
    "總感覺忘了甚麼"
    qq "......走吧"
    jump Demo_end

label Demo_end:
    define ddd = Character('開發者', kind=nvl, color="#00ffea")
    scene black
    ddd """
    以上就是試玩版內容了

    正式版將在學測結束後再繼續製作，屆時劇情也會再做完善

    關於舊世界的劇情也將在正式版完成(實在沒空寫了QQ)

    關於劇情因為趕工原因，很多地方有些跳tone，懇請各位賜教

    email: yunledeer@gmail.com

    =====感謝您的遊玩=====

    {clear}

    {b}開發者名單{/b}

    製作人 雨亦奇

    劇本 雨亦奇

    企劃 雨亦奇

    角色設計 雨亦奇 Koyo

    原畫 雨亦奇

    AI詠唱師 Koyo 雨亦奇

    腳本(Scripting) 雨亦奇

    音樂 BGMemon、Kirara Magic (in alphabet order)

    特別感謝 吳宇恩 邱彥宸 BGMemon Kirara Magic

    {clear}

    {b}音樂來源{/b}
    
    Anxious Heart (BGMemon)

    Checkmate (Kirara Magic)
    
    Magical Girl (Kirara Magic)

    Manda Landa (BGMemon)

    tutorial_text_0257 (BGMemon)

    """

    ".:. {b}憧憬未來 end{/b} .:."
    return

    

    

    





image black:
    "#000000"

image red:
    "#ff0000"

image white:
    "#ffffff"

image gray:
    "#4f4f4f"

# label before_main_menu:
#     show black
#     scene yuen
#     with dissolve
#     show black
#     hide yuen
#     with dissolve
#     return
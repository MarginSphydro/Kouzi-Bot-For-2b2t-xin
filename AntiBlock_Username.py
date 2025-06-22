import os
import re
import random

# 中文字符池（已扩充）
chinese_chars = "天王盖地虎宝塔镇河妖鸡鸭鱼猪马呈书顽奋疤它摊滥杨血揉油排骄惯颂睛丽官口鞋捉搜掘亲冬稻倘受延勇贡租戚驻摆执浩了份饮布营填烦毛愤纷卫尸维该蕉添肤耽递支忍答音泄扯鼓绣联巾决第恢陶振不旬醒奏就脑酒捏轮钱鉴歇畜擦灶升冠辆君薯衬吩污希犁筝葛魄愉般安京标种罪菊贩齐怜去腹真毯院催虏悄驾丢得役迷些眼乘丈丁粥贱话因蠢鹿志节附减似弄条胳掏窃二洗夫宵灾龟疫访抱嗽香信详热南局赏泊匪蜂天除坑摔关七兼峰柏创丧龙抽宴送欺建捷百甚锈软隆军淡榆白辫汉服低辉省珍刷唱剂己冶跟雀抚把再国饭土厚释基撑腥庸阿兰腐衫懒持熔捧饥已识震奖森电茫丝奸围拥滑胁漠债夏叶肩乞金咏含胖朵滴操剃煎倍搬缠冒缩炒票币凤化逢四筛侧晴透实商期爱棒站艇仔怨尖槐丘夸晌被习率徐剥花仰精楚繁胞判质射仪航毫卧干哑背跨教逆辜赵枯拜配寄爸刑团弱崖豆开遭柳派快从宫停东坝笼终晚鸟于础累帜食碧裤窑场业次踏扩灌董瑞影肉吹晒糟泳紧桃拦割翁李狂罩渣刃碌批年绩转多缘倚调免范怎叹罢陈也交九怒粘麦垒聋慈掩帽眯生稼仇跑匆粱奔渐暮俭吐统汇劈猾僵格叉乃苍拴虹迎钉喷许翼俗瓶烛托午沸庆降敌问婶令材父进兽农冈争两桂但雅箱律哲熄忧贼沈兄任途娱裙步爷始义所砌破善挥火患蜘懂点粪锯寿敞弟末纳录辱劣他续乌届水虑鱼秩垂勿遗套纠达羞扣蝶撇忆枝镇葱夜芒肠德招镜载瓜跃滚闹盯妖宿湾月吵差肚势庭佣怀喝银本角棵抛物者矮惊葬羡状美乡露吸跌控姑户腔絮瞒烫毕蓬扮初伸鄙牢邪桑深寸盛别鲁俊璃蓄众烈植过逮允氧导俱政英盾筹未拌撞粒戴来竖鸡壮唯广躬负穴老情死幕后损诸浊辈长主插斑嫩区炕埋寒锤乓疮糊鹅妄渴盖扬辨饱纤手听哀沫汪纹切恭帆扶昨绕亩更榨藏恶之你宜兆牌坐如动压阵鬼称灭自蛇艺谅熊浑廊聪橘约船要瓦笋正抬毙拼旧织杠供泡杂至是烧谈呜荡椒经辣筋亏芦湿闻缸秘昌黑愈互紫剖垮削膀架偷像退辅犬歪狡扑纺邮吴御组锄通伯态私厕籍扔庄面力举敲诞潜厘鸽廉取钟咐鼠熟泻谁店斤胀询溪郑唇米洞焰尝败携坏赌苏燃吓发晋那颗玻婚尚哗谎税奴首挣宁躁每准旺遵酿鸭搏留讲童犯事吧拆按学参枪怖翅悟窜外群涝哈谨羊菠各丑馆扫膊乙暂耍莲牛蹄蝴入借财恰绳揭蜡害等朗闲胶小专敬简虾几柿困冻堡艳妻推衰握尾颠另记职浪跳逝鹰桶券独文哥慢越台胡皇时慨科娇野泽芳悼畏萝蒙灰陷略誉锦梦民鸣慌杜梅网皂剪粮碑馋俘并咬荣液词俯印栏秒我宗辽的当迫然雕骂绢驴秧芬顷锋汗险淹么折旗驰屋顶窝暴涨肥伞既症剧立线缝汤部特滤三哨乒烂绑浅楼惑相恐浓樱洋笨永洽圾难喂眠彩亿赞够厅闪储根神元欢腿名货较闯蜓将陆针霜给娃启狠占非能幼倾绪余平坚典夺勉杏应公贺牛羊猴龙凤麒麟张李王赵钱孙周吴郑冯陈褚卫蒋沈韩杨朱秦尤许何吕施孔曹严华金魏陶姜"
english_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

def generate_mixed_name():
    # 总长度 3~7
    length = random.randint(3, 7)
    # 至少一个中文，剩下随机混合
    name_chars = [random.choice(chinese_chars)]
    pool = chinese_chars + english_chars + digits
    for _ in range(length - 1):
        name_chars.append(random.choice(pool))
    random.shuffle(name_chars)
    return ''.join(name_chars)

base_dir = os.getcwd()
generated_names = []

for i in range(1, 31):
    folder = os.path.join(base_dir, str(i))
    ini_path = os.path.join(folder, "MinecraftClient.ini")

    if not os.path.isfile(ini_path):
        print(f"[跳过] 未找到 {ini_path}")
        continue

    with open(ini_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_username = generate_mixed_name()
    generated_names.append(new_username)

    new_content = re.sub(
        r'Account\s*=\s*\{\s*Login\s*=\s*".*?",\s*Password\s*=\s*".*?"\s*\}',
        f'Account = {{ Login = "{new_username}", Password = "-" }}',
        content
    )

    with open(ini_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"[完成] {ini_path} → 用户名设置为 {new_username}")

# 保存所有生成的用户名
with open("已生成.txt", 'w', encoding='utf-8') as f:
    for name in generated_names:
        f.write(name + "\n")

print("\n✅ 所有用户名已保存到 '已生成.txt'")

# 详情页数据
def disney_info(name):
    if name == 'treasure':
        data = {
            'title': '宝藏湾',
            'image':'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/treasure.png',
            'describe': '宝藏湾位于上海迪士尼乐园东北部，共有4个游玩项目，分别为探秘海妖复仇号、加勒比海盗——沉落宝藏之站、船奇戏水滩、探险家独木舟。',
            'play': [
                {'project': '探秘海妖复仇号',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/treasure_1.png',
                 'introduce': '登上真正的海盗船，体验海盗的刺激生活与惊险行动。'},
                {'project': '加勒比海盗-沉落宝藏之战',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/treasure_2.png',
                 'introduce': '伙计们，来加入杰克船长的海盗队伍，向海洋进发，来一场寻宝之旅，沿途还会遇上怪兽呢！'},
                {'project': '船奇戏水滩',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/treasure_3.png',
                 'introduce': '在“宝藏湾”主题园区的一艘海盗船残骸中探索戏水，感受互动乐趣。'},
                {'project': '探险家独木舟',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/treasure_4.png',
                 'introduce': '登上探险家独木舟，划着船桨，开启在“宝藏湾”和“探险岛”两大主题园区的刺激探险之旅。'}
            ],
        }
    elif name == 'explore':
        data = {
            'title': '探险岛',
            'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/explore.png',
            'describe': '探险岛位于上海迪士尼乐园东南部，共有4个游玩项目，分别为翱翔·飞跃地平线、古迹探寻营、欢笑聚友会自拍点、雷鸣山漂流。',
            'play': [
                {'project': '翱翔•飞越地平线',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/explore_1.png',
                 'introduce': '来一场令人兴奋的飞行，以前所未有的方式见证这个神奇的世界吧！'},
                {'project': '古迹探索营',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/explore_2.png',
                 'introduce': '在探索探险岛的过程中，穿越绳索挑战道，踏上探索步行道，发掘部落遗迹。'},
                {'project': '欢笑聚友会自拍点',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/explore_3.png',
                 'introduce': '在地球上最大、最深、最蓝的海洋中，有一座被丛林覆盖的岛屿。您可能会在岛上的旅途中遇到一些丛林故事里的可爱迪士尼朋友，比如来自《丛林故事》、《狮子王》, 甚至可能在现场与《疯狂动物城》中的朋友见面！'},
                {'project': '雷鸣山漂流',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/explore_4.png',
                 'introduce': '踏上刺激的漂筏之旅，深入黑暗的深渊，和凶猛的巨兽赛跑， 在激流中辗转翻腾。'}
            ],
        }
    elif name == 'mickey':
        data = {
            'title': '米奇大街',
            'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/mickey.png',
            'describe': '沿着这条喧闹的大街走下去，您或许会偶遇几位全世界最受欢迎的迪士尼朋友！致敬迪士尼的经典动画人物，您永远无法提前预知自己会遇见哪一位动画角色。',
            'play': [
                {'project': '米奇妙游童话书',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/mickey_1.png',
                 'introduce': '以独特的故事和音乐曲目，将大家带入米奇和高飞的奇妙探险中。沉浸式的现场演绎，近距离欣赏耳熟能详的迪士尼歌曲，与23位挚爱的迪士尼朋友们一起欢唱。'},
                {'project': '迪士尼乐团',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/mickey_2.png',
                 'introduce': '乐团成员都是严肃的音乐家，但他们也有令人忍俊不禁的一面，非常适合在氛围友好、热闹非凡的米奇大街上为大家表演。他们用传统的仪仗队乐器，同时辅以口哨、卡祖笛和中式乐器的演奏，定会让您惊喜连连。'},
                {'project': '米奇大街自拍点',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/mickey_3.png',
                 'introduce': '进入上海迪士尼乐园这个神奇的王国，与米妮和米奇大街的所有朋友们见面！'},
            ],
        }
    elif name == 'garden':
        data = {
            'title': '奇想花园',
            'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/garden.png',
            'describe': '奇想花园位于上海迪士尼乐园北部，推荐3个游玩项目，分别为小飞象、漫威英雄总部、幻想曲旋转木马',
            'play': [
                {'project': '小飞象',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/garden_1.png',
                 'introduce': '乘着小飞象在空中尽情飞翔！他是奇想花园冉冉升起的超级明星。'},
                {'project': '漫威英雄总部',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/garden_2.png',
                 'introduce': '探索这一囊括全球诸多伟大超级英雄的广阔世界！所有这些优秀勇敢的战士在漫威电影世界中都享有尊崇地位，在漫威漫画中皆有根可循。'},
                {'project': '幻想曲旋转木马',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/garden_3.png',
                 'introduce': '乘坐飞马，伴随迪士尼《幻想曲》中恢弘大气的交响乐，回旋在梦幻的世界里。'},
            ],
        }
    elif name == 'dream':
        data = {
            'title': '梦幻世界',
            'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/dream.png',
            'describe': '梦幻世界位于上海迪士尼乐园北部，推荐3个游玩项目，分别为爱丽丝梦游仙境迷宫、晶彩奇航、奇幻童话城堡。',
            'play': [
                {'project': '爱丽丝梦游仙境迷宫',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/dream_1.png',
                 'introduce': '穿越爱丽丝梦游仙境中蜿蜒的迷宫，参加愉快的疯狂茶会派对。'},
                {'project': '晶彩奇航',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/dream_2.png',
                 'introduce': '晶彩奇航将借助音乐、灯光和神奇魔法，为游客呈现迪士尼经典故事。'},
                {'project': '奇幻童话城堡',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/dream_3.png',
                 'introduce': '奇幻童话城堡宏伟壮丽，塔尖高耸入云，欢迎各位到来。这里赋予了传奇的迪士尼故事无限生命力。'},
            ],
        }
    elif name == 'tomorrow':
        data = {
            'title': '明日世界',
            'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/tomorrow.png',
            'describe': '明日世界位于上海迪士尼乐园西北部，推荐5个游玩项目，分别为巴斯光年星际营救、创速极光轮—雪佛兰呈献、 创界：雪佛兰数字挑战、喷气背包飞行器。',
            'play': [
                {'project': '巴斯光年星际营救',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/tomorrow_1.png',
                 'introduce': '投身战斗，竭尽全力消灭索克天王手下骇人的机器人部队，拯救外星人的星球！'},
                {'project': '创速极光轮—雪佛兰呈献',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/tomorrow_2.png',
                 'introduce': '进入“创”的电子网络世界，随着极速光轮、极速转向，全力奔驰吧！'},
                {'project': '创界：雪佛兰数字挑战',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/tomorrow_3.png',
                 'introduce': '探索奇妙的未来驾驶世界，游客们在这里能体验全新一代雪佛兰概念车与创世界尖端技术的融合。'},
                {'project': '喷气背包飞行器',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/tomorrow_4.png',
                 'introduce': '准备好，背上喷气背包飞行器，在明日世界的高空中俯冲盘旋，如果您曾幻想来一场单人飞行之旅，来试试明日世界的交通方式——宇宙探险之旅将让您叹为观止。'}
            ],
        }
    elif name == 'toyStory':
        data = {
            'title': '玩具总动员',
            'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/toyStory.png',
            'describe': '迪士尼·皮克斯玩具总动员位于上海迪士尼乐园西北部，共有3个游玩项目，分别为抱抱龙冲天赛车、弹簧狗团团转、胡迪牛仔嘉年华。',
            'play': [
                {'project': '抱抱龙冲天赛车',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/toyStory_1.png',
                 'introduce': '在好朋友三角龙特蕾西的帮助下，抱抱龙将邀请大家坐上遥控冲天赛车，在长长的“U”型轨道上开启一段精彩刺激的冒险旅程'},
                {'project': '弹簧狗团团转',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/toyStory_2.png',
                 'introduce': '坐上弹簧狗的螺旋形弹簧，和他一起欢快地围着一个盛满了玩具骨头的大狗盘绕圈。'},
                {'project': '胡迪牛仔嘉年华',
                 'image': 'https://ybc-online.fbcontent.cn/ada-ide-application/resource/ybc-disney/image/toyStory_3.png',
                 'introduce': '跳上怀旧的西部马车，让小马们拉着你，踏着欢快的音乐，一同摇摆。'},
            ],
        }

    else:
        return '请输入正确的景区名称'

    return data

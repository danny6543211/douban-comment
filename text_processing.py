import random

# 全局
file_list = [
    '武林外传', '甄缳传', '红楼梦', '大明王朝1566', '仙剑奇侠传(一)',
    '仙剑奇侠传(三)', '大宋提刑官', '大明宫词', '少年包青天', '上错花桥嫁对郎', '大秦帝国之裂变',
    '琅琊榜', '山河令', '长安十二时辰', '庆余年', '宸汐缘',
    '琅琊榜之风起长林', '陈情令', '御赐小仵作', '天盛长歌', '知否知否应是绿肥红瘦'
]

keyword_list1 = [
    "演员（名字）", "选角", "颜值", "演技", "服装", "画面", "配饰", "妆容", "造型",
    "道具", "布景", "场景", "布局", "置景", "滤镜", "特效", "镜头", "服化道",
]
keyword_list2 = [
    "台词", "金句", "音乐", "歌曲", "插曲", "歌词", "文言", "诗词", "配乐", "对白", "配音", 
    "主题曲", "片尾曲", "bgm"
]
keyword_list3 = [
    "剧情", "情节", "人物", "剧本", "编剧", "故事", "人设", "逻辑", "设定", "结局", "细节", "感情线"
]
keyword_list4 = [
    "价值观"
]
keyword_list5 = [
    "历史", "诗词歌赋", "引经据典", "文化", "还原度", "民俗"
]

keyword_dict = {
    "视觉审美": keyword_list1,
    "听觉审美": keyword_list2,
    "叙事": keyword_list3,
    "价值观": keyword_list4,
    "文化传播": keyword_list5
}

# 文件中评论数量
def comment_count(file_name: str) -> int:
    f = open(file="./影评/" + file_name + ".txt", mode="r", encoding="utf-8")
    count = 0
    for line in f.readlines():
        if (line != '\n'):
            count += 1
    f.close()
    return count

# 文件中关键字数量
def comment_key_count(file_name: str, key: str) -> int:
    f = open(file="./影评/" + file_name + ".txt", mode="r", encoding="utf-8")
    count = 0
    for line in f.readlines():
        if (line.find(key) != -1):
            count += 1
    f.close()
    return count

# 把评论浓缩成全部评论
def all_file_in_one():
    res_file = open(file="./影评/全部评论.txt", mode="w", encoding="utf-8")
    for f in file_list:
        read_file = open(file="./影评/" + f +".txt", mode="r", encoding="utf-8")
        for line in read_file.readlines():
            res_file.write(line)
    res_file.close()

# 文件查找关键字返回list
def find_keyword(file_name: str, keyword: str) -> list:
    read_file = open(file="./影评/" + file_name + ".txt", mode="r", encoding="utf-8")
    res_list = []
    for line in read_file.readlines():
        if (line.find(keyword) != -1):
            res_list.append(line)
    read_file.close()
    return res_list

def all_file_processing():
    # 合并评论文件
    all_file_in_one()
    # 评论数
    res_file = open(file="评论数.txt", mode="w", encoding="utf-8")
    res_file.write("全部评论: " + str(comment_count("全部评论")) + "\n\n")
    for key, value in keyword_dict.items():
        res_file.write(key + ": " + "\n")
        for find_key in value:
            res_file.write(find_key + ": " + str(comment_key_count("全部评论", find_key)) + "\n")
        res_file.write("\n")
    res_file.close()

    # 关键字评论范例
    res_file = open(file="全部关键字评论.txt", mode="w", encoding="utf-8")
    res_file.write("全部关键字评论:" + "\n\n")
    res_file.write("\n--------------------------------------------------------------------------------------------\n")
    for key, value in keyword_dict.items():
        res_file.write(key + ": " + "\n")
        for find in value:
            comment = find_keyword("全部评论", find)
            # 打乱取前五个
            random.shuffle(comment)
            count = 0
            res_file.write(find + ":\n")
            for choice in comment:
                if count == 5:
                    break
                res_file.write(choice + "\n")
                count += 1
            res_file.write("\n")
        res_file.write("\n--------------------------------------------------------------------------------------------\n")
    res_file.close()


def one_file_processing(file_name: str):
    read_file = open(file="./影评/" + file_name + ".txt", encoding="utf-8", mode="r")
    res_file = open(file="./关键字评论/" + file_name + ".txt", encoding="utf-8", mode="w")
    res_file.write(file_name + "(" + str(comment_count(file_name)) + ")\n")
    res_file.write("--------------------------------------------------------------------------------------------\n")
    for key, value in keyword_dict.items():
        res_file.write(key + ":\n")
        for find in value:
            comment = find_keyword(file_name, find)
            random.shuffle(comment)
            count = 0
            res_file.write(find + "(" +str(len(comment))+ "):\n")
            for choice in comment:
                if count == 5:
                    break
                res_file.write(choice + "\n")
                count += 1
            res_file.write("\n")
        res_file.write("\n--------------------------------------------------------------------------------------------\n")
    read_file.close()
    res_file.close()

if __name__ == "__main__":
    # 全部影评一起处理
    all_file_processing()

    # 影评分开处理
    for f in file_list:
        one_file_processing(f)
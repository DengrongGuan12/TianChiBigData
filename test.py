__author__ = 'I322233'
# url = "http://aliyuntianchiresult.cn-hangzhou.oss.aliyun-inc.com/file/race/documents/231506/test_items.txt?Expires=1442912629&OSSAccessKeyId=2zep9f8tkzg6ennfl26ciifi&Signature=GJDcpYjj%2BXFs38cgnIeFEMCFeg4%3D"
# wp = urllib.urlopen(url)
# content = wp.read()
# f = open("test_items.txt",'w')
# f.write(content)
# f.close()
# print (content)

history = open('user_bought_history.txt')
for line in history:
    print(line)

def find_item(line,item):
    if(line.find(item,0,len(line)) == -1):
        return 0
    else:
        return 1

def find_match_count(test_item):

    dim_fashion_matchsets = open('dim_fashion_matchsets.txt')
    all_matches = ''
    for line in dim_fashion_matchsets:
        # print(matchset)
        tmp = ''
        finded = 0
        matchset = line.split(' ')[1]

        matches = matchset[:-1].split(';')

        for similar_list in matches:
            if( find_item (similar_list,str(test_item)) == 1):
                finded = 1
                continue
            tmp = tmp+similar_list+";"

        if(finded == 1):
            all_matches += tmp

    dim_fashion_matchsets.close()

    # print(all_matches.split(';'))

    count = 0;
    for match_item in all_matches:
        count = count+1
    return count

# test_items = open("test_items.txt")
# for item in test_items:
#     itemc = item[:-1]
#     count = find_match_count(itemc)
#     print(itemc + ' : '+ str(count))
# test_items.close()


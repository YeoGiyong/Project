from konlpy.corpus import kobill
from konlpy.tag import Twitter
from collections import Counter
import re
import numpy as np
import pandas as pd
import codecs


# files_ko = kobill.fileids()         # Get file ids
# doc_ko = kobill.open('c:/Java/duplicate.txt').read()

# 불용어 처리 할 파일을 c:/JAVA 디렉토리에 넣는다
f = open('c:/Java/out.txt', encoding='utf-8')
tw = f.read()

# print(tw)
eng_remove = re.sub('[a-zA-Z]', '', tw)
num_remove = re.sub('[0-9]', '', eng_remove)
sign_remove = re.sub('[~!@#:^/;\[\]‘$’%,&*\-()_+=?<>]', '', num_remove)
kor1_remove = re.sub('[ㄱ-ㅎ]', '', sign_remove)
kor2_remove = re.sub('[ㅏ-ㅣ]', '', kor1_remove)
sp_remove = re.sub('[.]', '\r\n', kor2_remove)
sp2_remove = re.sub(r'^\s\s', '', sp_remove)

# print(sp2_remove)

lists = sp2_remove.split()
# print(lists)

# lists = set(lists)
# print(lists)

lists = '\r\n'.join(lists)


nlp = Twitter()              #이게 답니다!!
nouns = nlp.nouns(lists)
# nouns = nlp.morphs(tw)

# print(nouns)

count = Counter(nouns)

# print(count.most_common(20))

# 불용어 처리 된 파일은 foo.txt UTF-8 형식으로 저장된다
with open("foo.txt", "w", encoding='utf-8') as f:
    for items in count.most_common(50):
        result = items[0] + '/' + str(items[1]) + ','
        f.write(result)
        print(result)
    f.write('/r/n')
install.packages("extrafont")
library(extrafont)        
font_import()         ## 처음 한번만 실행
loadfonts(device='win')

#windowsFonts(malgun=windowsFont("맑은 고딕")) 
windowsFonts(headline=windowsFont("HY헤드라인M")) # 해당 폰트로 사용
#windowsFonts(baedal=windowsFont("배달의민족 연성"))


library(wordcloud)
library(wordcloud2)


doc <- readLines('c:/Java/foo.txt', encoding='UTF-8')

lists <- strsplit(doc, ",")
lists

word <- c()
cnt <- c()
for (i in 1:length(lists[[1]])) {
  if (nchar(strsplit(lists[[1]][i], "/")[[1]][1]) > 1) {
    word <- append(word, strsplit(lists[[1]][i], "/")[[1]][1])
    cnt <- append(cnt, as.numeric(strsplit(lists[[1]][i], "/")[[1]][2]))
  }
}
  
wc <- data.frame(word, cnt)
wc

wordcloud2(wc, size=1.5, color='random-dark',
           minRotation = -pi/6,  maxRotation = -pi/6, 
           #rotateRatio = 1,  fontFamily ='배달의민족 도현' ) 
           rotateRatio = 1,  fontFamily ='HY헤드라인M' ) 

# palete = brewer.pal(9,"Set1")
# wordcloud(words = wc$word, freq = wc$cnt,
#           scale = c(3,.5), min.freq = 0,
#           random.order=F, random.color = T, 
#           colors=palete, family='headline')
# 
# head(demoFreq)
# wordcloud2(demoFreq, size=1.6, shape = 'star')



# wordcloud2(wc, size=1.6, color='random-dark',
       # shape = 'star', figPath = "peace.png")
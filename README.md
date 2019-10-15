# debate2vec
Word-vectors created from a large corpus of competative debate evidence.

# Download Link
Github won't let me store large files in their repos. 
* [FastText Vectors Here](https://drive.google.com/file/d/1m-CwPcaIUun4qvg69Hx2gom9dMScuQwS/view?usp=sharing) (~260mb)


# About 

Created from all publically available Cross Examination Competative debate evidence posted by the community on [Open Evidence](https://openev.debatecoaches.org/) (From 2013-2020)

Search through the original evidence by going to [debate.cards](http://debate.cards/)

Stats about this corpus: 
* 222485 unique documents larger than 200 words
* 107555 unique words (showing up more than 10 times in the corpus)
* 101 million total words

Stats about debate2vec vecotrs: 
* 300 dimensions, minimum number of appearances of a word was 10, trained for 100 epochs with lr set to 0.10 using FastText
* lowercased (will release cased)
* No subword information

The corpus includes the following topics 

* 2013-2014 Cuba/Mexico/Venezuela Economic Engagement
* 2014-2015 Oceans
* 2015-2016 Domestic Surveillance
* 2016-2017 China
* 2017-2018 Education
* 2018-2019 Immigration
* 2019-2020 Reducing Arms Sales

Other topics that this word vector model will handle extremely well

* Philosophy (Especially Left-Wing / Post-modernist)
* Law
* Government 
* Politics


Initial release is of fasttext vectors without subword information. Future releases will include fine-tuned GPT-2 and other high end models as my GPU compute allows. 

# Screenshots
![](https://github.com/Hellisotherpeople/debate2vec/blob/master/debate2vec.jpg)
![](https://github.com/Hellisotherpeople/debate2vec/blob/master/debate2vec2.jpg)
![](https://github.com/Hellisotherpeople/debate2vec/blob/master/debate2vec3.jpg)

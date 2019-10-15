#import fasttext For training 
from pyfasttext import FastText ##for inference - need the wrapper which is frustrating - only if you didn't pull original fasttext from github
import pprint
from string import punctuation


def train():
    import fasttext
    model = fasttext.train_unsupervised('debate2vec.txt', dim=300, minn=0, maxn=0, thread=11, minCount=10, loss='ns', epoch = 100, lr = 0.10, bucket = 2000000, verbose = 2)

    ##number of cards processed = 222485 in this dataset
    #number of unique  words: 107555
    #number of total words: 101 million 
    #300 dimensions, minimum number of appearances of a word was 10, trained for 100 epochs with lr set to 0.10

    model.save_model("debate2vec.bin")

#train()


def evaluate():
	model = FastText("debate2vec.bin")

	#print(model.similarity('dog', 'cat'))

	pprint.pprint(model.nearest_neighbors('praxis', k=30))

	#print(model.most_similar(positive=['arakan', 'export'], k=100)), #negative=['racism']))

evaluate()
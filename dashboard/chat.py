import nltk
import os.path
from os import path
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


import numpy
import tflearn
import tensorflow as tf
import random
import json
import pickle

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

print(os.path.isdir("dashboard/ml_sources"))
with open("dashboard/ml_sources/intents.json") as file:
	data = json.load(file)
with open("dashboard/ml_sources/data.pickle", "rb") as f:
	words, labels, training, output = pickle.load(f)

tf.compat.v1.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.load("dashboard/ml_sources/model.tflearn")

def status_desc(status):
	if status == 0:
		return "You still have to take Risk Assessment Test in order to know the type of investor you are"
	elif status == 1:
		return "You care about the preservation of Capital over Market Returns. In short, you like playing it safe. You generally like more lower-risk investments such as fixed income. You want to make your money grow but you do it slowly and surely. "
	else: return "You want to maximize returns by going with high-risk, high reward investments. You are a spicy one! Because of that, you must monitor your stocks with utmost care."


def bag_of_words(s, words):
	bag = [0 for _ in range(len(words))]

	s_words = nltk.word_tokenize(s)
	s_words = [stemmer.stem(word.lower()) for word in s_words]

	for se in s_words:
		for i, w in enumerate(words):
			if w == se:
				bag[i] = 1

	return numpy.array(bag)

def chats(inp):
	results = model.predict([bag_of_words(inp, words)])
	results_index = numpy.argmax(results)
	tag = labels[results_index]

	if results[0][results_index] > 0.70:
		for tg in data["intents"]:
			if tg["tag"] == tag:
				responses = tg["responses"]

		return str(random.choice(responses))
	else:
		return "I quite didn't get that, maybe try something other than that<br>Maybe try the suggested keywords we have like<br><br><b>What is investing?</b>: to start Investing Education<br><b>I want to take Exam</b>: to The Start the Risk Assessment Test<br><b>Describe that Company</b>: to give info about certain company"


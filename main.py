from cnnTSNE import *


img_width = 224
img_height = 224
vgg_path = '/Users/gene/Learn/keras-rtst/vgg16_weights.h5'
images_path = '/Users/gene/Code/of_v0.9.0_osx_release/addons/ofxTSNE_2/example-images/bin/data/animals'
tsne_path = '/Users/Gene/Desktop/tempco.txt'

# load model
model = VGG_16()
load_weights(model, vgg_path)

# compile
sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(optimizer=sgd, loss='categorical_crossentropy')

# get images
images = [f for f in listdir(images_path) if isfile(join(images_path, f))]
images = [images[i] for i in range(1,len(images), 100)]

# analyze images and grab activations
activations = []
for idx,image_path in enumerate(images):
	print "getting activations for %s %d/%d" % (image_path,idx,len(images))
	file_path = join(images_path,image_path)
	image = get_image_PIL(file_path, img_width, img_height)
	activations.append(model.predict(image)[0])


# t-SNE
X = np.array(activations)
tsne = TSNE(n_components=2, perplexity=30, verbose=2).fit_transform(X)


# save file
x, y = tsne[:,0], tsne[:,1]
x = (x-np.min(x)) / (np.max(x) - np.min(x))
y = (y-np.min(y)) / (np.max(y) - np.min(y))

f = open(tsne_path, 'w')
for idx,image_path in enumerate(images):
	file_path = join(images_path,image_path)
	line = "%s, %f, %f" % (file_path, x[idx], y[idx])
	f.write('%s\n'%line)
f.close()

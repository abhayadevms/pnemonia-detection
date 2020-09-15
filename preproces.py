import glob
import skimage.io as io
import skimage.transform as trans
#normal
train_path =""
train_save =""
test_path = ""
test_save =""
#not_normal
train_path =""
train_save =""
test_path = ""
test_save =""
def train(train_path,train_save):
    train_path=glob.glob(train_path + "/*.jpeg")
    resize = (240,240,3)
    count = 0
    for i in train_path:
        count = count + 1
        img = io.imread(i)
        img = trans.resize(img, resize, mode='constant')
        print("resize")
        path =(train_save+"/normal_{}.jpg".format(count))
        save = io.imsave(path, img)


def test(test_path):
    train_path=glob.glob(test_path+"/*.jpeg")
    resize = (240,240,3)
    count = 0
    for i in train_path:
        count = count + 1
        img = io.imread(i)
        img = trans.resize(img, resize, mode='constant')
        print("resize")
        path =(test_save + "/normal_{}.jpg".format(count))
        save = io.imsave(path, img)

##@############################not_normal################################
def train_not(train_path,train_save):
    train_path=glob.glob(train_path + "/*.jpeg")
    resize = (240,240,3)
    count = 0
    for i in train_path:
        count = count + 1
        img = io.imread(i)
        img = trans.resize(img, resize, mode='constant')
        print("resize")
        path =(train_save+"/pheno_{}.jpg".format(count))
        save = io.imsave(path, img)


def test_not(test_path):
    train_path=glob.glob(test_path+"/*.jpeg")
    resize = (240,240,3)
    count = 0
    for i in train_path:
        count = count + 1
        img = io.imread(i)
        img = trans.resize(img, resize, mode='constant')
        print("resize")
        path =(+test_save + "/phen_{}.jpg".format(count))
        save = io.imsave(path, img)



train(train_path,train_save)

train(test_path,test_save)

train_not(train_path,train_save)

train_not(test_path,test_save)
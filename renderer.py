import pylab as plt
from scipy import misc
import pandas as pd

lists = pd.read_csv(‘./SUBMISSION_FILE.txt')
_list = [0]*2000

for k in range(20):
    _list[k] = lists['Top_20_Image_IDs'][k].split(' ')
    im_x20 = [misc.imread(‘.PATH_TO_/final/data/images_test/%s' % i) for i in _list[k]]
    plt.figure()
    plt.figure(num=None, figsize=(12, 16), dpi=200)
    
    for j in range(20):
        plt.subplot2grid((5,4), (int(j)//4,j%4))
        plt.axis('off')
        plt.title('No.%d, %s' % (j+1, list_0txt[j]),  fontsize=14)
        plt.imshow(im_x20[j])
        
    print(lists['Descritpion_ID'][k] + '\n')
    
    with open(‘.PATH_TO_/final/data/descriptions_test/%d.txt' % k, 'r') as f:
        descriptions = f.read()
    f.closed
    
    print(descriptions)
    plt.tight_layout()
    plt.show()
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('\n')

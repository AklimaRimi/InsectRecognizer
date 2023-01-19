from fastbook import *
import os

bugs = ['Caterpillar','Leaf Footed Bug','Aphids',
        'stink bugs','grasshopper','thrips','whiteflies','mexican bean beetles',
        'fruitflies','colorado potato beetles','leaf miners','mealybugs', 'spidermites']


if not os.path.exists('C:/pythons/Deep Learning/data scrapping/bug-insects/images'):
    os.mkdir('C:/pythons/Deep Learning/data scrapping/bug-insects/images')
    
for bug in bugs:

    path = f'C:/pythons/Deep Learning/data scrapping/bug-insects/images/{bug}/'
    if not os.path.exists(path):
        os.mkdir(path)
    
    try:
        links = search_images_ddg(bug,max_images=500)

        print(f'{bug}  {len(links)}')
        download_images(path,urls=links)

    except:
        print(f'{bug} err')
        continue
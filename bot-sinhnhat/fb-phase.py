import re,json 
from facebook_scraper import *

"""
options={"comments": True}
for post in get_posts(post_urls = "https:\/\/www.facebook.com\/LienMinhHuyenThoai\/posts\/4387428904674656", options = options ):
    a = json.dumps(post)
    
codes = list(set(re.findall("LOL[A-Z0-9]{10}", a) ))
print(len(codes))
for i in codes:
    print(i, end = ' ')
"""

import pandas as pd
df_ori = pd.DataFrame(columns = ['post_id', 'text', 'post_text', 'shared_text', 'time', 'image',
       'image_lowquality', 'images', 'images_description', 'images_lowquality',
       'images_lowquality_description', 'video', 'video_duration_seconds',
       'video_height', 'video_id', 'video_quality', 'video_size_MB',
       'video_thumbnail', 'video_watches', 'video_width', 'likes', 'comments',
       'shares', 'post_url', 'link', 'user_id', 'username', 'user_url',
       'is_live', 'factcheck', 'shared_post_id', 'shared_time',
       'shared_user_id', 'shared_username', 'shared_post_url', 'available',
       'comments_full', 'reactors', 'w3_fb_url', 'reactions', 'reaction_count',
       'image_id', 'image_ids', 'fetched_time'])

options = {"comments": 0,
           "progress": True,
           "allow_extra_requests": True,
           "posts_per_page": 200}

post_urls = [#"https://www.facebook.com/LienMinhHuyenThoai/posts/4387428904674656",
             #"https://www.facebook.com/LienMinhHuyenThoai/posts/4397440670340146",
             #"https://www.facebook.com/LienMinhHuyenThoai/posts/4397845020299711",
             #"https://www.facebook.com/LienMinhHuyenThoai/posts/4397256357025244",
             #"https://www.facebook.com/LienMinhHuyenThoai/posts/4396117707139109",
             #"https://www.facebook.com/LienMinhHuyenThoai/posts/4395218007229079"
                          ]

for post in get_posts(post_urls, options = options):
    dataframe = post
    df = pd.DataFrame.from_dict(dataframe, orient='index')
    df = df.transpose()
    df_ori = df_ori.append(df)
    print("a POST ")
df_ori.to_csv(r'Scrapped_FB.csv', index = False)
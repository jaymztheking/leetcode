import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(views[views.author_id == views.viewer_id]['author_id'].sort_values().unique(), columns=['id'])

#alternative solution after reading more
'''
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.loc[views.author_id == views.viewer_id,['author_id']] \
       .drop_duplicates() \
       .sort_values(by='author_id') \
       .set_axis(['id'], axis=1) 
'''
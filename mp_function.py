from PyMovieDb import IMDB
import re
import json
imdb = IMDB()


def options(method,name='none'):
    '''dict of list return'''
    data=method(name) 
    return json.loads(data)
   

def searchbyquery(name):
    result=update_data(searchbyname,name)
    return result



def movies(name):
    return imdb.popular_movies(genre=None, start_id=1, sort_by=None)
def series(name):
    return imdb.popular_tv(genre=None, start_id=1, sort_by=None)
def searchbyname(name):
    return imdb.search(f'{name}')
def searchbyid(name):
    return imdb.get_by_id(name)  
    

def update_data(select,name='none'):
    raw_data=options(select,name)
    if(select.__name__== 'searchbyid'):
        imdb_id = raw_data.get('url', '').split('/')[-2]  # Extract IMDb ID from the URL
        name = raw_data.get('name', '')
        poster = raw_data.get('poster', '')
        poster=re.sub(r"(UX|UY).*\.jpg", "UX200.jpg", poster)
        movie_type = raw_data.get('type', '')
        return [imdb_id, name, poster, movie_type]
    else:
        data=raw_data['results']
        count=raw_data['result_count']
        result = [[d['id'], d['name'], d['poster']] for d in data]
        for item in result:
            item[2] = re.sub(r"(UX|UY).*\.jpg", "UX200.jpg", item[2])
        
    if select.__name__ == 'searchbyname':
        search_result=result
        search_list=[]
        search_list.append(count)
        search_list.append(search_result)
        return search_list
    else:
        ll = f"converted_data = {result}"
        with open(f'{select.__name__}.py', 'w') as file:
            file.write(ll)
        return 'successfully updated'


# data=update_data(searchbyname,'3 idiot')
# print(data)

 






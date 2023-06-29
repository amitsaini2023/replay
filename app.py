from flask import Flask,render_template,url_for,request
import movies,series
import mp_function as mf
import apis
import time

app = Flask(__name__)

movies_data=movies.converted_data
series_data=series.converted_data



@app.route("/play/<imdb>/<name>")
def play(imdb,name,var_data=[]):
    play=apis.myplayer(imdb)
    var_data=movies_data
    return render_template('play.html',title=name,play=play,md=var_data)

@app.route("/")
@app.route("/home")
def home(var_data=[]):
    var_data=movies_data
    return render_template('home.html',md=var_data) 

@app.route("/results",methods=['POST','GET'])
def results():
    if request.method=='POST':
        q=request.form.to_dict()
        query=q['search']
        query_result=mf.searchbyquery(query)
        query_count=query_result[0]
        query_data=query_result[1]
        show_title=f'{query_count} Result Found!!!'
    return render_template('unified.html',md=query_data,value=show_title)

@app.route("/<var>")
def unified(var,var_data=[]):
    if var=='movies':
        var_data=movies_data
    elif var=='series':
        var_data=series_data

    return render_template('unified.html',md=var_data,value=var.capitalize())




# @app.route("/season/<vari>")
# def season(vari):
#     ml=function.searchall(vari)
#     newml=function.convert_date_format(ml)
#     return render_template('season.html',myl=newml,value=vari)

# @app.route("/episode/<vari>")
# def episode(vari):
#     ml=function.searchall(vari)
#     newml=function.convert_date_format(ml)
#     return render_template('episode.html',myl=newml,value=vari)


# @app.route("/genre/<vari>")
# def genre(vari,ml=[]):
#     ml=function.searchbygenre(f'{vari}')
#     newml=function.convert_date_format(ml)
#     return render_template('unified.html',myl=newml,value=vari.capitalize())

@app.route("/search")
def search():
    return render_template('search.html')



@app.route("/contribution")
def contribution():
    return render_template('contribution.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml', mimetype='application/xml')


from flask import Flask,render_template,request,send_from_directory,flash
import converter
import os

app=Flask(__name__)

#CONFIG SECTION

app.config.from_object('config.development')
app.config['folder_video']="../"

#END CONFIG 


@app.route('/')
def index():

    os.system('rm ../web-mp3-converter/*.mp3')

    return render_template('index.html')



@app.route('/convert',methods=['POST'])

def convert_file():

    if request.method=='POST':

        urlVideo=request.form['videoUrl']

        try:

            f=converter.converter(urlVideo)

            return send_from_directory(app.config['folder_video'],f,as_attachment=True)
    
        except:

            flash('Dirección url no válida')
            return render_template('index.html')
            

#RUNNING SERVER

if __name__=='__main__':

    app.run()

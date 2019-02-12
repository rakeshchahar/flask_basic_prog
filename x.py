from flask import Flask, render_template, request,url_for,redirect

app = Flask(__name__)

@app.route('/result/')
# def result():
# 	dict ={'math': at_math,'phy':at_phy
# 	,'eng':at_eng}
# 	return render_template('result.html',result=dict)

@app.route('/input/', methods=["GET","POST"])
def inputpage():
	if request.method=="POST":
		at_name=request.form['sname']
		at_math=request.form['math']
		at_phy=request.form['phy']
		at_eng=request.form['eng']
		dict ={'Mathemetics': at_math,'Physics':at_phy,'English':at_eng}
		return render_template('result.html',result=dict,sname=at_name)
		#return redirect(url_for('result'))

	else:
		return render_template('input.html')

if __name__ == '__main__':
	app.run(debug = True)

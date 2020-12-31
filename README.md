# Introdcution
    
  This project was done by Hussein BALLOUK and Mouna BADOURI from DIA 2. 

  In this project we worked with the dataset Online Video Characteristics and Transcoding Time Dataset Data Set. 
  
  Our goal was to predict the transcoding time using 20 features. We followed the standard approach where we started by exploring the data and plotting some results to understand what we're working with and then do data cleaning / feature engineering when need. The first dataset was used to get those insights and the 2nd dataset (with 68K rows) was used for the training.

# Content

 In this github you will find the following :
  
  1. The readme File explaining important requirements
  
  2. The powerpoint presentation in pdf format
  
  3. The notebook of the training and data exploration
  
  4. The files related to our API.
  
 
 In this readme, you will find the necessary modules and their respective versions, followed a quick guide as to how we did our API and how to use it.
 
 # Modules
 
 The modules you will need are the following
 
  1. Pandas
  
  2. Numpy
  
  3. Matplotlib
  
  4. Flask
  
  5. Scikit-learn version 0.21.3 -> Do a "pip install scikit-learn==0.21.3". <br>~> This is **really important** since our training was done on that version (the version on our PC) and there has been some changes since that version, so installing the latest version will break our code.
  
  6. Seaborn
  
  7. Itertools
  
# Notebook guide
  
For the notebook, it is simple : we divded it into multiple parts so it is easier to read.
  
However, if you want to re-run the notebook, please keep the following in mind : 

  1. If you press "run all cells", the notebook will take a really long time to be done. The grid search part takes a really long time to compute.
    
  2. If you want to re-run it, we advise you to not re-run the Grid search function (unless you have to) since it is the part that takes a long time.
    
  3. The pickled model is well over the github 100 MB limit (660 MB) so we divided it into a 2 part zip that you can unzip by pressing "Extract here" on "model part1.rar"
    
  4. There's a problem with the cell with the Logistic regression model (cell number 34). It will return an error "SVD couldn't converge". You just have to re-run the cell once or twice before it works again. If it doesn't, you can re-run cells 28 to 34 again.
    
# API guide

Please, before running the API, unzip the pickle file, since it was zipped because its size is too high for github, and it is used in the API so unzip BEFORE running.

You should start by running "python app.py" in a console to get the API working.

For the API you have two choices : 

  1. Go to request.py and only modify the "request_test" variable following the correct order. Then you run, in a seperate console, "python request.py" and you will get your prediction.
    
  2. Go to "127.0.0.1:5000/" and fill out our form with the test data and press submit. It will redirect you to the result page, showing how long transcoding will take. Please make sure to only enter float / int in the form since we didn't handle the errors / an incomplete form.
    
Important note : 

We noticed that frames should be the sum of i, p and b columns and size should be the sum of i_size, b_size, p_size. So, for the site version, those features were computed automatically in python (no need to fill them out) but in the manual "request.py" version, you have to do it manually, and you have to make sure it is equal to the sum.

Here's a test data that we tried : [180,"flv",480,360,550000,30,250,5000,150,5400,2000,85000,1000,88000,"mpeg4",56000,60,3840,2160,58528].

# Conclusion 

Random Forest seems to have a very slightly higher R2 and slightly lower MSE. However, Bagging has a better grid
best score. So, since the results are close (and the methods are related after all, bagging is a special case of random
forest ), we will choose Bagging since it has a higher grid score (on unseen data thanks to oob_score = True), so it is
less likely to overfit the data.

Now, usually a score > 99% would raise some red flags since the model could have overfit the data and memorized
the answers.

Usually, we want an accuracy that is high but not very close to 100%. But we think that this is completely normal and
not due to overfitting just because of the context of our dataset :
- => Generally, when it comes to transcoding, there's not really any magic behind it. Meaning, that for the same settings we will
most likely always get the same / very close transcoding time. This differs from predicting the price of a house for example
(Boston dataset), our dataset here seems log

# CAR-PRICE-PREDICTION-MODEL.CAPSTON-PROJECT
-This data was scrapped from japanesse car prices website through a url.
-The data contains features like,name,mileage,model code,registration year,price and total price.
-The data is scrapped from the wed through inspecting it vividly and extracting the features that contains the records needed to work on  the model,for predicting car prices.

-We scrap and extract the data through using various tools like;Beautifulsoup,Requests and Headers that helps access the website illegaly.
-The data is run in the visual studio after creating an environment by various tools like;pandas,numpy which are imported after being installed n the terminal.
-Columns are created for each feature that hold records from the web.
-The whole pages whih add upto 200 pages are collected and a function is created and put through a loop to total all the data in the pages through a code.

-Then the DataFrame is craeted so that the data can be worked on as an object,,,and the it is cleaned by

1.Removing duplicated
2.Handling missing values and filling spaces
3.Droping some rows which are unuseful

-then i save the model in database which is postgresql.
-Then i created a calculator to which builds a platform for calcualtion and comparison with the local price in kenya by using the fuction and the feature names in a dictionary and return.Which then I make a comparison with the local price.

-Then i went on to building a machine learning model using the data i extracted.
-Created the features to use in prediction and price as what to predict(x-features,y-price).
-Went on and split the data by using the tool (from sklearn.model_selection import train_test_split)
and training a model(from sklearn.ensemble import RandomForestRegressor) And then did the prediction.

- Which i found Randomforest to be the best model to use to create the japan car price predictor app.
- went on and built a web application on the app.py by streamlit which actually run and i have the app.




**Task 1: Read Up on Machine Learning**

The answers can be found in the machine-learning-papers.md

**Task 2: Gatering Training Data**

New data can be captured using the gater-data.py. To gather data for an activity the corresponding button must be pressed in the DIPPID app.
-	Button 1: jumping
-	Button 2: lying
-	Button 3: waving

After the button is pressed you have one second to start the activity. After one second the data is captured for 3 seconds and stored in the data folder with an unique id. The 10 data sets per activity can be found in the data folder.

**Task 3: Activity Recognition**

The activity-visualizer.py file should be executed to run the program. It imports the activity_recognizer.py which is a class to read data from the data folder, preprocesses it and train a support vector machine with it. When executing activity-visualizer.py you should connect your DIPPID app, following that your activities will be recognized and visualized.

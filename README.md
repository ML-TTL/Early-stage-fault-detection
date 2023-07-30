# Early-stage-fault-detection
Internship at KU TTL

This is done on the assumption that the files(To_csv.ipynb and to_csv_data.ipynb) is located inside the fase 1 folder.

For windows change the / to \\\ on all path related lines.

To train the models with new data the path of the data must be adjusted appropriately.
The length of the data can be changed as required but the input length of in the input layer of the model must also be changed accordingly.

code of knn,random_forest and fully convolution model is provided.


## Installation
requires installation of python

run the following code to install the required libraries:

#### pip install -r requirements.txt

# To run the program run the following code:
(note that the mean.csv, std.csv and model_l20_e10_ns_np.h5 must be inside the same folder as main.py)
(the code must be run where main.py is present)

#### python -m uvicorn main:app --reload

go to localhost:8000/docs and click on post method and click try it out. Then the csv file can be uploaded.
The csv file must contain the data of PGV1,PGV2,PGV3,ATB1 and ATB2. An example file is testing.csv

(note: file should not be named mean.csv,std.csv or model_l20_e10_ns_np.h5)
(do not use the the name of any of the file stored in same folder as main.py)

In case a new model is to be used, the path of the new model should be included in place of model_l20_e10_ns_np.h5.
Only the name of the model can be changed if it is in the same directoty.

The input data must be processed accordingly to fit the new model.

mean.csv and std.csv can be changed to include the mean and standard deviation of the sensors mentioned above of other turbine. However the quality of result is not guaranteed.

Any extra installiation required to train the model is likely included in the code itself. Jupyter notebook is preferred to run the traning of the model. 
It can be done in google colab as well but uploading the data might require significant time.

note: the model is trained only on the data of h12 as including data from more head could not be handled by the computer used to train.
note: knn and random forest are only trained on BEP data of length 915 of PGV1 while convolution network is trained on all operating point data of length 20 of above mentioned sensors.

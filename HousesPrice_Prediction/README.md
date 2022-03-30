# HousesPrice_Prediction
HousesPrice Prediction using Tensorflow Keras
## Get the dataset
- First downlaod the dataset from **[Houses-dataset repository](https://github.com/emanhamed/Houses-dataset)** or open up a terminal and execute the following command:
  - ```
    git clone https://github.com/emanhamed/Houses-dataset
    ```
## Train the model
- Then execute the following command in terminal for train the model:
  - ```
    python cnn_regression.py --dataset "Houses-dataset\Houses Dataset"
    ```
## Use the inference
- And after the training done, You can execute the following command for Inference:
- Or you can downlaod the trained model from my google drive and put the model folder into your folder:
  - [Click to see](https://drive.google.com/drive/folders/1lK6ccTRAGs3ByWdRO00FvLh0zzmHGD90) 
  - ```
    python inference.py --input-path "[Input Patth]"
    ```

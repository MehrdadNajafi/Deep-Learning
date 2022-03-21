# Deep-Learning
## Assignment 42
<details>
  <summary>Click to expand!</summary>
  
  ### MLP- Actors Classification
  - Face classification using DeepFace library
  - Use ArcFace model for extract the feature vector and save it into a csv file
  - Create a MLP model and train it with FaceFeatures data
  - [Wandb charts](https://wandb.ai/mehrdadnajafi/actors_classification?workspace=user-mehrdadnajafi)
  - ![Screenshot (46)](https://user-images.githubusercontent.com/88179607/156261873-9d91339b-e87a-436e-a191-d619841919da.png)

  - | Algorithm | MLP Classification |
    | :---: | :---: |
    | Accuracy | 88 % |
  
</details>

## Assignment 43
<details>
  <summary>Click to expand!</summary>
  
  ### Comparison between Machine Learning ( MLP ) and Deep Learning ( CNN + MLP )
  - Comparison between Machine Learning ( MLP ) and Deep Learning ( CNN + MLP )
    - Contains 4 datasets:
      - Mnist
      - Fashion_Mnist
      - Cifar_10
      - Cifar_100

    - Wandb Charts:
      - [Mnist](https://wandb.ai/mehrdadnajafi/Mnist?workspace=user-mehrdadnajafi)
      - [Fashion_Mnist](https://wandb.ai/mehrdadnajafi/Fashion_Mnist?workspace=user-mehrdadnajafi)
      - [Cifar_10](https://wandb.ai/mehrdadnajafi/cifar_10?workspace=user-mehrdadnajafi)
      - [Cifar_100](https://wandb.ai/mehrdadnajafi/cifar_100?workspace=user-mehrdadnajafi)

    - Compare accuracy
      - |   | Accuracy | Accuracy |
        | :---: | :---: | :---: |
        | Datasets | MLP (Machine Learning) | CNN + MLP (Deep Learning) |
        | Mnist | 97% | 99% |
        | Fashion_Mnist| 88% | 89% |
        | Cifar_10 | 42% | 70% |
        | Cifar_100 | 25% | 36% |

</details>

## Assignment 44
<details>
  <summary>Click to expand!</summary>
  
  ### Animals_Classification
  - Classification between 4 animals:
    - Elephant
    - Lion
    - Koala
    - Wolf
  - Collect data using [Pinterest-Crawler](https://github.com/SajjadAemmi/Pinterest-Crawler) repository
  - Collect more than 200 photo data from each animal for Model training
  - Using Augmentation To increase Train data
  - Wandb charts:
    - [Click to see](https://wandb.ai/mehrdadnajafi/Animals_Classification?workspace=user-mehrdadnajafi)
  - Download the model and dataset from link below:
    - [model](https://drive.google.com/drive/folders/1sAf4e7PatE014Nz8ByP8Ce9pwl4ue8aV?usp=sharing)
    - [dataset](https://drive.google.com/drive/folders/1y6lMNTo6dDwXwwkaxnE40FvxYiiXPo48?usp=sharing)

  - | Train Loss: 0.5458 | Val Loss: 0.9695 | Test Loss: 0.6731 |
    | :---: | :---: | :---: |
    | Train ACC: 79% | Val ACC: 64% | Test ACC: 75% |

  ### TelegramBot_animalsClassification
  - Get a image from user and detect the animal in the image.
  - For now it can only detect 4 animals
    - Lion
    - Wolf
    - Elephant
    - Koala

</details>

## Assignment 45
<details>
  <summary>Click to expand!</summary>
  
  ### akhondDetection
  - Recognize that a sheikh is in the picture or an ordinary person
  - using [InceptionV3](https://keras.io/api/applications/inceptionv3/) for base model
  - Wandb charts:
    - [Click to see](https://wandb.ai/mehrdadnajafi/Akhond_Detector?workspace=user-mehrdadnajafi)

  - Accuracy of the model:
    - | Train Acc | Validation Acc | Test Acc |
      | :---: | :---: | :---: |
      | 99% | 100% | 100% |

  ### TelegramBot_akhondDetection
  - Recognize that a sheikh is in the picture or an ordinary person
  - Download the model from the link below:
    - [Model](https://drive.google.com/file/d/1-WmliWNkDhtba2YFdjvYxJ4i44F13jmB/view?usp=sharing)
  
</details>

## Assignment 46
<details>
  <summary>Click to expand!</summary>
  
  ### Face Mask Detection
  - Face Mask Detection using tensorflow keras, opencv, pyside6, mtcnn
  - It can detect the face and predict the mask is on the face or not
  - Using [MobileNetV2](https://keras.io/api/applications/mobilenet/#mobilenetv2-function) for model
  - Dataset:
    - [Click to see](https://www.kaggle.com/ashishjangra27/face-mask-12k-images-dataset)
  - For use the inference folder, You need to download the model folder from link below and put it in inference folder:
    - [Download Model](https://drive.google.com/drive/folders/1Upq7A9dB3zJxt0MVi8dS6XEMv9R2-9vZ?usp=sharing)
  - Wandb Charts:
    - [Click to see](https://wandb.ai/mehrdadnajafi/faceMask_detection?workspace=user-mehrdadnajafi)

  - |     | Accuracy | Loss |
    | :---: | :---: | :---: |
    | MobileNetV2 | 99.8 % | 0.006 |

  - Demo of Application:
    -  ![20220320_150419](https://user-images.githubusercontent.com/88179607/159161517-e4bc37dc-b97a-4302-ac5a-45621d866cfb.gif)

  ### 17 Flowers Classification
  - 17 Flowers Classification using Tensorflow Keras
  - [InceptionV3](https://keras.io/api/applications/inceptionv3/) is used for model
  - Dataset:
    - [Click to see](https://www.kaggle.com/datasets/saidakbarp/17-category-flowers)
  - Model:
    - [Click to see](https://drive.google.com/drive/folders/1ZoobD3eDkRtn4TLWuwNtXFmILTIAp6vY?usp=sharing)
  - Wandb Charts:
    - [Click to see](https://wandb.ai/mehrdadnajafi/17_Flowers?workspace=user-mehrdadnajafi)

  - |     | Accuracy | loss |
    | :---: | :---: | :---: |
    | InceptionV3 | 96 % | 0.1040 |
  
</details>

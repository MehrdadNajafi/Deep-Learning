# faceRecognition_tensorflowExpertMode
Face Recognition using tensorflow expert mode and classification between 14 different person
- Dataset:
  - [Click to see](https://drive.google.com/drive/folders/1WGSotRtFPYGuxPEGkWWRsBPlVXFSvl7p?usp=sharing)
- Download Model Weights:
  - [Click to see](https://drive.google.com/drive/folders/1CNt9Z9FPf3YZP8THosgtNyzwTRNjI9fg?usp=sharing)
- Wandb Charts:
  - [Click to see](https://wandb.ai/mehrdadnajafi/faceRecognition_tensorflowExpert)

|     | Accuracy | Loss (MSE) |
| :--: | :--: | :--: |
| MyModel | 80% | 0.02 |

## Inference
- For using inference folder, You should first download the model weights and put it inside the inference folder, Then open up inference folder in terminal and run following code:
  - ```
    python inference.py --inputPath [input path] --weightsPath [weights path]
    ```

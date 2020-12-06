# Identifying Fake News through NLP

## Data
Source: [Kaggle - Fake News](https://www.kaggle.com/c/fake-news/data)

A full training dataset with the following attributes:

- id: unique id for a news article
- title: the title of a news article
- author: author of the news article
- text: the text of the article; could be incomplete
- label: a label that marks the article as potentially unreliable
  - 1: unreliable
  - 0: reliable

## Hypoteses
- Percentage of punctuation characters does not improve the performances
- Percentage of capitalized letters does not improve the performances

## Results

The best score on Kaggle was 0.98, but this work can be seen as a comparison between the various features that can be used for improving the model's performances.

| Features    | Accuracy | Precision |            | Recall |      | F1   |      |
|-------------|----------|-----------|------------|--------|------|------|------|
|             |          | Reliable  | Unreliable | Rel.   | Unr. | Rel. | Unr. |
| None        | 0.88     | 0.88      | 0.88       | 0.84   | 0.91 | 0.86 | 0.89 |
| Punctuation | 0.86     | 0.89      | 0.84       | 0.77   | 0.93 | 0.83 | 0.88 |
| Uppercase   | 0.90     | 0.92      | 0.88       | 0.84   | 0.95 | 0.88 | 0.91 |
| Both        | 0.84     | 0.87      | 0.82       | 0.75   | 0.91 | 0.80 | 0.86 |

Evaluation was performed by comparing the prediction of the model with the true value of each document on the test set. Each of the four models (one for each feature) was trained on the training data for each combination of hyperparameters and the one with the best performances on the evaluation set was chosen to be tested on the test set.

## Requirements
```
tensorflow
pandas
random
pickle
spacy
numpy
csv
```

## How to run the code

To run the experiments please check that you have all the required libraries. The experiments have been done in the `ipynb` file in the `src` folder. The folder includes, in `src/results/models`, the best trained models for each combination of features. The notebook won't train again the model if it's already in that folder. To train the model from scratch, just delete the relative file in the `models` folder.

The filename is a timestamp of when the model has been trained. The file `src/results/tests.csv` contains the timestamp for each combination of features and hyperparameters: this allows to get the correct filename. During the training phase, the presence of a row containing the combination that is being tried is checked. If the `tests.csv` file already conrtains a row with those hyperparameters and features, no model will be trained since it has already been trained in the past. To force training, just remove the relative row from the `csv` file.

The folder `src/results` also contains `results_*.csv` files, where `*` is the timestamp. These files contain the true label and the prediction made during the evaluation.
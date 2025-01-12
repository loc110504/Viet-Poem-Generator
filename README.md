# Viet Poem Generator
This project generates Vietnamese poetry using a pre-trained GPT-2 model for 7-word poetry.

## Data
You can find datasets in the following Google Drive folder:
[Google Drive Folder](https://drive.google.com/drive/folders/1-Yu6tTGQSTXWZP7imaAkYfvxzZagwjsZ?usp=sharing)


## Run the project

To run this project, follow these steps:

### 1. Clone the respository

First, clone the repository to your local machine:

```bash
git clone https://github.com/loc110504/Viet-Poem-Generator.git
cd your-repository-name
```

### 2. Create virtual environment and install dependencies

```bash
conda create -n venv python=3.12 -y
conda activate venv
pip install -r requirements.txt
```


### 3. Run the app
If you want to use the Gradio web interface to generate poems, run:
```bash
python app.py
```
This will start a web server local host where you can generate poems after entering a 7-word sentence to begin the poem or use some examples I have suggested .


## Challenges

### Limited Computing Resources
- **Training Time**: Due to limited computing power, the training process was cut short, leading to insufficient learning.
- **Dataset Size**: The dataset used for training was significantly smaller than ideal, impacting the model's ability to generalize well and fully capture the intricate style of the poems.

### Learning Poetic Structure
- The model struggled to fully learn and replicate the strict 7-character per line structure, a critical aspect of Vietnamese poetry.

## Future Improvements

To improve the quality of the generated poems, the following steps are recommended:
- **Increase Computing Resources**: Utilize more powerful hardware to enable longer training times and processing larger datasets.
- **Expand Dataset**: Collect a larger dataset of 7-character verse poems to provide the model with more examples for learning.
- **Fine-tuning**: Apply further fine-tuning techniques to refine the model's ability to replicate the poetic style and structure.

## Conclusion

This project serves as a foundational step towards building an AI-powered poem generator. While the current model faces limitations due to computing resources, it demonstrates the potential of using machine learning to generate structured poetry. Future improvements will focus on overcoming these limitations to produce more accurate and stylistically correct poems.

# CodeLlama-7b: Training + Fine-Tuning

This repository contains the implementation of fine-tuning the CodeLlama-7b model using LoRA (Low-Rank Adaptation). The process focuses on adapting the model to generate Python code solutions based on input questions.

## Key Features
- Fine-tuning of CodeLlama-7b with LoRA for efficient training.
- 4-bit quantization to reduce memory usage.
- Semantic evaluation using CodeBERT cosine similarity.
- Functional evaluation using Google FLAN as a judge.

## Techniques Used
- **Training**: Pre-trained weights of CodeLlama-7b.
- **Fine-Tuning**: LoRA applied to specific layers.

## Model Details
- **Model Size**: ~283MB (with 4-bit quantization).
- **Trainable Parameters**: ~80M.

## Evaluation
- **CodeBERT Cosine Similarity**: 0.9239.
- **Google FLAN Score**: 1.0 (average).


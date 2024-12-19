# CodeLlama-34b: Training + Fine-Tuning

This repository contains the implementation of fine-tuning the CodeLlama-34b model using LoRA (Low-Rank Adaptation). The larger model capacity is leveraged for generating more complex and accurate Python code solutions.

## Key Features
- Fine-tuning of CodeLlama-34b with LoRA for efficient training.
- 4-bit quantization to handle large model size.
- Semantic evaluation using CodeBERT cosine similarity.
- Functional evaluation using Google FLAN as a judge.

## Techniques Used
- **Training**: Pre-trained weights of CodeLlama-34b.
- **Fine-Tuning**: LoRA applied to specific layers.

## Model Details
- **Model Size**: ~1.5GB (with 4-bit quantization).
- **Trainable Parameters**: ~218M.

## Evaluation
- **CodeBERT Cosine Similarity**: 0.9133.
- **Google FLAN Score**: 1.66 (average).
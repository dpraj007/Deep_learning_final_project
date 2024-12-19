# CodeLlama-7b: Unlearning + Fine-Tuning

This repository demonstrates machine unlearning and subsequent fine-tuning on the CodeLlama-7b model using LoRA (Low-Rank Adaptation). The process involves removing outdated knowledge from the model and retraining it on updated datasets.

## Key Features
- Machine unlearning using gradient ascent to remove outdated knowledge.
- Relearning (fine-tuning) on updated datasets for accurate and up-to-date code generation.
- 4-bit quantization to optimize memory usage.
- Semantic evaluation using CodeBERT cosine similarity.
- Functional evaluation using Google FLAN as a judge.

## Techniques Used
- **Unlearning**: Gradient ascent applied to maximize cross-entropy loss for deprecated samples.
- **Fine-Tuning**: LoRA applied to specific layers for efficient adaptation.

## Model Details
- **Model Size**:
  - Before Fine-Tuning: ~3.3GB (Unlearned).
  - After Fine-Tuning: ~283MB (4-bit quantization).
- **Trainable Parameters**: ~80M.

## Evaluation
- **CodeBERT Cosine Similarity**: 0.9517.
- **Google FLAN Score**: 1.0 (average).

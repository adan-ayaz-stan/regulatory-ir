# Regulatory IR : RIRAG 2025 Shared Task

The task was organized in time for COLING 2025
as part of the RegNLP 2025 workshop.

The Regulatory Information Retrieval and
Answer Generation (RIRAG) focuses on automating two core processes: retrieving relevant regulatory information and generating concise, accurate
answers to compliance-related questions. By combining information retrieval and answer generation,
RIRAG provides a framework to streamline compliance workflows and enhance organizational efficiency.

## Dataset
The shared task leverages the ObliQA dataset 1,
a regulatory compliance-focused dataset derived
from Abu Dhabi Global Market (ADGM) regulations. ObliQA comprises 27,869 questions, each
annotated with corresponding passages, making it
a robust resource for developing and benchmarking
RIRAG systems. The dataset poses unique challenges, including:
Single-Passage Questions: Questions that require retrieving and analyzing a single passage.
Multi-Passage Questions: Questions necessitating the integration of multiple passages for a complete answer.

## Evaluation
To evaluate system performance, different metrics
are applied to the two subtasks. For Subtask 1
(Information Retrieval), Recall at 10 (R@10) and
Mean Average Precision at 10 (M@10) are used
to assess the system’s ability to retrieve relevant
passages effectively.

For Subtask 2 (Answer Generation), the Regulatory Passage Answer Stability
Score (RePASs)2 measures the quality of generated
answers based on their entailment with source passages, avoidance of contradictions, and coverage
of obligations.
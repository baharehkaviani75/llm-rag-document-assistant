import json
import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from datasets import Dataset

from ragas import evaluate

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)

from app.rag.chain import ask_pdf

from app.evaluation.ragas_llm import get_ragas_llm

from app.evaluation.ragas_embeddings import get_ragas_embeddings


# -----------------------------------------
# Load evaluation questions
# -----------------------------------------

with open(
    "evaluation/questions.json",
    "r",
    encoding="utf-8"
) as f:

    questions = json.load(f)



# -----------------------------------------
# Run RAG pipeline
# -----------------------------------------

data = []


for item in questions:

    question = item["question"]

    print("\n")
    print("=" * 70)
    print("QUESTION:")
    print(question)


    try:

        result = ask_pdf(
            question
        )


    except Exception as e:

        import traceback

        print("\nERROR IN RAG:")
        traceback.print_exc()

        break


    answer = result["answer"]


    contexts = [
        doc.page_content
        for doc in result["documents"]
    ]


    print("\nANSWER:")
    print(answer)


    data.append(
        {
            "question": question,

            "answer": answer,

            "contexts": contexts,

            "ground_truth": item["ground_truth"],
        }
    )



# -----------------------------------------
# Create Dataset
# -----------------------------------------

print("\n")
print("=" * 70)
print("ALL QUESTIONS PROCESSED")
print("Number of samples:", len(data))

dataset = Dataset.from_list(
    data
)


print("\nDataset:")
print(dataset)



# -----------------------------------------
# Run RAGAS
# -----------------------------------------

result = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    ],
    llm=get_ragas_llm(),
    embeddings=get_ragas_embeddings(),
    batch_size=1
)

# -----------------------------------------
# Print Result
# -----------------------------------------

print("\n")
print("=" * 70)

print("Evaluation Result:")

print(result)



# -----------------------------------------
# Save Result
# -----------------------------------------

df = result.to_pandas()


df.to_csv(

    "evaluation/results.csv",

    index=False,

    encoding="utf-8"

)


print("\nSaved:")
print("evaluation/results.csv")
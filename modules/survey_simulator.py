from openai import OpenAI

client = OpenAI(
    api_key="YOUR_KEY"
)

def simulate_response(
        persona,
        question
):

    prompt = f"""

You are a survey respondent.

Persona:

{persona}

Answer naturally.

Question:
{question}

"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text

def generate_survey_answers(
        persona_df,
        question
):

    answers = []

    for _, row in persona_df.iterrows():

        answer = simulate_response(
            row.to_dict(),
            question
        )

        answers.append(answer)

    return answers
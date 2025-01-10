import gradio as gr
from transformers import pipeline

# Initialize the text generation pipeline
generator = pipeline('text-generation', model='loc1105/gpt2_viet_tho_7_chu')

def generate_poem(starting_line, prompt):
    # If the starting line is provided, use it; otherwise, use the prompt directly
    if starting_line and starting_line != "None":
        prompt = starting_line + ' ' + prompt

    # Generate the poem based on the combined prompt
    results = generator(
        prompt,
        max_new_tokens=100,
        do_sample=True,
        top_k=40,
        top_p=0.95,
        temperature=1.2,
        repetition_penalty=1.2,
    )
    generated_text = results[0]['generated_text']

    # Split the result into lines of poetry
    max_words_per_line = 10
    min_words_per_line = 5  # Minimum words per line
    lines = generated_text.split('\n')

    formatted_poem = ""
    for line in lines:
        words = line.split()
        if len(words) > max_words_per_line:
            words = words[:max_words_per_line]
        if len(words) >= min_words_per_line:
            formatted_poem += " ".join(words) + "\n"

    return formatted_poem

# List of example 7-word Vietnamese poetry lines (add more if needed)
example_poems = [
    "Sóng vỗ trùng khơi mang hơi thở",
    "Hoa dại giữa rừng không ai biết",
    "Mưa rơi lấm tấm theo đường gió",
    "Dòng sông chảy mãi không hề nghỉ",
    "Cánh chim lướt gió qua đồi núi"
]

iface = gr.Interface(
    fn=generate_poem,
    inputs=[
        gr.Dropdown(choices=[None] + example_poems, label="Select a starting line (optional)", value=None),  # Allow dropdown to be empty or have a valid selection
        gr.Textbox(lines=2, placeholder="Enter your prompt here... (optional)")  # The user can input their own prompt
    ],
    outputs=gr.Textbox(label="Generated Poem", lines=10),
    title="Vietnamese Poetry Generator",
    description="Generate beautiful Vietnamese poetry from a given prompt or select from the examples!",
)

iface.launch()
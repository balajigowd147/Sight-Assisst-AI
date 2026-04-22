import torch
from transformers import AutoProcessor , Qwen2_5_VLForConditionalGeneration
from Image_Loading.Image_processing import image_loading

model_name = "Qwen/Qwen2.5-VL-3B-Instruct"

model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype = torch.float16,
    device_map = "auto",
    attn_implementation = "eager",
    trust_remote_code = True
)

processor = AutoProcessor.from_pretrained(model_name , min_pixels=256*28*28,
    max_pixels=320*28*28,)

def image_description(pil_image, user_question=None):
    """Fixed version - now properly respects user question"""
    
    if user_question is None or user_question.strip() == "":
        user_question = "Is it safe to move forward? Answer briefly."

    full_prompt = f"""You are a navigation assistant for a blind person.

User question: {user_question}

Answer in 1 short sentence.
Focus only on safety and movement.
Do NOT describe everything.
Be direct like:
- "Safe to move forward"
- "Obstacle ahead, move left"
- "Stop, something is blocking the way"
"""

    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": pil_image},
            {"type": "text", "text": full_prompt}
        ]
    }]

    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    inputs = processor(
        text=[text],
        images=[pil_image],
        padding=True,
        return_tensors='pt'
    ).to(model.device)

    with torch.no_grad():
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=40,
            # temperature=0.3,
            do_sample=False,        # Changed to True
            use_cache=True
        )
    
    generated_text = processor.decode(generated_ids[0], skip_special_tokens=True)
    description = generated_text.split('assistant')[-1].strip()

    return description
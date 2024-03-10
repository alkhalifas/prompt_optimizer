# Poptimizer - Prompt Optimizer for ChatGPT

Poptimizer is a Python package designed to enhance and optimize prompts for OpenAI's ChatGPT models. It helps in refining prompts to obtain more precise and relevant responses from the AI model. This package is especially useful for developers and researchers who frequently interact with GPT models and seek to improve the quality of AI-generated content.

## Features

- **Prompt Optimization**: Refines and clarifies prompts to improve AI responses.
- **Customizable Settings**: Adjust the AI's response style with temperature settings.
- **Execute Optimized Prompts**: Option to directly execute optimized prompts and obtain AI responses.
- **Easy Integration**: Designed to be easily integrated into existing Python projects.

## Quick Start:

To install Poptimizer, simply use pip:

    pip install poptimizer

Import the package:

    from poptimizer import Poptimizer

Initialize the Poptimizer with desired temperature

    poptimizer = Poptimizer(temperature=0.7)

Optimize a prompt

    original_prompt = "Tell me a story about a company in Boston."
    optimized_prompt = poptimizer.optimize_prompt(original_prompt)

    print("Optimized Prompt:", optimized_prompt)

Optimized Prompt:

    Title: Crafting a Tale: The Rise of Tech Innovators in Boston
    
    Part 1: Introduction (50 words)
    Describe the setting of Boston as a hub for tech innovation and entrepreneurship.
    
    Part 2: Company Background (100 words)
    Introduce a fictional tech company based in Boston. Provide details on its founders, mission, and unique product/service.
    
    Part 3: Challenges Faced (75 words)
    Detail the obstacles the company encounters in the competitive tech landscape.
    
    Part 4: Innovation and Success (100 words)
    Explain how the company overcomes challenges through innovation and determination, leading to success.
    
    Part 5: Conclusion (50 words)
    Reflect on the company's journey and its impact on the Boston tech scene.

Optionally, execute the optimized prompt

    optimized_prompt, response = poptimizer.optimize_prompt(original_prompt, execute_optimized=True)
    print("Response:", response) # Produces the response



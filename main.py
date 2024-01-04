from poptimizer.poptimizer import Poptimizer

# Example usage
poptimizer = Poptimizer(temperature=0.3)
original_prompt = "Create a story about a Scientist in a Company."
optimized_prompt = poptimizer.optimize_prompt(original_prompt, execute_optimized=False)
print(optimized_prompt)

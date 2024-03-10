from poptimizer.poptimizer import Poptimizer

# Example usage
poptimizer = Poptimizer(temperature=0.3)
original_prompt = "Tell me a story about a company in Boston"
optimized_prompt = poptimizer.optimize_prompt(original_prompt, execute_optimized=False)
print(optimized_prompt)

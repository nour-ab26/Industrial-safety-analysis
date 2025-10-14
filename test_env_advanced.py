import sys
import transformers

print("--- Advanced Environment Verification ---")
print("Python Executable:", sys.executable)
print("\nAttempting to locate the 'transformers' library...")

try:
    # Get the file path of the loaded transformers module
    library_path = transformers.__file__
    print(f"\nSUCCESS: The 'transformers' library was loaded from:")
    print(f"==> {library_path}")
    print("\nThis path should be inside your 'final_env' directory.")
    print("If it is NOT, it is the source of the problem.")

    # Also print the version for confirmation
    version = transformers.__version__
    print(f"\nVersion found at this path: {version}")

except Exception as e:
    print(f"\nFAILURE: Could not even locate the library. Error: {e}")


print("\n-----------------------------------------------------")
print("Now, attempting to create TrainingArguments...")

try:
    from transformers import TrainingArguments
    args = TrainingArguments(
        output_dir="./results_test",
        evaluation_strategy="epoch",
    )
    print("\nSUCCESS: TrainingArguments created successfully.")

except TypeError as e:
    print("\nFAILURE: Encountered the exact TypeError.")
    print(f"Error message: {e}")
    print("\nCONCLUSION: The library at the path shown above is an old version,")
    print("even if the version number it reports is new. This indicates file corruption.")
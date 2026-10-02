from job_manager import create_shallow_copy, create_deep_copy


job_template = {
    "customer": {
        "name": "ABC Ltd",
        "address": {
            "city": "Lahore"
        }
    },
    "engineer": {
        "name": "Ali"
    },
    "parts": [
        "Filter",
        "Pipe"
    ]
}


# Create shallow copy
shallow_job = create_shallow_copy(job_template)

# Create deep copy
deep_job = create_deep_copy(job_template)


print("========== BEFORE CHANGES ==========")

print("Original:")
print(job_template)

print("\nShallow Copy:")
print(shallow_job)

print("\nDeep Copy:")
print(deep_job)


# Change city in shallow copy
shallow_job["customer"]["address"]["city"] = "Karachi"


print("\n========== AFTER SHALLOW COPY CHANGE ==========")

print("Original:")
print(job_template)

print("\nShallow Copy:")
print(shallow_job)

print("\nDeep Copy:")
print(deep_job)


# Change city in deep copy
deep_job["customer"]["address"]["city"] = "Islamabad"


print("\n========== AFTER DEEP COPY CHANGE ==========")

print("Original:")
print(job_template)

print("\nShallow Copy:")
print(shallow_job)

print("\nDeep Copy:")
print(deep_job)
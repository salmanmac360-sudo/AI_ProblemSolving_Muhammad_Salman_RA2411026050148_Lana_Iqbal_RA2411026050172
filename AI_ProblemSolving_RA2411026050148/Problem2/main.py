def evaluate_condition(condition, facts):
    tokens = condition.split()
    result = None
    operator = None

    for token in tokens:
        if token == "AND":
            operator = "AND"
        elif token == "OR":
            operator = "OR"
        elif token == "NOT":
            operator = "NOT"
        else:
            value = facts.get(token, False)

            if operator == "NOT":
                value = not value
                operator = None

            if result is None:
                result = value
            else:
                if operator == "AND":
                    result = result and value
                elif operator == "OR":
                    result = result or value

    return result


def main():
    print("=== Insurance Claim Decision System ===")

    facts = {}
    n = int(input("Enter number of facts: "))

    for _ in range(n):
        key = input("Enter fact name: ").strip()
        value = input("Enter value (True/False): ").strip().lower()
        facts[key] = True if value == "true" else False

    rules = []
    r = int(input("\nEnter number of rules: "))

    for _ in range(r):
        rule = input("Enter rule (IF condition THEN action): ")
        rules.append(rule)

    decision = "Reject Claim"

    print("\n--- Rule Evaluation ---")

    for rule in rules:
        parts = rule.split("THEN")
        condition_part = parts[0].replace("IF", "").strip()
        action = parts[1].strip().lower()

        result = evaluate_condition(condition_part, facts)

        print(f"{condition_part} → {result}")

        if result:
            if "approve" in action:
                decision = "Claim Approved"
            elif "reject" in action:
                decision = "Claim Rejected"

    print("\n--- Final Output ---")
    print("Facts:", facts)
    print("Rules:", rules)
    print("Decision:", decision)


if __name__ == "__main__":
    main()
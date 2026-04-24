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

    for i in range(n):
        key = input("Fact name: ")
        value = input("Value (True/False): ").lower()
        facts[key] = True if value == "true" else False

    rules = []
    r = int(input("Enter number of rules: "))

    for i in range(r):
        rule = input("Rule (IF ... THEN ...): ")
        rules.append(rule)

    decision = "Claim Rejected"

    print("\n--- Evaluation ---")

    for rule in rules:
        parts = rule.split("THEN")
        condition = parts[0].replace("IF", "").strip()
        action = parts[1].strip().lower()

        result = evaluate_condition(condition, facts)

        print(condition, "→", result)

        if result:
            if "approve" in action:
                decision = "Claim Approved"
            elif "reject" in action:
                decision = "Claim Rejected"

    print("\nDecision:", decision)


if __name__ == "__main__":
    main()
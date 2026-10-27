def check_result(marks, attendance, disciplinary_issue):
   
    if marks < 70:
        return "FAIL", "Marks are below 70."


    if attendance < 75:
        return "FAIL", "Attendance is below 75%."

    if disciplinary_issue:
        return "FAIL", "Student has a disciplinary issue."

    return "PASS", "All conditions satisfied."




test_cases = [
    {
        "name": "Case 1",
        "marks": 85,
        "attendance": 90,
        "disciplinary_issue": False
    },
    {
        "name": "Case 2",
        "marks": 65,
        "attendance": 90,
        "disciplinary_issue": False
    },
    {
        "name": "Case 3",
        "marks": 85,
        "attendance": 70,
        "disciplinary_issue": False
    },
    {
        "name": "Case 4",
        "marks": 85,
        "attendance": 90,
        "disciplinary_issue": True
    }
]

for case in test_cases:
    result, reason = check_result(
        case["marks"],
        case["attendance"],
        case["disciplinary_issue"]
    )

    print(case["name"])
    print("Input:", case)
    print("Expected Result:", 
          "PASS" if case["name"] == "Case 1" else "FAIL")
    print("Actual Result:", result)
    print("Reason:", reason)
    print("-" * 50)
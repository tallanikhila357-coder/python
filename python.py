def scholarship_allocation():
    applicants = [
        ("Anu", 88, 70, 90, 250000),
        ("Bala", 78, 62, 80, 280000),
        ("Charan", 91, 55, 95, 200000),
        ("Divya", 85, 68, 72, 180000)
    ]

    eligible = []

    for name, aggregate, subject_min, attendance, income in applicants:
        if (aggregate >= 75 and subject_min >= 60
                and attendance >= 75 and income <= 300000):
            eligible.append((name, aggregate, attendance))

    eligible.sort(key=lambda student: (student[1], student[2]), reverse=True)

    print("\nEligible Scholarship Applicants")
    if eligible:
        for rank, student in enumerate(eligible, start=1):
            print(rank, student[0], "- Aggregate:", student[1],
                  "Attendance:", str(student[2]) + "%")
    else:
        print("No eligible applicants")


def electricity_billing():
    units = int(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units")
    else:
        if units <= 100:
            energy = units * 1.50
        elif units <= 200:
            energy = 100 * 1.50 + (units - 100) * 2.50
        else:
            energy = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00

        bill = energy + 50
        adjustment = 0

        if bill > 500:
            adjustment = bill * 0.05
            bill += adjustment
            print("Surcharge:", round(adjustment, 2))
        elif units <= 100:
            adjustment = energy * 0.10
            bill -= adjustment
            print("Rebate:", round(adjustment, 2))

        print("Energy charge: Rs.", round(energy, 2))
        print("Final bill: Rs.", round(bill, 2))


def hospital_billing():
    age = int(input("Enter patient age: "))

    if age < 0:
        print("Invalid age")
    else:
        consultation = 500
        diagnostics = 800
        treatment = 1500
        total = consultation + diagnostics + treatment

        concession = total * 0.10 if age >= 60 else 0
        final_bill = total - concession
        category = "High Cost" if final_bill >= 2500 else "Standard"

        print("Total charges: Rs.", total)
        print("Concession: Rs.", round(concession, 2))
        print("Final bill: Rs.", round(final_bill, 2))
        print("Patient billing category:", category)


def employee_payroll():
    basic = float(input("Enter basic pay: Rs. "))
    overtime_hours = float(input("Enter overtime hours: "))
    incentive = float(input("Enter incentive: Rs. "))

    if basic < 0 or overtime_hours < 0 or incentive < 0:
        print("Invalid input")
    else:
        hra = basic * 0.20
        da = basic * 0.10
        overtime_pay = overtime_hours * 150
        gross = basic + hra + da + overtime_pay + incentive
        pf = basic * 0.12
        tax = min(gross, 30000) * 0.05 + max(gross - 30000, 0) * 0.10
        net = gross - pf - tax

        print("\n--- Salary Statement ---")
        print("HRA: Rs.", round(hra, 2))
        print("DA: Rs.", round(da, 2))
        print("Overtime pay: Rs.", round(overtime_pay, 2))
        print("Gross salary: Rs.", round(gross, 2))
        print("PF deduction: Rs.", round(pf, 2))
        print("Tax deduction: Rs.", round(tax, 2))
        print("Net salary: Rs.", round(net, 2))


def telecom_plan_optimization():
    plans = [
        ("Plan A", 299, 10, 20, 28),
        ("Plan B", 399, 20, 0, 56),
        ("Plan C", 249, 5, 20, 28)
    ]

    usage = float(input("Enter expected data usage (GB): "))
    required_days = int(input("Enter required validity (days): "))
    budget = float(input("Enter budget: Rs. "))

    eligible = []

    for name, base, included, extra_rate, validity in plans:
        extra_gb = max(usage - included, 0)
        total_cost = base + extra_gb * extra_rate
        if validity >= required_days and total_cost <= budget:
            eligible.append((name, total_cost, validity))

    for plan in eligible:
        print(plan[0], "- Total cost: Rs.", round(plan[1], 2),
              "- Validity:", plan[2], "days")

    if eligible:
        best = min(eligible, key=lambda item: item[1])
        print("Most economical plan:", best[0],
              "at Rs.", round(best[1], 2))
    else:
        print("No plan satisfies the requirements")


def railway_fare_calculator():
    distance = float(input("Enter distance in km: "))
    age = int(input("Enter passenger age: "))
    travel_class = input("Enter class (Sleeper/AC): ").strip().lower()

    if distance <= 0 or age < 0 or travel_class not in ("sleeper", "ac"):
        print("Invalid input")
    else:
        if distance <= 100:
            base_fare = distance * 1.20
        else:
            base_fare = 100 * 1.20 + (distance - 100) * 1.00

        multiplier = 1.0 if travel_class == "sleeper" else 1.8
        distance_fare = base_fare * multiplier
        concession = distance_fare * 0.20 if age >= 60 else 0
        final_fare = distance_fare - concession + 40

        print("Distance fare: Rs.", round(distance_fare, 2))
        print("Concession: Rs.", round(concession, 2))
        print("Reservation fee: Rs. 40")
        print("Final fare: Rs.", round(final_fare, 2))


def retail_billing():
    items = [
        ("Notebook", 10, 100, 0.05),
        ("Bag", 5, 300, 0.12)
    ]

    subtotal = sum(qty * price for name, qty, price, rate in items)
    discount = min(subtotal * 0.10, 500) if subtotal >= 2000 else 0
    total_tax = 0

    print("--- Itemized Invoice ---")
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))

    for name, qty, price, rate in items:
        item_subtotal = qty * price
        share = item_subtotal / subtotal if subtotal else 0
        discounted = item_subtotal - discount * share
        tax = discounted * rate
        total_tax += tax
        print(name, "| Qty:", qty, "| Discounted value: Rs.",
              round(discounted, 2), "| Tax: Rs.", round(tax, 2))

    print("Total tax: Rs.", round(total_tax, 2))
    print("Amount payable: Rs.", round(subtotal - discount + total_tax, 2))


def manufacturing_profit_analysis():
    quantity = int(input("Enter units produced: "))
    material_unit = float(input("Material cost per unit: Rs. "))
    labour = float(input("Total labour cost: Rs. "))
    machine = float(input("Machine cost: Rs. "))
    wastage_percent = float(input("Wastage percentage: "))
    selling_unit = float(input("Selling price per unit: Rs. "))

    values = [quantity, material_unit, labour, machine,
              wastage_percent, selling_unit]

    if any(value < 0 for value in values):
        print("Invalid input")
    else:
        material_cost = quantity * material_unit
        wastage_cost = material_cost * wastage_percent / 100
        total_cost = material_cost + wastage_cost + labour + machine
        revenue = quantity * selling_unit
        profit = revenue - total_cost
        target = total_cost * 0.20

        print("Material cost: Rs.", round(material_cost, 2))
        print("Wastage cost: Rs.", round(wastage_cost, 2))
        print("Total production cost: Rs.", round(total_cost, 2))
        print("Sales revenue: Rs.", round(revenue, 2))
        print("Profit: Rs.", round(profit, 2))
        print("Target profit: Rs.", round(target, 2))
        print("Target achieved" if profit >= target else "Target not achieved")


def travel_budget_analysis():
    expenses = [
        ("Hotel", 200),
        ("Food", 80),
        ("Local transport", 50)
    ]

    exchange_rate = 83
    fee_rate = 0.02
    budget = 30000
    total = 0
    converted_expenses = []

    for category, usd in expenses:
        converted = usd * exchange_rate
        fee = converted * fee_rate
        amount_with_fee = converted + fee
        total += amount_with_fee
        converted_expenses.append((category, converted, fee))
        print(category, "- Converted: Rs.", round(converted, 2),
              "| Fee: Rs.", round(fee, 2))

    largest = max(converted_expenses, key=lambda item: item[1])
    print("Total including fees: Rs.", round(total, 2))
    print("Largest expense category:", largest[0])

    if total <= budget:
        print("Budget status: Within budget")
    else:
        print("Budget status: Over budget by Rs.", round(total - budget, 2))


def campus_event_financial_planning():
    import math

    participants = int(input("Enter expected participants: "))

    if participants < 0:
        print("Invalid participant count")
    else:
        venue = 12000
        equipment = 5000
        transport = 3000
        catering_per_person = 150
        certificate_per_person = 20
        registration_fee = 500
        sponsorship = 10000

        fixed_cost = venue + equipment + transport
        variable_per_person = catering_per_person + certificate_per_person
        total_cost = fixed_cost + participants * variable_per_person
        income = sponsorship + participants * registration_fee
        balance = income - total_cost
        contribution = registration_fee - variable_per_person
        break_even = math.ceil((fixed_cost - sponsorship) / contribution)

        print("Fixed cost: Rs.", fixed_cost)
        print("Total event cost: Rs.", total_cost)
        print("Total income: Rs.", income)
        print("Financial balance: Rs.", balance)
        print("Break-even registrations:", break_even)

        if balance >= 0:
            print("Event status: Surplus")
        else:
            print("Event status: Shortfall")


def main():
    programs = {
        "1": ("University Scholarship Allocation", scholarship_allocation),
        "2": ("Progressive Electricity Billing", electricity_billing),
        "3": ("Hospital Billing and Patient Classification", hospital_billing),
        "4": ("Employee Payroll and Deduction Analysis", employee_payroll),
        "5": ("Telecommunications Plan Optimization", telecom_plan_optimization),
        "6": ("Railway Fare and Reservation Calculator", railway_fare_calculator),
        "7": ("Retail Billing with Multiple Discount Rules", retail_billing),
        "8": ("Manufacturing Cost and Profitability Analysis", manufacturing_profit_analysis),
        "9": ("Multi-Currency Travel Budget Analysis", travel_budget_analysis),
        "10": ("Campus Event Financial Planning", campus_event_financial_planning)
    }

    while True:
        print("\n========== PYTHON ACTIVITY PROGRAMS ==========")
        for number, (name, function) in programs.items():
            print(number + ".", name)
        print("0. Exit")

        choice = input("Enter your choice (0-10): ")

        if choice == "0":
            print("Program ended.")
            break
        elif choice in programs:
            print("\n---", programs[choice][0], "---")
            programs[choice][1]()
        else:
            print("Invalid choice. Please select from 0 to 10.")


if __name__ == "__main__":
    main()

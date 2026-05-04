# Module 8 Assignment: Data Lookup with Dictionaries
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create dictionary of service categories and hourly rates
services = {"Web Development": 150, "Data Analysis": 175, "Business Management": 200, "Cybersecurity Analyst": 225, "AI Developer": 250}

# TODO 2: Customer dictionaries
customer1 = {"company_name": "TechNova Inc", "contact_person": "Kevin Johnson", "email": "kevin@gmail.com", "phone": "472-539"}
customer2 = {"company_name": "ABC Corp", "contact_person": "John Smith", "email": "john@gmail.com", "phone": "573-498"}
customer3 = {"company_name": "DataTech", "contact_person": "Timmy Tucker", "email": "timmy@gmail.com", "phone": "631-259"}
customer4 = {"company_name": "Zcomps" , "contact_person": "Zack Evans", "email": "zack@gmail.com", "phone": "322-643"}

# TODO 3: Create master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4,
    }

# TODO 4: Display all customer information
print("\nAll Customers:")
print("-" * 60)

print(customers)

# TODO 5: Look up specific customers
print("\n\nCustomer Lookups:")
print("-" * 60)

c002_info = customers["C002"]
print(f"C002 Info: {c002_info}")

c003_contact = customers["C003"]["contact_person"]
print(f"\nC003 Contact Person: {c003_contact}")

c999_info = customers.get("C999", "Customer doesn't exsist")
print(f"\nCustomer C999: {c999_info}")

# TODO 6: Update customer information
print("\n\nUpdating Customer Information:")
print("-" * 60)

customers["C001"]["phone"] = "590-534"
customers["C002"]["industry"] = "lumber"

print(customers["C001"])
print(customers["C002"])

# TODO 7: Create project dictionaries
print("\n\nProject Information:")
print("-" * 60)

projects = {
    "C001": [
        {"name": "Website Upgrade", "service": "Web Development", "hours": 40, "budget": 6000, "status": "active"},
        {"name": "Data Migration", "service": "AI Developer", "hours": 25, "budget": 7000, "status": "completed"}
        ],
    "C002": [{"name": "Market Dashboard", "service": "Business Management", "hours": 50, "budget": 9000, "status": "pending"}],
    
    "C003": [{"name": "Code Analysis", "service": "Cybersecurity Analyst", "hours": 15, "budget": 4000, "status": "active"}],
       
    "C004": [{"name": "Data Organization", "service": "Data Analysis", "hours": 30, "budget": 5000, "status": "completed"}]
    }

# TODO 8: Project costs
for plist in projects.values():
    for p in plist:
        rate = services[p["service"]]
        p["cost"] = rate * p["hours"]
        print(p["name"], p["cost"])
        
# TODO 9: Customer statistics
print("\n\nCustomer Statistics:")
print("-" * 60)

print(f"Customer IDS: {list(customers.keys())}")


print(f"\nAll Companies: {[c['company_name'] for c in customers.values()]}")
print(f"\nTotal Customers: {len(customers)}")

# TODO 10:
print("\n\nService Usage Analysis:")
print("-" * 60)

service_counts = {}
for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service, 0) + 1
print(service_counts)

# TODO 11: Financial aggregations
print("\n\nFinancial Summary:")
print("-" * 60)

project_hours = [p["hours"] for plist in projects.values() for p in plist]
project_budgets = [p["budget"] for plist in projects.values() for p in plist]

total_hours = sum(project_hours)
total_budget = sum(project_budgets)
avg_budget = total_budget / len(project_budgets)
max_budget = max(project_budgets)
min_budget = min(project_budgets)

print(f"Total hours across projects: {total_hours}")
print(f"\nTotal budget across projects: {total_budget}")
print(f"\nAverage project budget: {avg_budget}")
print(f"\nMost expensive project: {max_budget}")
print(f"\nLeast expensive project: {min_budget}")

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)

for cid, plist in projects.items():
    details = customers[cid]
    number_of_projects = len(plist)
    customer_total_budget = sum(p["budget"] for p in plist)
    customer_total_hours = sum(p["hours"] for p in plist)
    
    print(f"{cid} Customer details: {details}")
    print(f"{cid} Number of projects: {number_of_projects}")
    print(f"{cid} Total budget: ${customer_total_budget}")
    print(f"{cid} Total hours: {customer_total_hours}")

# TODO 13: Rate adjustments using dictionary comprehension
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)

adjusted_rates = {k: v * 1.1 for k, v in services.items()}
print(adjusted_rates)

# TODO 14: Filter customers
print("\n\nActive Customers (with projects):")
print("-" * 60)

active_customers = {cid: customers[cid] for cid in projects if cid in customers}
print(active_customers)

# TODO 15: Project summaries
print("\n\nCustomer Budget Totals:")
print("-" * 60)

customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}
print(customer_budgets)

# TODO 16: Service pricing tiers
print("\n\nService Pricing Tiers:")
print("-" * 60)

service_tiers = {
    service: ("Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic")
    for service, rate in services.items()
    }
print(service_tiers)

# TODO 17: Customer validation function
print("\n\nCustomer Validation:")
print("-" * 60)

def validate_customer(customers):
    required = {"company_name", "contact_person", "email", "phone"}
    return required.issubset(customers.keys())

for cid, cdata in customers.items():
    print(cid, validate_customer(cdata))

# TODO 18: Project status tracking
print("\n\nProject Status Summary:")
print("-" * 60)

status_counts = {}
statuses = ["active", "completed", "pending"]

for plist in projects.values():
    for p in plist:
        status = p.get("status")
        status_counts[status] = status_counts.get(status, 0) + 1

print(status_counts)

# TODO 19: Budget analysis function with aggregation
print("\n\nDetailed Budget Analysis:")
print("-" * 60)

def analyze_customer_budgets(projects):
    budget_analysis = {}
    
    for cid, plist in projects.items():
        total = 0
        count = 0
        
        for p in plist:
            total += p["budget"]
            count += 1
            
        average = total / count
        
        budget_analysis[cid] = {
            "total": total,
            "average": average,
            "count": count
            }
    return budget_analysis

budget_analysis = analyze_customer_budgets(projects)

print(budget_analysis)

# TOD0 20: Service recommendation system
print("\n\nService Recommendations:")
print("-" * 60)


    
    
    
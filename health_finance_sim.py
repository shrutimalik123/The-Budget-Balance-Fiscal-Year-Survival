import random

def health_finance_game():
    # 1. Financial Setup
    budget = 1000000  # $1 Million for the quarter
    revenue = 0
    patient_satisfaction = 75
    equipment_health = 80
    
    print("--- 💰 THE BUDGET BALANCE: CFO SIMULATOR 💰 ---")
    print(f"Starting Quarterly Budget: ${budget:,}")
    print("Goal: End the quarter with a positive Margin and high Patient Satisfaction.")

    # 2. Quarterly Rounds (3 Months)
    for month in ["October", "November", "December"]:
        print(f"\n--- 📅 MONTH: {month} ---")
        print(f"Current Funds: ${budget:,} | Equipment Status: {equipment_health}%")
        
        # Monthly Variance Event
        variance_type = random.choice(["Labor", "Supply", "Volume"])
        if variance_type == "Labor":
            cost = 50000
            print(f"⚠️ VARIANCE: Nursing overtime surged. Cost: ${cost:,}")
        elif variance_type == "Supply":
            cost = 30000
            print(f"⚠️ VARIANCE: Price of surgical gloves increased. Cost: ${cost:,}")
        else:
            gain = 40000
            print(f"📈 VARIANCE: Patient volume was higher than projected! Revenue: +${gain:,}")
            budget += gain
            cost = 0
        
        budget -= cost

        # 3. Decision Phase
        print("\nEXECUTIVE DECISION:")
        print("1) Invest in Staff Training (Boosts Satisfaction, Cost: $100k)")
        print("2) Repair Aging Equipment (Boosts Equipment Health, Cost: $150k)")
        print("3) Save Reserves (No cost, but Equipment/Satisfaction may drift)")
        
        choice = input("Select Action (1-3): ")

        if choice == "1":
            budget -= 100000
            patient_satisfaction += 10
            print("✨ Staff training complete. Patient satisfaction up!")
        elif choice == "2":
            budget -= 150000
            equipment_health = min(100, equipment_health + 20)
            print("🔧 MRI and Lab equipment serviced. Downtime reduced.")
        else:
            # Natural drift if no investment is made
            patient_satisfaction -= 5
            equipment_health -= 5
            print("📉 Minimal maintenance performed. Resources are aging.")

    # 4. Final Financial Audit
    print(f"\n--- 📑 QUARTERLY FISCAL REPORT ---")
    print(f"Remaining Budget: ${budget:,}")
    print(f"Final Patient Satisfaction: {patient_satisfaction}%")
    print(f"Final Equipment Health: {equipment_health}%")
    
    if budget > 500000 and patient_satisfaction > 70:
        print("🏆 FISCAL ELITE: You achieved a high margin without sacrificing quality!")
    elif budget > 0:
        print("📋 STABLE: You kept the hospital in the black, but growth is slow.")
    else:
        print("❌ INSOLVENT: The hospital has a negative margin. Board of Directors is concerned.")

health_finance_game()

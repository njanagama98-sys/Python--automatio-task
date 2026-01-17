import datetime

# SINSIST - Professional Dashboard Prototype
def sinsist_dashboard():
    header = "--- SINSIST: GRAM NIDHI TRACKER ---"
    village = "గ్రామం: మంచిర్యాల (Sample)"
    funds = "మొత్తం నిధులు: ₹1,00,00,000"
    spent = "ఖర్చు చేసినవి: ₹45,00,000"
    balance = "మిగిలినవి: ₹55,00,000"
    
    print("=" * len(header))
    print(header)
    print("=" * len(header))
    print(f"తేదీ: {datetime.date.today()}")
    print(village)
    print("-" * 20)
    print(funds)
    print(spent)
    print(balance)
    print("-" * 20)
    print("స్టేటస్: 80% పనులు పారదర్శకంగా జరుగుతున్నాయి.")
    print("=" * len(header))

sinsist_dashboard()
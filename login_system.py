import time

def sinsist_login():
    print("=" * 30)
    print("   SINSIST DIGITAL LOGIN   ")
    print("=" * 30)
    
    phone = input("మీ 10 అంకెల ఫోన్ నంబర్ నమోదు చేయండి: ")
    
    if len(phone) == 10 and phone.isdigit():
        print(f"\n{phone} కు OTP పంపుతున్నాము...")
        time.sleep(1.5)
        
        otp = input("మీకు వచ్చిన 4 అంకెల OTP ని ఎంటర్ చేయండి: ")
        
        # డెమో కోసం 1234 ని OTP గా వాడుతున్నాం
        if otp == "1234":
            print("\n✅ లాగిన్ విజయవంతమైంది!")
            print("SINSIST డ్యాష్‌బోర్డ్‌కు స్వాగతం.")
            return True
        else:
            print("\n❌ తప్పుడు OTP. మళ్ళీ ప్రయత్నించండి.")
            return False
    else:
        print("\n❌ తప్పుడు ఫోన్ నంబర్. 10 అంకెలు ఉండాలి.")
        return False

if __name__ == "__main__":
    sinsist_login()
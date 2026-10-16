#!/usr/bin/env python3
# SHADOW BOOSTER — safe battery monitor for Android via Termux:API
import json, shutil, subprocess, sys
from datetime import datetime

RED='\033[91m'; CYAN='\033[96m'; YELLOW='\033[93m'; GREEN='\033[92m'; RESET='\033[0m'

def battery():
    if not shutil.which('termux-battery-status'):
        print(RED+'لم أجد termux-battery-status.'+RESET)
        print('ثبّت Termux:API وإضافة Termux:API، ثم نفّذ: pkg install termux-api')
        return None
    try:
        p=subprocess.run(['termux-battery-status'],capture_output=True,text=True,timeout=8)
        if p.returncode: print(RED+(p.stderr.strip() or 'تعذرت قراءة البطارية')+RESET); return None
        return json.loads(p.stdout)
    except Exception as e:
        print(RED+f'خطأ في قراءة البطارية: {e}'+RESET); return None

def main():
    print(CYAN+'🌑 SHADOW BOOSTER | مراقب البطارية'+RESET)
    print('لا يحتاج روت. لا يغيّر إعدادات النظام ولا يحذف ملفاتك.\n')
    while True:
        d=battery()
        if d:
            print('\n'+'─'*34)
            print('الوقت:',datetime.now().strftime('%H:%M:%S'))
            for key,label in [('percentage','نسبة الشحن'),('status','حالة البطارية'),('plugged','مصدر الطاقة'),('health','صحة البطارية')]:
                if key in d: print(f'{label}: {d[key]}'+('%' if key=='percentage' else ''))
            t=d.get('temperature')
            if t is not None:
                print('درجة الحرارة:',t,'°C')
                try:
                    if float(t)>=45: print(RED+'تحذير: أوقف اللعب واترك الهاتف يبرد. افصل الشاحن إذا استمرت الحرارة.'+RESET)
                    elif float(t)>=40: print(YELLOW+'الحرارة مرتفعة نسبيًا؛ خفف الاستخدام أثناء الشحن.'+RESET)
                    else: print(GREEN+'الحرارة تبدو معتدلة.'+RESET)
                except (ValueError,TypeError): pass
            print('\nنصائح سريعة:')
            pct=d.get('percentage')
            if isinstance(pct,(int,float)) and pct<=20: print('• فعّل وضع توفير الطاقة من إعدادات الهاتف.')
            print('• خفّض سطوع الشاشة وأوقف GPS ونقطة الاتصال عند عدم الحاجة.')
            print('• افتح الإعدادات > البطارية لمعرفة التطبيقات الأعلى استهلاكًا.')
            print('• تجنّب الألعاب الثقيلة أثناء الشحن لتقليل الحرارة.')
            print('• استخدم شاحنًا وكابلًا موثوقين ومتوافقين مع هاتفك.')
            print('• لا تضع الهاتف في الثلاجة أو قرب الماء لتبريده.')
        print('\nاضغط Enter للتحديث أو اكتب q للخروج.')
        try: ans=input('> ').strip().lower()
        except (EOFError,KeyboardInterrupt): print('\nإلى اللقاء!'); break
        if ans=='q': break

if __name__=='__main__': main()

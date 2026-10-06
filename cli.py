import re

def parse_cmdg_line(line, context):
    line = line.strip()
    
    # 1. دعم الجمل الشرطية (iz)
    if line.startswith("iz"):
        # استخراج الشرط والأمر المُراد تنفيذه بين علامات %
        match = re.match(r"iz\s*\((.*?)\)\s*%\s*(.*?)\s*%", line)
        if match:
            condition, action = match.groups()
            # تقييم الشرط ببساطة (على سبيل المثال التحقق من التساوي)
            if "==" in condition:
                left, right = condition.split("==")
                left_val = context.get(left.strip(), left.strip().strip("'"))
                right_val = context.get(right.strip(), right.strip().strip("'"))
                
                if left_val == right_val:
                    parse_cmdg_line(action, context) # تنفيذ الأمر المشروط
            return

    # 2. دعم الحلقات التكرارية (krar)
    if line.startswith("krar"):
        match = re.match(r"krar\s*\((.*?)\)\s*%\s*(.*?)\s*%", line)
        if match:
            times_str, action = match.groups()
            times = int(times_str.strip())
            for _ in range(times):
                parse_cmdg_line(action, context) # تكرار تنفيذ الأمر
            return

    # الأوامر الأساسية القديمة للغة
    if line.startswith("kars"):
        val = re.findall(r"'(.*?)'", line)
        if val: context['kara'] = val[0]
    elif line.startswith("ja"):
        if 'kara' in context:
            print(context['kara'])
          

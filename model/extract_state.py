import re

def extract_state(text):
    # Use regular expressions to find the desired substring
    match = re.search(r'(辽宁|北京|天津|山东|山西|河北|河南)', text)
    if match:
        return match.group()
    else:
        return None
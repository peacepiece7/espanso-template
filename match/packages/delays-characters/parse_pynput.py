# Intended for use with the delays-characters package.yml file.
# Uses the Python pynput library to inject text, instead of Espanso. Enables the 
# addition of pauses (sleep) and <Tab> etc. keys and can include Espanso {{variables}}
# See https://pynput.readthedocs.io/en/latest/keyboard.html#controlling-the-keyboard
# Supports type, tap, press, release, and sleep

import argparse, time, random, string
try:
    from pynput.keyboard import Controller, Key
except ImportError:
    import sys
    print("Error: The 'pynput' library is not installed.", file=sys.stderr)
    print("Install it using: pip install pynput", file=sys.stderr)
    sys.exit(1)  # Exit with a non-zero status code to indicate failure


# Initialize the keyboard controller
keyboard = Controller()

def generate_random_short_string():
    """2-3단어 랜덤 문자열 생성"""
    words = ['blue', 'red', 'green', 'yellow', 'black', 'white', 'sky', 'ocean', 'mountain', 'river', 'tree', 'flower', 'bird', 'fish', 'cat', 'dog', 'sun', 'moon', 'star', 'cloud', 'wind', 'rain', 'snow', 'fire', 'earth', 'water', 'air']
    return ' '.join(random.sample(words, random.randint(2, 3)))

def generate_random_long_string():
    """2-3문장 랜덤 문자열 생성"""
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "All work and no play makes Jack a dull boy.",
        "To be or not to be, that is the question.",
        "A journey of a thousand miles begins with a single step.",
        "Practice makes perfect.",
        "Actions speak louder than words.",
        "Better late than never.",
        "Don't judge a book by its cover.",
        "Time waits for no one.",
        "Knowledge is power.",
        "Where there's a will, there's a way.",
        "The early bird catches the worm.",
        "You can't teach an old dog new tricks.",
        "A picture is worth a thousand words.",
        "The pen is mightier than the sword.",
        "When in Rome, do as the Romans do.",
        "Every cloud has a silver lining.",
        "The grass is always greener on the other side."
    ]
    return '\n'.join(random.sample(sentences, random.randint(2, 4)))

def generate_random_phone():
    """010-NNNN-NNNN 형식 랜덤 전화번호 생성"""
    middle = ''.join(random.choices(string.digits, k=4))
    last = ''.join(random.choices(string.digits, k=4))
    return f"010-{middle}-{last}"

def generate_random_date():
    """YYYY-MM-DD 형식 랜덤 날짜 생성"""
    year = random.randint(2020, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # 28일로 제한하여 유효한 날짜 보장
    return f"{year:04d}-{month:02d}-{day:02d}"

def generate_random_email():
    """랜덤 이메일 주소 생성"""
    # 사용자명 부분
    first_names = ['john', 'jane', 'mike', 'sarah', 'david', 'lisa', 'chris', 'emma', 'alex', 'anna', 'tom', 'kate', 'sam', 'lucy', 'ben', 'zoe', 'dan', 'mia', 'joe', 'eva']
    last_names = ['smith', 'johnson', 'williams', 'brown', 'jones', 'garcia', 'miller', 'davis', 'rodriguez', 'martinez', 'hernandez', 'lopez', 'gonzalez', 'wilson', 'anderson', 'thomas', 'taylor', 'moore', 'jackson', 'martin']
    
    # 도메인 부분
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'naver.com', 'daum.net', 'company.com', 'example.com', 'test.com', 'demo.org']
    
    # 랜덤 조합 생성
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    domain = random.choice(domains)
    
    # 사용자명 형식 랜덤 선택
    username_formats = [
        f"{first_name}.{last_name}",
        f"{first_name}{last_name}",
        f"{first_name}_{last_name}",
        f"{first_name}{random.randint(10, 99)}",
        f"{first_name}.{last_name}{random.randint(10, 99)}",
        f"{last_name}.{first_name}",
        f"{first_name[0]}{last_name}",
        f"{first_name}{last_name[0]}"
    ]
    
    username = random.choice(username_formats)
    return f"{username}@{domain}"

def parse_and_execute_commands(commands):
    lines = commands.strip().splitlines()

    for line in lines:
        line = line.strip()
        if line.startswith('type'):
            text = line[len('type '):].strip()
            keyboard.type(text)
        
        elif line.startswith('tap'):
            keys = line[len('tap '):].strip().lower().split('+')
            keys = [k.strip() for k in keys]
            if len(keys) == 1:
                key = getattr(Key, keys[0], keys[0])
                keyboard.tap(key)
            else:
                # 여러 키 조합 (예: ctrl + l)
                key_objs = []
                for k in keys:
                    if hasattr(Key, k):
                        key_objs.append(getattr(Key, k))
                    else:
                        key_objs.append(k)
                # 조합키 누르기
                for k in key_objs[:-1]:
                    keyboard.press(k)
                keyboard.tap(key_objs[-1])
                for k in reversed(key_objs[:-1]):
                    keyboard.release(k)
        
        elif line.startswith('press'):
            key_name = line[len('press '):].strip().lower()
            key = getattr(Key, key_name, key_name)
            keyboard.press(key)

        elif line.startswith('release'):
            key_name = line[len('release '):].strip().lower()
            key = getattr(Key, key_name, key_name)
            keyboard.release(key)
        
        elif line.startswith('sleep'):
            time_to_sleep = float(line[len('sleep '):].strip())
            time.sleep(time_to_sleep)
        
        elif line.startswith('random_short'):
            text = generate_random_short_string()
            keyboard.type(text)
        
        elif line.startswith('random_long'):
            text = generate_random_long_string()
            keyboard.type(text)
        
        elif line.startswith('random_phone'):
            text = generate_random_phone()
            keyboard.type(text)
        
        elif line.startswith('random_date'):
            text = generate_random_date()
            keyboard.type(text)
        
        elif line.startswith('random_email'):
            text = generate_random_email()
            keyboard.type(text)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Execute keyboard automation commands.")
    parser.add_argument('trig', type=str, help='The trigger key to simulate.')
    parser.add_argument('input', type=str, help='The input commands to execute.')
    args = parser.parse_args()

    # Press backspace key as many times as the length of the trigger
    for _ in args.trig: keyboard.tap(Key.backspace)

    # Parse and execute the input commands
    if args.input:
        parse_and_execute_commands(args.input)
    else:
        print("No input provided.")

    # Replace trigger for Espanso to remove after the script
    keyboard.type(args.trig)

if __name__ == "__main__":
    main()

import sys # ⬅️ تم تصحيح الكتابة من Import إلى import
import time
import os
import aiohttp
import asyncio
import random
import uuid
import string
import hashlib
import base64
import json
# ⚠️ يجب التأكد من وجود هذه المكتبة في بيئة التشغيل
import ms4 
import re
import fake_useragent
import telebot

MAG = "\033[35m"
PINK = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def premium_loader(seconds=4):
    clear()
    print(f"{MAG}{BOLD}")
    print("╔══════════════════════════════════════╗")
    print("║       PREMIUM TOOLS LOADING...       ║")
    print("╚══════════════════════════════════════╝\n"+RESET)

    total_steps = 40
    delay = seconds / total_steps

    for i in range(total_steps + 1):
        percent = int((i / total_steps) * 100)
        bar_fill = "█" * i
        bar_empty = "░" * (total_steps - i)
        sys.stdout.write(f"\r{PINK}[{bar_fill}{bar_empty}] {percent}%")
        sys.stdout.flush()
        time.sleep(delay)

    print(f"\n\n{MAG}✅ جاهز للعمل!{RESET}")

premium_loader()

def ui():
    clear()
    print(f"""{MAG}{BOLD}
╔═══════════════════════════════════════════════════════╗
║            PREMIUM tiklist TOOL - MWAML               ║
╚═══════════════════════════════════════════════════════╝
{RESET}""")

ui()
BOT_TOKEN = input(f"{PINK}[🔑] TOKIN: {RESET}").strip()

# ===== المكتبات =====
# تم تجميعها في بداية الملف

try:
    bot = telebot.TeleBot(BOT_TOKEN)
except Exception as e:
    print(f"❌ خطأ في تهيئة البوت: {e}")
    sys.exit()

# ===== متغيرات =====
ss = {}
ua_gen = fake_useragent.FakeUserAgent()
STOP_FLAGS = {}
GLOBAL_CACHE = set()

# ===== أدوات =====
def rn(l=10):
    return ''.join(random.choice(string.digits) for _ in range(l))

def ru():
    return str(uuid.uuid4())

def ra():
    br = ["Infinix", "Samsung", "Xiaomi", "Huawei"]
    mo = ["X692", "A52", "M21", "Note9"]
    av = ["10", "11", "12", "13"]
    return f"Android {random.choice(av)}; {random.choice(br)} {random.choice(mo)}"

def gx(ts):
    b = hashlib.md5(str(ts).encode()).hexdigest()
    return "8404" + b[:30]

def ga(ts, di, ii):
    r = f"{di}:{ii}:{ts}"
    h = hashlib.sha256(r.encode()).digest()
    return base64.b64encode(h).decode()

def gp(pd):
    e = json.dumps(pd).encode()
    return base64.b64encode(e).decode()

# ===== شريط تقدم =====
def real_progress(done, total, scraped):
    percent = int((done / total) * 100) if total else 0
    size = 20
    filled = int(size * percent / 100)
    bar = "█" * filled + "░" * (size - filled)

    return (
        f"⏳ جاري السحب...\n\n"
        f"[{bar}] {percent}%\n"
        f"✅ الحسابات المكتملة: {done}/{total}\n"
        f"📥 اليوزرات المسحوبة: {scraped}"
    )

# ===== لودر تيليجرام =====
def premium_startup_frames():
    return [
        "💎 MWAML PREMIUM ENGINE\n\n⏳ جاري التهيئة ░░░░░░░░░░",
        "💎 MWAML PREMIUM ENGINE\n\n⏳ جاري التهيئة █░░░░░░░░░",
        "💎 MWAML PREMIUM ENGINE\n\n⏳ جاري التهيئة ██░░░░░░░░",
        "💎 MWAML PREMIUM ENGINE\n\n⏳ جاري التهيئة ███░░░░░░░",
        "💎 MWAML PREMIUM ENGINE\n\n⏳ جاري التهيئة ████░░░░░░",
        "💎 MWAML PREMIUM ENGINE\n\n✅ تم تجهيز الأداة بنجاح!"
    ]

# ===== كابتشا =====
def generate_math():
    op = random.choice(['+', '-', '*', '/'])
    if op == '+':
        a, b = random.randint(1,20), random.randint(1,20)
        ans = a+b
    elif op == '-':
        a, b = random.randint(10,30), random.randint(1,10)
        ans = a-b
    elif op == '*':
        a, b = random.randint(1,10), random.randint(1,10)
        ans = a*b
    else:
        b = random.randint(1,10)
        ans = random.randint(2,10)
        a = ans*b
    return f"{a} {op} {b}", ans

# ===== مهمة السحب المعدلة لاسترجاع النتائج =====
async def pu(user, chat):
    if STOP_FLAGS.get(chat):
        return set()

    sn = set()

    try:
        # ⚠️ التأكد من وجود مكتبة ms4
        info = ms4.InfoTik.TikTok_Info(user) 
        tid = info.get("id", "")
        
        if not tid:
            print(f"⚠️ فشل الحصول على TID لليوزر: {user}")
            return set()

        pt = ""

        while True:
            if STOP_FLAGS.get(chat):
                break

            ts = int(time.time())
            did = rn(19)
            iid = rn(19)

            hd = {
                "User-Agent": ra(),
                "x-khronos": str(ts),
                "x-argus": ga(ts, did, iid),
                "x-gorgon": gx(ts),
                "X-Tt-Params": gp({"iid": iid, "device_id": did})
            }

            api = f"https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/following/list/?user_id={tid}&count=200&page_token={pt}"

            try:
                async with aiohttp.ClientSession() as ses:
                    async with ses.get(api, headers=hd) as res:
                        if res.status != 200:
                            print(f"❌ فشل API لليوزر {user}، الحالة: {res.status}")
                            break
                        js = await res.json()

                for x in js.get("followings", []):
                    u = x["unique_id"]
                    if u not in sn and u not in GLOBAL_CACHE:
                        sn.add(u)
                        GLOBAL_CACHE.add(u)
                        
                if not js.get("has_more"):
                    break
                pt = js.get("next_page_token", "")
                
                await asyncio.sleep(random.uniform(0.5, 1.5))
                
            except aiohttp.ClientError as e:
                print(f"❌ خطأ في طلب HTTP لليوزر {user}: {e}")
                break
            except Exception as e:
                print(f"❌ خطأ غير متوقع أثناء السحب من {user}: {e}")
                break
                
    except Exception as e:
        print(f"❌ فشل تهيئة السحب لليوزر {user}: {e}")
        pass
        
    return sn # ⬅️ ترجع مجموعة اليوزرات التي تم سحبها

# ===== أوامر البوت =====
@bot.message_handler(commands=['start'])
def start(m):
    frames = premium_startup_frames()
    msg = bot.send_message(m.chat.id, frames[0])

    for i in range(1, len(frames)):
        time.sleep(0.25)
        try:
            bot.edit_message_text(
                chat_id=m.chat.id,
                message_id=msg.message_id,
                text=frames[i]
            )
        except:
            pass

    q, a = generate_math()
    ss[m.chat.id] = {"s": "math", "ans": a}

    try:
        bot.edit_message_text(
            chat_id=m.chat.id,
            message_id=msg.message_id,
            text=f"✅ جاهز للعمل\n\n{q} = ?"
        )
    except:
        bot.send_message(m.chat.id, f"✅ جاهز للعمل\n\n{q} = ?")

@bot.message_handler(commands=['stop'])
def stop(m):
    STOP_FLAGS[m.chat.id] = True
    bot.send_message(m.chat.id, "⛔ تم الإيقاف، يرجى الانتظار حتى تكتمل المهام الحالية.")

@bot.message_handler(func=lambda m: m.chat.id in ss)
def handler(m):
    s = ss[m.chat.id]

    if s["s"] == "math":
        try:
            if int(m.text.strip()) != s["ans"]:
                q, a = generate_math()
                s["ans"] = a
                bot.send_message(m.chat.id, f"غلط ❌\n{q} = ?")
                return
        except:
            bot.send_message(m.chat.id, "اكتب رقم فقط")
            return

        s["s"] = "users"
        bot.send_message(m.chat.id, "✅ ارسل اليوزرات")
        return

    if s["s"] == "users":
        users = list(set([x.strip() for x in m.text.split() if x.strip()]))
        if not users:
            bot.send_message(m.chat.id, "لا يوجد يوزرات")
            return

        total_users = len(users)
        sm = bot.send_message(m.chat.id, real_progress(0, total_users, 0))

        async def run():
            GLOBAL_CACHE.clear()
            STOP_FLAGS[m.chat.id] = False

            file_path = "user.txt"
            if os.path.exists(file_path):
                os.remove(file_path)

            done_count = 0
            scraped_count = 0
            
            # 💡 دالة لتحديث شريط التقدم 
            def update_progress(done_c, scraped_c):
                nonlocal done_count, scraped_count
                done_count = done_c
                scraped_count = scraped_c
                try:
                    bot.edit_message_text(
                        chat_id=m.chat.id,
                        message_id=sm.message_id,
                        text=real_progress(done_c, total_users, scraped_c)
                    )
                except Exception as e:
                    print(f"⚠️ فشل تحديث رسالة التقدم: {e}") 
                    pass

            # 💡 تشغيل المهام بشكل متزامن
            tasks = [pu(u, m.chat.id) for u in users]
            
            all_scraped_users = set()
            
            # نستخدم as_completed لتحديث شريط التقدم مباشرة بعد انتهاء كل مهمة
            for future in asyncio.as_completed(tasks):
                try:
                    user_set = await future
                    all_scraped_users.update(user_set)
                except Exception as e:
                    print(f"❌ خطأ في مهمة السحب: {e}")

                done_count += 1
                scraped_count = len(all_scraped_users)
                
                # تحديث التقدم بعد اكتمال كل يوزر
                update_progress(done_count, scraped_count)

                if STOP_FLAGS.get(m.chat.id):
                    break
            
            # 3. حفظ جميع اليوزرات المجمعة في ملف واحد
            if all_scraped_users:
                with open(file_path, "w", encoding="utf-8") as f:
                    for u in all_scraped_users:
                        f.write(u + "\n")
            
            # 4. إرسال الملف بعد الانتهاء
            final_text = ""
            if STOP_FLAGS.get(m.chat.id):
                final_text = f"⛔ تم الإيقاف بناءً على طلبك.\n\n✅ تم سحب: {len(all_scraped_users)} يوزر قبل الإيقاف."
            else:
                final_text = f"✅ اكتمل السحب بنجاح!\n\n📥 اليوزرات المسحوبة: {len(all_scraped_users)}"

            try:
                bot.edit_message_text(
                    chat_id=m.chat.id,
                    message_id=sm.message_id,
                    text=final_text
                )
            except:
                bot.send_message(m.chat.id, final_text)

            if os.path.exists(file_path):
                try:
                    with open(file_path, "rb") as f:
                        bot.send_document(m.chat.id, f)
                except Exception as e:
                    bot.send_message(m.chat.id, f"❌ فشل إرسال الملف: {e}")
                finally:
                    os.remove(file_path)

        asyncio.run(run())
        s["s"] = "done"

# ===== تشغيل البوت =====
print(f"{MAG}🤖 البوت قيد التشغيل...{RESET}")
bot.infinity_polling()

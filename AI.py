import difflib, re, json

# Load saved memory if available
try:
    with open("memory.json") as f:
        a = json.load(f)
    print("📂 Loaded previous memory.")
except:
    a = {}
    print("🆕 Starting fresh.")

b = {}         # last essay's Q&A
skipped = []   # skipped sentences

def c(x, y, z = 0.8):
    m = difflib.get_close_matches(x, y, n = 1, cutoff = z)
    return m[0] if m else None

def extract_patterns(g):
    f = {}
    g = g.strip()
    if len(g.split()) < 4:
        skipped.append(g)
        return f

    # Core Definitions & Identity
    if " is " in g and g.count(" is ") == 1:
        h = g.split(" is ", 1)
        f[f"what is {h[0].strip()}"] = h[1].strip()
    elif " means " in g:
        h = g.split(" means ", 1)
        f[f"what does {h[0].strip()} mean"] = h[1].strip()
    elif " refers to " in g:
        h = g.split(" refers to ", 1)
        f[f"what does {h[0].strip()} refer to"] = h[1].strip()
    elif " is called " in g:
        h = g.split(" is called ", 1)
        f[f"what is {h[0].strip()} called"] = h[1].strip()
    elif " is known as " in g:
        h = g.split(" is known as ", 1)
        f[f"what is {h[0].strip()} known as"] = h[1].strip()
    elif " is defined as " in g:
        h = g.split(" is defined as ", 1)
        f[f"how is {h[0].strip()} defined"] = h[1].strip()
    elif " defines " in g:
        h = g.split(" defines ", 1)
        f[f"what defines {h[1].strip()}"] = h[0].strip()
    elif " stands for " in g:
        h = g.split(" stands for ", 1)
        f[f"what does {h[0].strip()} stand for"] = h[1].strip()
    elif " symbolizes " in g:
        h = g.split(" symbolizes ", 1)
        f[f"what does {h[0].strip()} symbolize"] = h[1].strip()
    elif " represents " in g:
        h = g.split(" represents ", 1)
        f[f"what does {h[0].strip()} represent"] = h[1].strip()
    elif ":" in g and g.count(":") == 1:
        h = g.split(":", 1)
        f[f"what is {h[0].strip()}"] = h[1].strip()
    # Composition & Structure
    elif " consists of " in g:
        h = g.split(" consists of ", 1)
        f[f"what does {h[0].strip()} consist of"] = h[1].strip()
    elif " includes " in g and "," not in g:
        h = g.split(" includes ", 1)
        f[f"what does {h[0].strip()} include"] = h[1].strip()
    elif " is made of " in g:
        h = g.split(" is made of ", 1)
        f[f"what is {h[0].strip()} made of"] = h[1].strip()
    elif " is composed of " in g:
        h = g.split(" is composed of ", 1)
        f[f"what is {h[0].strip()} composed of"] = h[1].strip()
    elif " is formed by " in g:
        h = g.split(" is formed by ", 1)
        f[f"what is {h[0].strip()} formed by"] = h[1].strip()
    elif " is built from " in g:
        h = g.split(" is built from ", 1)
        f[f"what is {h[0].strip()} built from"] = h[1].strip()

    # Classification & Types
    elif " is classified as " in g:
        h = g.split(" is classified as ", 1)
        f[f"how is {h[0].strip()} classified"] = h[1].strip()
    elif " is categorized as " in g:
        h = g.split(" is categorized as ", 1)
        f[f"how is {h[0].strip()} categorized"] = h[1].strip()
    elif " is grouped into " in g:
        h = g.split(" is grouped into ", 1)
        f[f"how is {h[0].strip()} grouped"] = h[1].strip()
    elif " is divided into " in g:
        h = g.split(" is divided into ", 1)
        f[f"how is {h[0].strip()} divided"] = h[1].strip()
    elif " are types of " in g:
        h = g.split(" are types of ", 1)
        f[f"what are types of {h[1].strip()}"] = h[0].strip()
    elif " are examples of " in g:
        h = g.split(" are examples of ", 1)
        f[f"what are examples of {h[1].strip()}"] = h[0].strip()
    # Cause & Effect Relationships
    elif re.search(r"\b(leads to|results in|causes|triggers|enables|facilitates|initiates|sparks|explains|produces|generates|requires|prevents|supports)\b", g):
        h = re.split(r"\b(leads to|results in|causes|triggers|enables|facilitates|initiates|sparks|explains|produces|generates|requires|prevents|supports)\b", g, maxsplit=1)
        f[f"what does {h[0].strip()} {h[1].strip()}"] = h[2].strip()

    # Passive Voice Constructions
    elif re.search(r"\bwas .* by\b", g):
        h = re.search(r"(.+?) was (.+?) by (.+)", g)
        if h:
            f[f"what did {h.group(3).strip()} {h.group(2).strip()}"] = h.group(1).strip()
    elif re.search(r"\bwere .* by\b", g):
        h = re.search(r"(.+?) were (.+?) by (.+)", g)
        if h:
            f[f"what did {h.group(3).strip()} {h.group(2).strip()}"] = h.group(1).strip()   
    # Quantities & Percentages
    elif re.search(r"\bconstitutes\b", g):
        h = g.split(" constitutes ", 1)
        f[f"how much of {h[1].strip()} is {h[0].strip()}"] = h[0].strip()
    elif re.search(r"\b(\d+\.?\d*)% (.*?)\b", g):
        h = re.search(r"(\d+\.?\d*)% (.*?)", g)
        if h:
            f[f"how much of {h.group(2).strip()}"] = f"{h.group(1)} percent"

    # Hypotheses & Possibilities
    elif " is thought to " in g:
        h = g.split(" is thought to ", 1)
        f[f"what is {h[0].strip()} thought to do"] = h[1].strip()
    elif " is believed to " in g:
        h = g.split(" is believed to ", 1)
        f[f"what is {h[0].strip()} believed to do"] = h[1].strip()
    elif " is considered to be " in g:
        h = g.split(" is considered to be ", 1)
        f[f"what is {h[0].strip()} considered to be"] = h[1].strip()
    elif " is favored by " in g:
        h = g.split(" is favored by ", 1)
        f[f"what is favored by {h[1].strip()}"] = h[0].strip()
    elif " is accepted by " in g:
        h = g.split(" is accepted by ", 1)
        f[f"what is accepted by {h[1].strip()}"] = h[0].strip()

    # Alternatives & Theories
    elif " are alternatives to " in g:
        h = g.split(" are alternatives to ", 1)
        f[f"what are alternatives to {h[1].strip()}"] = h[0].strip()
    elif " are theories of " in g:
        h = g.split(" are theories of ", 1)
        f[f"what are theories of {h[1].strip()}"] = h[0].strip()
    elif " are hypotheses about " in g:
        h = g.split(" are hypotheses about ", 1)
        f[f"what are hypotheses about {h[1].strip()}"] = h[0].strip()
    # Actions & Discoveries
    elif " began to " in g:
        h = g.split(" began to ", 1)
        f[f"what did {h[0].strip()} begin to do"] = h[1].strip()
    elif " started " in g:
        h = g.split(" started ", 1)
        f[f"what did {h[0].strip()} start"] = h[1].strip()
    elif " did " in g:
        h = g.split(" did ", 1)
        f[f"what did {h[0].strip()} do"] = h[1].strip()
    elif " discovered " in g:
        h = g.split(" discovered ", 1)
        f[f"who discovered {h[1].strip()}"] = h[0].strip()
    elif " invented " in g:
        h = g.split(" invented ", 1)
        f[f"who invented {h[1].strip()}"] = h[0].strip()
    elif " developed " in g:
        h = g.split(" developed ", 1)
        f[f"who developed {h[1].strip()}"] = h[0].strip()

    # List Parsing
    elif " includes " in g and "," in g:
        h = g.split(" includes ", 1)
        items = [i.strip() for i in re.split(r",| and ", h[1])]
        for item in items:
            f[f"what does {h[0].strip()} include"] = item
    elif " consists of " in g and "," in g:
        h = g.split(" consists of ", 1)
        items = [i.strip() for i in re.split(r",| and ", h[1])]
        for item in items:
            f[f"what does {h[0].strip()} consist of"] = item
    elif " allowed for " in g and "," in g:
        h = g.split(" allowed for ", 1)
        items = [i.strip() for i in re.split(r",| and ", h[1])]
        for item in items:
            f[f"what did {h[0].strip()} allow for"] = item

    # Final catch-all
    elif " is used to " in g:
        h = g.split(" is used to ", 1)
        f[f"what is {h[0].strip()} used to do"] = h[1].strip()
    elif " is difficult to " in g:
        h = g.split(" is difficult to ", 1)
        f[f"why is {h[0].strip()} difficult to do"] = h[1].strip()

    return f                         
def d(t, s):
    t = t.lower().strip()
    e = re.split(r"[.!?]\s*", t)
    f = {}

    for g in e:
        g = g.strip()
        if not g:
            continue

        result = extract_patterns(g)
        if result:
            f.update(result)
        else:
            skipped.append(g)

    s.update(f)
    return f

# Main loop
while True:
    q = input("\n🟢 Ask (type 'exit', 'learn', 'save', 'learn-list', '/learn-skip', '/learn-1,2,3', '/learn-skip-1,2,3,...'): ").lower().strip("?")

    if q == "exit":
        break

    elif q == "save":
        with open("memory.json", "w") as f:
            json.dump(a, f)
        print("💾 Saved everything to memory.json!")
        continue

    elif q == "learn":
        t = input("🟣 Paste essay: ")
        b = d(t, a)
        print(f"✅ Learned {len(b)} items from your essay.")
        continue

    elif q == "learn-list":
        if a:
            print("\n📘 Everything I've learned:")
            for k, v in a.items():
                print(f"- {k}? → {v}")
        else:
            print("🔴 Nothing learned yet.")
        continue

    elif q == "/learn-skip":
        if skipped:
            print("\n🔍 Sentences I skipped:")
            for i, s in enumerate(skipped, 1):
                print(f"{i}. {s}")
        else:
            print("✅ No skipped sentences yet.")
        continue

    elif q.startswith("/learn-") and q[7:].replace(",", "").isdigit():
        indexes = q[7:].split(",")
        if not b:
            print("🔴 No recent essay learned.")
            continue

        print("\n🟠 What did I learn:")
        if "1" in indexes:
            print("\n🔹 Questions:")
            for k in b.keys():
                print(f"- {k}?")
        if "2" in indexes:
            print("\n🔹 Answers:")
            for v in b.values():
                print(f"- {v}")
        if "3" in indexes:
            print("\n🔹 Q&A:")
            for k, v in b.items():
                print(f"- {k}? → {v}")
        continue

    elif q.startswith("/learn-skip-") and q[13:].replace(",", "").isdigit():
        indexes = q[13:].split(",")
        selected = []

        for i in indexes:
            try:
                idx = int(i) - 1
                if 0 <= idx < len(skipped):
                    selected.append(skipped[idx])
            except:
                continue

        if not selected:
            print("🔴 No valid items selected.")
            continue

        print("🟣 Learning selected skipped sentences...")
        temp = {}
        for g in selected:
            result = extract_patterns(g)
            if result:
                temp.update(result)
            else:
                print(f"⚠️ Still couldn't learn from: {g}")

        a.update(temp)
        b.update(temp)
        print(f"🟢 Learned {len(temp)} new items from skipped list.")
        continue
    if q in a:
        print("🟢 Answer:", a[q])
        continue

    m = c(q, list(a.keys()))
    if m:
        print(f"🟡 Did you mean: '{m}'?")
        r = input("Type 'no' to teach, or Enter to accept: ").strip().lower()
        if r == "no":
            ans = input("🔴 Give correct answer: ").strip()
            a[q] = ans
            print("🟩 Saved!")
        else:
            print("🟢 Answer:", a[m])
    else:
        ans = input("🔴 I don’t know. Teach me: ").strip()
        a[q] = ans
        print("🟩 Saved!")    
"""Generate the Gandalf slide illustration with the newest Gemini image model.

Key: GEMINI_API_KEY env var, or the first line of the file given as argv[1].
Writes x/gandalf_<n>.png (one per candidate).
"""
import base64, json, os, sys, urllib.request

key = os.environ.get("GEMINI_API_KEY") or (open(sys.argv[1]).readline().strip() if len(sys.argv) > 1 else "")
if not key:
    sys.exit("no key: set GEMINI_API_KEY or pass a key file")
API = "https://generativelanguage.googleapis.com/v1beta"


def call(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    return json.load(urllib.request.urlopen(req, timeout=300))


models = [m["name"] for m in call(f"{API}/models?pageSize=1000")["models"]
          if "image" in m["name"] and "generateContent" in m.get("supportedGenerationMethods", [])]
print("image models:", models)
pref = [m for m in models if "pro" in m] or models
model = sorted(pref)[-1]
print("using", model)

PROMPT = """A richly detailed, original fantasy book illustration in the tradition of classic illustrated editions of
children's fantasy novels: fine pen-and-ink linework with layered watercolour washes, warm golden light, hand-painted texture.

Scene: at golden dusk, a tall old wandering wizard in a long grey cloak and a tall pointed grey hat, with a long white beard
and a gnarled wooden staff whose tip glows with a soft white light, stands on a grassy hill beside the round green door of a
cosy hillside burrow-home set into the slope. With the end of his staff he is scratching a small glowing rune onto the door.
A small, plump, barefoot gentleman in a waistcoat peeks out of a round window, half alarmed, half curious, holding a pipe.
Behind the wizard, a winding road leads down past patchwork fields, a mill and a little river, toward far blue misty mountains
where a lone mountain peak glints faintly in the distance. Thirteen tiny hooded travellers with packs walk up the road toward
the door, lanterns lit. Fireflies and drifting sparks of magic swirl around the staff. Puffs of pipe-smoke curl into the shape
of a ship sailing over the hills.

Composition: wide 16:9 landscape. Keep the wizard, door and hobbit in the left 60% of the frame. The right third is open
evening sky and soft distant mountains, darker and calm, with no important detail, so text can be laid over it.
No text, no letters, no logos, no borders, no signature."""

body = {"contents": [{"parts": [{"text": PROMPT}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"], "imageConfig": {"aspectRatio": "16:9"}}}
os.makedirs("x", exist_ok=True)
n = 0
for attempt in range(int(os.environ.get("N", "2"))):
    out = call(f"{API}/{model}:generateContent", body)
    for part in out.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        if "inlineData" in part:
            n += 1
            p = f"x/gandalf_{n}.png"
            open(p, "wb").write(base64.b64decode(part["inlineData"]["data"]))
            print("wrote", p)
        elif "text" in part:
            print("text:", part["text"][:300])
if not n:
    sys.exit("no image returned: " + json.dumps(out)[:800])

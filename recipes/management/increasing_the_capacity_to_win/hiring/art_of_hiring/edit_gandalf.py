import base64,json,os,sys,urllib.request
key=os.environ["GEMINI_API_KEY"]
img=base64.b64encode(open('x/gandalf_2k.png','rb').read()).decode()
PROMPT="""Edit this illustration. Keep the wizard, the hobbit at the round window, the green round door, the hill, the valley, mill, river, mountains, the dusk light and the pen-and-ink watercolour style exactly as they are.

Change 1: remove the sailing ship in the pipe smoke completely; leave only soft curling pipe smoke.

Change 2: replace the small hooded walkers on the road with thirteen proper dwarves: short, broad, stocky and grizzled, with weathered faces, big noses, bushy eyebrows and very long beards, several beards tucked into wide belts. Each wears a long travelling cloak and a colourful hood: one dark-green hood (blue beard, golden belt), one very old dwarf with a white beard in a scarlet hood, two young yellow-bearded dwarves in blue hoods, one proud leader at the front in a sky-blue hood with a long silver tassel and a golden chain, others in purple, grey, brown and white hoods, two in yellow hoods, and one enormously fat dwarf in a pale-green hood puffing at the back. They carry heavy packs, bags, tools, lanterns, and musical instruments (a fiddle, flutes, a drum, a viol). They trudge up the road toward the door in a loose line.

No text, no letters, no signature."""
for i in range(int(os.environ.get("N","2"))):
    body={"contents":[{"parts":[{"inlineData":{"mimeType":"image/png","data":img}},{"text":PROMPT}]}],
      "generationConfig":{"responseModalities":["TEXT","IMAGE"],"imageConfig":{"aspectRatio":"16:9","imageSize":"2K"}}}
    req=urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent",data=json.dumps(body).encode(),headers={"Content-Type":"application/json","x-goog-api-key":key})
    out=json.load(urllib.request.urlopen(req,timeout=400))
    for p in out["candidates"][0]["content"]["parts"]:
        if "inlineData" in p:
            open(f'x/dwarves_{i+1}.png','wb').write(base64.b64decode(p["inlineData"]["data"])); print("ok",i+1)

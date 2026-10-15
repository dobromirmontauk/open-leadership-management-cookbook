G,O="#63E14F","#FF832A"
W='stroke-linecap="round" stroke-linejoin="round"'
snail=(f'<svg aria-label="A snail with a rocket strapped to its shell" width="240" height="170" viewBox="0 0 240 170"><g fill="none" stroke="{G}" stroke-width="7" {W}>'
 '<path d="M20 140 H200 C214 140 222 128 214 116 C206 104 190 110 186 96 L180 70"/>'
 '<path d="M180 70 L172 40 M190 68 L200 40"/><circle cx="172" cy="36" r="5" fill="#63E14F"/><circle cx="200" cy="36" r="5" fill="#63E14F"/>'
 '<circle cx="110" cy="96" r="44"/><path d="M110 96 m-22 0 a22 22 0 1 1 22 22 a12 12 0 1 1 -10 -12"/>'
 f'</g><g {W}><path d="M66 50 L130 50 L146 58 L130 66 L66 66 Z" fill="#1A1A1A" stroke="{O}" stroke-width="6"/>'
 f'<path d="M80 50 L70 38 M80 66 L70 78" stroke="{O}" stroke-width="6"/>'
 f'<path d="M64 52 L36 58 L64 64" fill="{O}" stroke="{O}" stroke-width="4"/><path d="M40 54 L16 58 L40 62" fill="#F5D227" stroke="#F5D227" stroke-width="3"/></g>'
 '<path d="M8 120 H40 M0 132 H28" stroke="#3A3E47" stroke-width="5" stroke-linecap="round"/></svg>')
torch=(f'<svg aria-label="A blazing torch" width="240" height="170" viewBox="0 0 240 170"><g {W}>'
 f'<path d="M120 12 C150 40 158 66 140 86 C150 60 132 52 128 40 C124 62 100 66 104 90 C82 74 90 44 120 12 Z" fill="{O}" stroke="{O}" stroke-width="4"/>'
 f'<path d="M120 50 C134 66 132 80 122 90 C112 82 110 68 120 50 Z" fill="#F5D227" stroke="#F5D227" stroke-width="3"/>'
 f'<path d="M92 92 H148 L138 112 H102 Z" fill="none" stroke="{G}" stroke-width="7"/>'
 f'<path d="M106 112 L116 162 H124 L134 112" fill="none" stroke="{G}" stroke-width="7"/>'
 f'<path d="M60 40 L72 48 M180 40 L168 48 M52 84 H68 M188 84 H172" stroke="{O}" stroke-width="5"/></g></svg>')
hammock=(f'<svg aria-label="A figure relaxing in a hammock under the sun" width="240" height="170" viewBox="0 0 240 170"><g fill="none" {W}>'
 f'<circle cx="196" cy="34" r="16" fill="{O}" stroke="{O}" stroke-width="4"/><path d="M196 6 V12 M196 56 V62 M168 34 H174 M218 34 H224 M176 14 L180 18 M216 14 L212 18" stroke="{O}" stroke-width="4"/>'
 f'<path d="M30 160 V70 M210 160 V80" stroke="{G}" stroke-width="7"/>'
 f'<path d="M30 70 C10 60 6 44 14 36 M30 70 C34 50 48 42 62 46 M30 70 C40 58 56 62 60 72" stroke="{G}" stroke-width="6"/>'
 f'<path d="M30 92 C70 140 170 140 210 100" stroke="{G}" stroke-width="7"/>'
 f'<circle cx="82" cy="104" r="12" fill="#1A1A1A" stroke="#E9ECEF" stroke-width="5"/>'
 f'<path d="M94 112 C120 124 146 122 168 112" stroke="#E9ECEF" stroke-width="9"/>'
 f'<path d="M110 70 l10 0 l-10 12 l10 0 M128 52 l8 0 l-8 10 l8 0" stroke="#8B9097" stroke-width="4"/></g></svg>')
ICONS=[snail,torch,hammock]
if __name__=="__main__":
    for i,s in enumerate(ICONS): open(f"x/icon{i}.svg","w").write(s.replace("<svg ",'<svg xmlns="http://www.w3.org/2000/svg" style="background:#1A1A1A" ',1))

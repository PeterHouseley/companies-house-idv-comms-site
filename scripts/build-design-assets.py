#!/usr/bin/env python3
from pathlib import Path
out = Path('assets/generated')
out.mkdir(parents=True, exist_ok=True)
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 360" role="img" aria-labelledby="title desc">
<title id="title">Director IDV communication workflow</title>
<desc id="desc">A compliance communication flow from official guidance to practice wording, client emails, readiness tracking and reminders.</desc>
<defs>
  <filter id="shadow" x="-10%" y="-20%" width="120%" height="150%"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#173c32" flood-opacity="0.16"/></filter>
  <style>
    .bg{fill:#f7f3e8}.ink{fill:#17231f}.deep{fill:#173c32}.green{fill:#1f6a52}.muted{fill:#60706a}.paper{fill:#fffdf7}.rule{stroke:#b9c8bf;stroke-width:2}.dash{stroke:#1f6a52;stroke-width:3;stroke-dasharray:8 9;fill:none}.label{font:800 18px Aptos,Segoe UI,sans-serif}.small{font:750 13px Aptos,Segoe UI,sans-serif}.mono{font:900 12px 'Courier New',monospace;letter-spacing:.08em}
  </style>
</defs>
<rect class="bg" width="920" height="360" rx="28"/>
<path class="dash" d="M190 180 C 275 100, 330 100, 420 178 S 580 260, 720 178"/>
<g filter="url(#shadow)">
  <rect x="42" y="70" width="190" height="220" rx="18" class="paper" stroke="#b9c8bf"/>
  <rect x="58" y="92" width="88" height="24" rx="12" class="deep"/><text x="70" y="109" fill="#fff" class="mono">SOURCE</text>
  <text x="64" y="152" class="label ink">Official guidance</text><text x="64" y="177" class="small muted">public pages, dates,</text><text x="64" y="197" class="small muted">scope and caveats</text>
  <path d="M66 238 h130 M66 258 h96" class="rule"/>
</g>
<g filter="url(#shadow)">
  <rect x="283" y="40" width="190" height="280" rx="18" class="paper" stroke="#b9c8bf"/>
  <rect x="299" y="62" width="102" height="24" rx="12" class="green"/><text x="312" y="79" fill="#fff" class="mono">PRACTICE</text>
  <text x="305" y="122" class="label ink">Approved wording</text><text x="305" y="147" class="small muted">client-safe explainer,</text><text x="305" y="167" class="small muted">FAQ and boundaries</text>
  <rect x="305" y="214" width="136" height="54" rx="10" fill="#dceadf"/><text x="322" y="247" class="small ink">Tone checked</text>
</g>
<g filter="url(#shadow)">
  <rect x="524" y="70" width="190" height="220" rx="18" class="paper" stroke="#b9c8bf"/>
  <rect x="540" y="92" width="88" height="24" rx="12" class="deep"/><text x="553" y="109" fill="#fff" class="mono">CLIENT</text>
  <text x="546" y="152" class="label ink">Email sequence</text><text x="546" y="177" class="small muted">notice, reminder,</text><text x="546" y="197" class="small muted">final chase copy</text>
  <path d="M548 238 h130 M548 258 h90" class="rule"/>
</g>
<g filter="url(#shadow)">
  <rect x="750" y="94" width="128" height="172" rx="18" class="deep"/>
  <text x="774" y="139" fill="#dceadf" class="mono">TRACKER</text>
  <circle cx="782" cy="178" r="8" fill="#dceadf"/><text x="800" y="183" fill="#fff" class="small">Briefed</text>
  <circle cx="782" cy="212" r="8" fill="#b9822e"/><text x="800" y="217" fill="#fff" class="small">Chase</text>
</g>
</svg>'''
(out / 'idv-comms-workflow.svg').write_text(svg)
print(out / 'idv-comms-workflow.svg')

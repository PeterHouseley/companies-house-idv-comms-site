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

control_room = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 520" role="img" aria-labelledby="title desc">
<title id="title">Director IDV deadline control room</title>
<desc id="desc">A professional compliance operating board that maps director ID verification communications from guidance review to client notices, chasers and audit notes.</desc>
<defs>
  <filter id="soft" x="-10%" y="-20%" width="120%" height="150%"><feDropShadow dx="0" dy="22" stdDeviation="20" flood-color="#173c32" flood-opacity="0.17"/></filter>
  <pattern id="paper" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0v32" fill="none" stroke="#173c32" stroke-opacity=".055"/></pattern>
  <style>
    .bg{fill:#f7f1e3}.sheet{fill:#fffdf7;stroke:#b9c8bf}.deep{fill:#173c32}.green{fill:#1f6a52}.mint{fill:#dceadf}.amber{fill:#b9822e}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.rule{stroke:#d7d0c1;stroke-width:2}.dash{stroke:#1f6a52;stroke-width:3;stroke-dasharray:10 9;fill:none}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.mono{font-family:'Courier New',monospace;font-weight:900;letter-spacing:.1em}
  </style>
</defs>
<rect width="1120" height="520" rx="34" class="bg"/><rect width="1120" height="520" rx="34" fill="url(#paper)"/>
<text x="44" y="62" class="mono" font-size="15" fill="#1f6a52">DIRECTOR IDV / ROLLOUT OPERATING BOARD</text>
<text x="44" y="112" class="serif ink" font-size="50">Status, wording, chase dates — one controlled trail.</text>
<g filter="url(#soft)">
  <rect x="46" y="156" width="314" height="286" rx="24" class="sheet"/>
  <rect x="70" y="184" width="114" height="28" rx="14" class="deep"/><text x="88" y="204" class="mono" font-size="13" fill="#fff">GUIDANCE</text>
  <text x="70" y="254" class="serif ink" font-size="33">What changed?</text>
  <path class="rule" d="M72 287h230M72 316h196M72 345h238"/>
  <rect x="72" y="382" width="222" height="32" rx="16" class="mint"/><text x="91" y="404" class="sans" font-size="15" fill="#173c32">Boundary wording approved</text>
</g>
<path class="dash" d="M364 300C424 218 478 218 538 300"/>
<g filter="url(#soft)">
  <rect x="410" y="144" width="302" height="316" rx="24" class="sheet"/>
  <text x="438" y="189" class="mono" font-size="13" fill="#1f6a52">DIRECTOR READINESS LEDGER</text>
  <g class="sans" font-size="14">
    <rect x="438" y="214" width="246" height="42" rx="12" fill="#dceadf"/><text x="456" y="241" fill="#173c32">Briefed</text><text x="626" y="241" fill="#173c32">42</text>
    <rect x="438" y="268" width="246" height="42" rx="12" fill="#f4e1bd"/><text x="456" y="295" fill="#173c32">Needs chase</text><text x="626" y="295" fill="#173c32">17</text>
    <rect x="438" y="322" width="246" height="42" rx="12" fill="#f0d7d1"/><text x="456" y="349" fill="#173c32">No reply</text><text x="632" y="349" fill="#173c32">8</text>
    <rect x="438" y="376" width="246" height="42" rx="12" fill="#fff7e9"/><text x="456" y="403" fill="#173c32">Partner review</text><text x="632" y="403" fill="#173c32">5</text>
  </g>
</g>
<path class="dash" d="M714 300C774 218 824 218 884 300"/>
<g filter="url(#soft)">
  <rect x="758" y="156" width="316" height="286" rx="24" class="deep"/>
  <text x="786" y="204" class="mono" font-size="13" fill="#dceadf">CLIENT COMMS SEQUENCE</text>
  <g class="sans" font-size="16" fill="#fff">
    <circle cx="800" cy="258" r="11" class="green"/><text x="826" y="264">Notice sent with FAQ link</text>
    <circle cx="800" cy="313" r="11" class="amber"/><text x="826" y="319">Reminder due in 7 days</text>
    <circle cx="800" cy="368" r="11" class="red"/><text x="826" y="374">Escalate unresolved cases</text>
  </g>
  <path d="M786 226h244M786 400h196" stroke="#dceadf" stroke-opacity=".34" stroke-width="2"/>
</g>
<g transform="translate(892 50) rotate(6)"><rect x="0" y="0" width="158" height="48" rx="7" fill="none" stroke="#a74739" stroke-width="4"/><text x="19" y="30" class="mono" font-size="14" fill="#a74739">AUDIT NOTES</text></g>
</svg>'''
(out / 'idv-deadline-control-room.svg').write_text(control_room)
partner_briefing = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 640" role="img" aria-labelledby="title desc">
<title id="title">Partner briefing file for Director IDV communications</title>
<desc id="desc">A premium practice file showing a partner decision note, approved staff script, director evidence ledger and reminder cadence for Companies House ID verification client communications.</desc>
<defs>
  <filter id="lift" x="-10%" y="-20%" width="125%" height="155%"><feDropShadow dx="0" dy="26" stdDeviation="22" flood-color="#173c32" flood-opacity="0.18"/></filter>
  <pattern id="grid" width="38" height="38" patternUnits="userSpaceOnUse"><path d="M38 0H0v38" fill="none" stroke="#173c32" stroke-opacity=".055"/></pattern>
  <style>
    .bg{fill:#f5f0e4}.paper{fill:#fffdf7;stroke:#b9c8bf}.deep{fill:#173c32}.green{fill:#1f6a52}.mint{fill:#dceadf}.amber{fill:#d8a24f}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.rule{stroke:#d7d0c1;stroke-width:2}.stamp{font:900 15px 'Courier New',monospace;letter-spacing:.13em}.mono{font:900 13px 'Courier New',monospace;letter-spacing:.09em}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}
  </style>
</defs>
<rect width="1180" height="640" rx="38" class="bg"/><rect width="1180" height="640" rx="38" fill="url(#grid)"/>
<circle cx="1010" cy="116" r="98" fill="none" stroke="#1f6a52" stroke-opacity=".2" stroke-width="2"/><circle cx="1010" cy="116" r="64" fill="none" stroke="#b9822e" stroke-opacity=".28" stroke-width="2"/>
<text x="54" y="66" class="mono" fill="#1f6a52">COMPANIES HOUSE IDV / PARTNER BRIEFING FILE</text>
<text x="54" y="124" class="serif ink" font-size="54">One practice position. One client message. One audit trail.</text>
<g filter="url(#lift)">
  <rect x="60" y="178" width="332" height="374" rx="24" class="paper"/>
  <rect x="84" y="206" width="142" height="30" rx="15" class="deep"/><text x="101" y="227" class="mono" font-size="13" fill="#fff">DECISION NOTE</text>
  <text x="84" y="283" class="serif ink" font-size="34">Partner sign-off</text>
  <text x="84" y="322" class="sans muted" font-size="17">• Practice position</text>
  <text x="84" y="354" class="sans muted" font-size="17">• Client-safe boundaries</text>
  <text x="84" y="386" class="sans muted" font-size="17">• Escalation rules</text>
  <path class="rule" d="M84 428h250M84 462h214M84 496h236"/>
  <g transform="translate(224 436) rotate(-8)"><rect x="0" y="0" width="112" height="42" rx="6" fill="none" stroke="#a74739" stroke-width="4"/><text x="15" y="27" class="stamp" font-size="12" fill="#a74739">APPROVED</text></g>
</g>
<g filter="url(#lift)">
  <rect x="424" y="156" width="358" height="418" rx="26" class="paper"/>
  <rect x="452" y="186" width="126" height="30" rx="15" class="green"/><text x="470" y="207" class="mono" font-size="13" fill="#fff">STAFF SCRIPT</text>
  <text x="452" y="262" class="serif ink" font-size="35">What to send when asked</text>
  <rect x="452" y="302" width="282" height="54" rx="14" fill="#dceadf"/><text x="474" y="335" class="sans ink" font-size="17">Email explainer + FAQ link</text>
  <rect x="452" y="372" width="282" height="54" rx="14" fill="#f6ead0"/><text x="474" y="405" class="sans ink" font-size="17">Phone answer boundaries</text>
  <rect x="452" y="442" width="282" height="54" rx="14" fill="#f0d7d1"/><text x="474" y="475" class="sans ink" font-size="17">Escalate unresolved cases</text>
  <path d="M748 320v158" stroke="#173c32" stroke-opacity=".26" stroke-width="3" stroke-dasharray="8 8"/>
</g>
<g filter="url(#lift)">
  <rect x="814" y="200" width="306" height="330" rx="24" class="deep"/>
  <text x="842" y="242" class="mono" font-size="13" fill="#dceadf">DIRECTOR EVIDENCE LEDGER</text>
  <g class="sans" font-size="15">
    <rect x="842" y="276" width="238" height="44" rx="12" fill="#fffdf7"/><text x="860" y="304" fill="#17231f">Briefed</text><text x="1034" y="304" fill="#1f6a52">42</text>
    <rect x="842" y="336" width="238" height="44" rx="12" fill="#fffdf7"/><text x="860" y="364" fill="#17231f">Chase due</text><text x="1034" y="364" fill="#b9822e">17</text>
    <rect x="842" y="396" width="238" height="44" rx="12" fill="#fffdf7"/><text x="860" y="424" fill="#17231f">No reply</text><text x="1042" y="424" fill="#a74739">8</text>
    <rect x="842" y="456" width="238" height="44" rx="12" fill="#fffdf7"/><text x="860" y="484" fill="#17231f">Partner review</text><text x="1042" y="484" fill="#b9822e">5</text>
  </g>
</g>
<path d="M392 362 C 430 302, 456 302, 494 362" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/><path d="M780 362 C 820 302, 850 302, 890 362" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<rect x="72" y="574" width="588" height="34" rx="17" fill="#173c32"/><text x="94" y="596" class="mono" font-size="12" fill="#fff">ADMINISTRATIVE COMMUNICATIONS SUPPORT ONLY · NOT ID CHECKING · NOT LEGAL ADVICE</text>
</svg>'''
(out / 'idv-partner-briefing-file.svg').write_text(partner_briefing)

correspondence_desk = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 650" role="img" aria-labelledby="title desc">
<title id="title">Director IDV correspondence desk</title>
<desc id="desc">A premium compliance correspondence desk with a client letter, FAQ card, call note, readiness ledger and dated chase slips for a Companies House ID verification rollout.</desc>
<defs>
  <filter id="deskShadow" x="-12%" y="-18%" width="130%" height="150%"><feDropShadow dx="0" dy="28" stdDeviation="24" flood-color="#173c32" flood-opacity="0.20"/></filter>
  <pattern id="fibres" width="44" height="44" patternUnits="userSpaceOnUse"><path d="M44 0H0v44" fill="none" stroke="#173c32" stroke-opacity=".045"/><circle cx="9" cy="28" r="1.4" fill="#b9822e" fill-opacity=".18"/></pattern>
  <style>
    .bg{fill:#efe7d8}.paper{fill:#fffdf7;stroke:#c7bda9}.green{fill:#1f6a52}.deep{fill:#173c32}.mint{fill:#dceadf}.amber{fill:#d8a24f}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.rule{stroke:#d7d0c1;stroke-width:2}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.mono{font-family:'Courier New',monospace;font-weight:900;letter-spacing:.11em}
  </style>
</defs>
<rect width="1180" height="650" rx="38" class="bg"/><rect width="1180" height="650" rx="38" fill="url(#fibres)"/>
<text x="54" y="68" class="mono" font-size="15" fill="#1f6a52">PRACTICE CORRESPONDENCE DESK / DIRECTOR IDV</text>
<text x="54" y="126" class="serif ink" font-size="58">Approved wording, not inbox improvisation.</text>
<g filter="url(#deskShadow)">
  <g transform="translate(72 188) rotate(-2)">
    <rect width="376" height="384" rx="24" class="paper"/>
    <rect x="28" y="28" width="134" height="30" rx="15" class="deep"/><text x="45" y="49" class="mono" font-size="13" fill="#fff">CLIENT LETTER</text>
    <text x="28" y="116" class="serif ink" font-size="35">What directors need to know</text>
    <path d="M30 154h284M30 188h326M30 222h296M30 256h244" class="rule"/>
    <rect x="30" y="304" width="272" height="38" rx="19" class="mint"/><text x="51" y="329" class="sans" font-size="16" fill="#173c32">Boundary note included</text>
  </g>
</g>
<g filter="url(#deskShadow)">
  <g transform="translate(420 166)">
    <rect width="318" height="210" rx="24" class="paper"/>
    <text x="28" y="48" class="mono" font-size="13" fill="#1f6a52">FAQ CARD</text>
    <text x="28" y="92" class="serif ink" font-size="32">Questions staff can answer safely</text>
    <path d="M28 126h250M28 158h214" class="rule"/>
  </g>
</g>
<g filter="url(#deskShadow)">
  <g transform="translate(770 180) rotate(1.4)">
    <rect width="320" height="356" rx="24" class="deep"/>
    <text x="28" y="48" class="mono" font-size="13" fill="#dceadf">READINESS LEDGER</text>
    <rect x="28" y="82" width="256" height="50" rx="13" fill="#fffdf7"/><text x="48" y="114" class="sans" font-size="16" fill="#17231f">Explainer sent</text><text x="244" y="114" class="sans" font-size="16" fill="#1f6a52">42</text>
    <rect x="28" y="150" width="256" height="50" rx="13" fill="#fffdf7"/><text x="48" y="182" class="sans" font-size="16" fill="#17231f">Reminder due</text><text x="244" y="182" class="sans" font-size="16" fill="#b9822e">17</text>
    <rect x="28" y="218" width="256" height="50" rx="13" fill="#fffdf7"/><text x="48" y="250" class="sans" font-size="16" fill="#17231f">Partner review</text><text x="252" y="250" class="sans" font-size="16" fill="#a74739">5</text>
    <path d="M30 304h192" stroke="#dceadf" stroke-opacity=".35" stroke-width="2"/>
  </g>
</g>
<g filter="url(#deskShadow)">
  <g transform="translate(438 420) rotate(-1)">
    <rect width="284" height="116" rx="18" fill="#f6ead0" stroke="#c7bda9"/>
    <text x="24" y="43" class="mono" font-size="12" fill="#8b5a18">CHASE SLIP / 7 DAYS</text>
    <text x="24" y="78" class="sans" font-size="17" fill="#17231f">Polite reminder, dated and logged.</text>
  </g>
</g>
<g transform="translate(918 72) rotate(9)"><circle cx="0" cy="0" r="68" fill="none" stroke="#a74739" stroke-width="5"/><circle cx="0" cy="0" r="48" fill="none" stroke="#a74739" stroke-opacity=".55" stroke-width="2"/><text x="-38" y="-4" class="mono" font-size="13" fill="#a74739">NOT LEGAL</text><text x="-28" y="18" class="mono" font-size="13" fill="#a74739">ADVICE</text></g>
<rect x="72" y="592" width="650" height="34" rx="17" fill="#173c32"/><text x="96" y="614" class="mono" font-size="12" fill="#fff">EVERY CLIENT TOUCHPOINT HAS AN OWNER · A WORDING SOURCE · A NEXT CHASE DATE</text>
</svg>'''
(out / 'idv-correspondence-desk.svg').write_text(correspondence_desk)

for asset in ['idv-comms-workflow.svg', 'idv-deadline-control-room.svg', 'idv-partner-briefing-file.svg', 'idv-correspondence-desk.svg']:
    print(out / asset)

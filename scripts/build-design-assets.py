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

evidence_matrix = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 620" role="img" aria-labelledby="title desc">
<title id="title">Director IDV evidence matrix</title>
<desc id="desc">A compliance evidence matrix connecting director readiness states, approved client wording, chase dates and partner exception notes.</desc>
<defs>
  <filter id="lift" x="-10%" y="-20%" width="125%" height="155%"><feDropShadow dx="0" dy="28" stdDeviation="24" flood-color="#173c32" flood-opacity="0.18"/></filter>
  <pattern id="ticks" width="44" height="44" patternUnits="userSpaceOnUse"><path d="M44 0H0v44" fill="none" stroke="#173c32" stroke-opacity=".05"/></pattern>
  <style>
    .bg{fill:#f6f1e6}.paper{fill:#fffdf7;stroke:#b9c8bf}.deep{fill:#173c32}.green{fill:#1f6a52}.mint{fill:#dceadf}.amber{fill:#dba64c}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.rule{stroke:#d7d0c1;stroke-width:2}.mono{font-family:'Courier New',monospace;font-weight:900;letter-spacing:.1em}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}
  </style>
</defs>
<rect width="1180" height="620" rx="38" class="bg"/><rect width="1180" height="620" rx="38" fill="url(#ticks)"/>
<text x="54" y="66" class="mono" font-size="15" fill="#1f6a52">DIRECTOR IDV / PRACTICE EVIDENCE MATRIX</text>
<text x="54" y="122" class="serif ink" font-size="54">Every director has a status. Every chase has approved wording.</text>
<g filter="url(#lift)">
  <rect x="58" y="170" width="724" height="360" rx="26" class="paper"/>
  <rect x="88" y="202" width="664" height="54" rx="16" class="deep"/>
  <text x="112" y="236" class="mono" font-size="13" fill="#fff">DIRECTOR</text><text x="318" y="236" class="mono" font-size="13" fill="#fff">READINESS</text><text x="514" y="236" class="mono" font-size="13" fill="#fff">NEXT MESSAGE</text>
  <g class="sans" font-size="16">
    <rect x="88" y="278" width="664" height="48" rx="13" fill="#f8f4e9"/><text x="112" y="309" fill="#17231f">A. Patel</text><rect x="312" y="288" width="94" height="28" rx="14" class="green"/><text x="331" y="307" fill="#fff">Briefed</text><text x="512" y="309" fill="#60706a">Send FAQ boundary note</text>
    <rect x="88" y="342" width="664" height="48" rx="13" fill="#eef5ed"/><text x="112" y="373" fill="#17231f">M. Lewis</text><rect x="312" y="352" width="108" height="28" rx="14" class="amber"/><text x="331" y="371" fill="#17231f">Unclear</text><text x="512" y="373" fill="#60706a">Partner exception review</text>
    <rect x="88" y="406" width="664" height="48" rx="13" fill="#f8f4e9"/><text x="112" y="437" fill="#17231f">R. Hughes</text><rect x="312" y="416" width="100" height="28" rx="14" class="red"/><text x="332" y="435" fill="#fff">Silent</text><text x="512" y="437" fill="#60706a">Chase 2 due Friday</text>
    <rect x="88" y="470" width="664" height="48" rx="13" fill="#eef5ed"/><text x="112" y="501" fill="#17231f">S. Khan</text><rect x="312" y="480" width="92" height="28" rx="14" class="green"/><text x="333" y="499" fill="#fff">Ready</text><text x="512" y="501" fill="#60706a">Log complete + archive</text>
  </g>
</g>
<g filter="url(#lift)">
  <rect x="824" y="178" width="292" height="338" rx="26" class="deep"/>
  <text x="854" y="222" class="mono" font-size="13" fill="#dceadf">PARTNER EXCEPTION QUEUE</text>
  <path d="M854 250h214" stroke="#dceadf" stroke-opacity=".28" stroke-width="2"/>
  <g class="sans" font-size="15">
    <rect x="854" y="278" width="224" height="58" rx="14" fill="#fffdf7"/><text x="874" y="302" fill="#17231f">Legal boundary question</text><text x="874" y="323" fill="#60706a">do not answer from inbox</text>
    <rect x="854" y="358" width="224" height="58" rx="14" fill="#fffdf7"/><text x="874" y="382" fill="#17231f">No response after chase</text><text x="874" y="403" fill="#60706a">escalate before deadline</text>
    <rect x="854" y="438" width="224" height="42" rx="21" class="mint"/><text x="880" y="465" fill="#173c32">Weekly partner digest</text>
  </g>
</g>
<path d="M766 352 C 812 304, 838 304, 884 352" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<g transform="translate(936 74) rotate(8)"><rect x="0" y="0" width="154" height="54" rx="8" fill="none" stroke="#a74739" stroke-width="4"/><text x="20" y="34" class="mono" font-size="14" fill="#a74739">DATED TRAIL</text></g>
</svg>'''
(out / 'idv-evidence-matrix.svg').write_text(evidence_matrix)

client_question_queue = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 640" role="img" aria-labelledby="title desc">
<title id="title">Director IDV client question queue</title>
<desc id="desc">A professional compliance communications visual showing director questions triaged into approved answers, partner review and logged follow-up for Companies House ID verification.</desc>
<defs>
  <filter id="lift" x="-10%" y="-18%" width="125%" height="150%"><feDropShadow dx="0" dy="30" stdDeviation="24" flood-color="#173c32" flood-opacity="0.18"/></filter>
  <pattern id="ruled" width="100" height="34" patternUnits="userSpaceOnUse"><path d="M0 33.5H100" stroke="#173c32" stroke-opacity=".055"/></pattern>
  <style>
    .bg{fill:#f3eee2}.paper{fill:#fffdf7;stroke:#c7bda9}.deep{fill:#173c32}.green{fill:#1f6a52}.mint{fill:#dceadf}.amber{fill:#d9a550}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.rule{stroke:#d7d0c1;stroke-width:2}.mono{font-family:'Courier New',monospace;font-weight:900;letter-spacing:.1em}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}
  </style>
</defs>
<rect width="1180" height="640" rx="38" class="bg"/><rect width="1180" height="640" rx="38" fill="url(#ruled)"/>
<text x="54" y="70" class="mono" font-size="15" fill="#1f6a52">DIRECTOR IDV / CLIENT QUESTION QUEUE</text>
<text x="54" y="128" class="serif ink" font-size="58">No staff member should invent the answer twice.</text>
<g filter="url(#lift)">
  <rect x="64" y="180" width="322" height="340" rx="28" class="paper"/>
  <rect x="92" y="212" width="120" height="30" rx="15" class="deep"/><text x="110" y="233" class="mono" font-size="13" fill="#fff">INBOX</text>
  <text x="92" y="292" class="serif ink" font-size="34">Client questions</text>
  <g class="sans" font-size="16">
    <rect x="92" y="326" width="244" height="44" rx="13" fill="#f6ead0"/><text x="112" y="354" fill="#17231f">“Do I need to verify?”</text>
    <rect x="92" y="386" width="244" height="44" rx="13" fill="#eef5ed"/><text x="112" y="414" fill="#17231f">“Can you do it for me?”</text>
    <rect x="92" y="446" width="244" height="44" rx="13" fill="#f0d7d1"/><text x="112" y="474" fill="#17231f">“What if I miss it?”</text>
  </g>
</g>
<path d="M390 350 C 430 298, 466 298, 506 350" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<g filter="url(#lift)">
  <rect x="466" y="158" width="292" height="388" rx="28" class="deep"/>
  <text x="496" y="204" class="mono" font-size="13" fill="#dceadf">TRIAGE RULES</text>
  <text x="496" y="260" class="serif" font-size="34" fill="#fffdf7">Answer from the pack, or escalate.</text>
  <g class="sans" font-size="15">
    <rect x="496" y="304" width="220" height="48" rx="14" class="mint"/><text x="516" y="334" fill="#173c32">Approved explainer</text>
    <rect x="496" y="372" width="220" height="48" rx="14" fill="#f6ead0"/><text x="516" y="402" fill="#173c32">Boundary wording</text>
    <rect x="496" y="440" width="220" height="48" rx="14" fill="#f0d7d1"/><text x="516" y="470" fill="#173c32">Partner exception</text>
  </g>
</g>
<path d="M760 350 C 800 298, 836 298, 876 350" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<g filter="url(#lift)">
  <rect x="830" y="188" width="292" height="332" rx="28" class="paper"/>
  <rect x="858" y="220" width="142" height="30" rx="15" class="green"/><text x="878" y="241" class="mono" font-size="13" fill="#fff">LOGGED REPLY</text>
  <text x="858" y="296" class="serif ink" font-size="32">One calm answer trail</text>
  <path d="M858 330h218M858 362h186M858 394h232" class="rule"/>
  <rect x="858" y="436" width="214" height="44" rx="22" class="mint"/><text x="884" y="464" class="sans" font-size="16" fill="#173c32">Tracker updated</text>
</g>
<g transform="translate(908 86) rotate(7)"><rect width="170" height="56" rx="8" fill="none" stroke="#a74739" stroke-width="4"/><text x="22" y="35" class="mono" font-size="14" fill="#a74739">NO AD-HOC DRIFT</text></g>
<rect x="72" y="574" width="690" height="34" rx="17" fill="#173c32"/><text x="96" y="596" class="mono" font-size="12" fill="#fff">QUESTION CAPTURE → APPROVED ANSWER → ESCALATION IF NEEDED → DATED TRACKER ENTRY</text>
</svg>'''
(out / 'idv-client-question-queue.svg').write_text(client_question_queue)

risk_register = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 650" role="img" aria-labelledby="title desc">
<title id="title">Director IDV rollout risk register</title>
<desc id="desc">A partner-ready risk register for a Companies House ID verification communications rollout, showing routine communications, amber chasers, red silent directors and partner exception decisions.</desc>
<defs>
  <filter id="lift" x="-10%" y="-18%" width="126%" height="150%"><feDropShadow dx="0" dy="30" stdDeviation="24" flood-color="#173c32" flood-opacity="0.18"/></filter>
  <pattern id="papergrid" width="42" height="42" patternUnits="userSpaceOnUse"><path d="M42 0H0v42" fill="none" stroke="#173c32" stroke-opacity=".05"/><circle cx="12" cy="30" r="1.2" fill="#b9822e" fill-opacity=".18"/></pattern>
  <style>
    .bg{fill:#f6f1e6}.sheet{fill:#fffdf7;stroke:#b9c8bf}.deep{fill:#173c32}.green{fill:#1f6a52}.mint{fill:#dceadf}.amber{fill:#d9a550}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.rule{stroke:#d7d0c1;stroke-width:2}.mono{font-family:'Courier New',monospace;font-weight:900;letter-spacing:.1em}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}
  </style>
</defs>
<rect width="1180" height="650" rx="38" class="bg"/><rect width="1180" height="650" rx="38" fill="url(#papergrid)"/>
<text x="54" y="68" class="mono" font-size="15" fill="#1f6a52">COMPANIES HOUSE IDV / PARTNER RISK REGISTER</text>
<text x="54" y="126" class="serif ink" font-size="58">Routine nudges stay routine. Exceptions reach a partner.</text>
<g filter="url(#lift)">
  <rect x="62" y="178" width="758" height="392" rx="28" class="sheet"/>
  <rect x="94" y="214" width="696" height="58" rx="18" class="deep"/>
  <text x="118" y="251" class="mono" font-size="13" fill="#fff">DIRECTOR</text><text x="332" y="251" class="mono" font-size="13" fill="#fff">RISK</text><text x="492" y="251" class="mono" font-size="13" fill="#fff">OWNER / NEXT ACTION</text>
  <g class="sans" font-size="16">
    <rect x="94" y="296" width="696" height="54" rx="14" fill="#f8f4e9"/><text x="118" y="330" fill="#17231f">A. Patel</text><rect x="326" y="308" width="96" height="30" rx="15" class="green"/><text x="348" y="328" fill="#fff">LOW</text><text x="492" y="330" fill="#60706a">Admin team · FAQ link sent</text>
    <rect x="94" y="366" width="696" height="54" rx="14" fill="#eef5ed"/><text x="118" y="400" fill="#17231f">M. Lewis</text><rect x="326" y="378" width="106" height="30" rx="15" class="amber"/><text x="346" y="398" fill="#17231f">AMBER</text><text x="492" y="400" fill="#60706a">Client manager · chase by Friday</text>
    <rect x="94" y="436" width="696" height="54" rx="14" fill="#f8f4e9"/><text x="118" y="470" fill="#17231f">R. Hughes</text><rect x="326" y="448" width="92" height="30" rx="15" class="red"/><text x="350" y="468" fill="#fff">RED</text><text x="492" y="470" fill="#60706a">Partner · silent after second chase</text>
    <rect x="94" y="506" width="696" height="38" rx="19" class="mint"/><text x="118" y="531" fill="#173c32">Weekly digest: 17 routine chasers · 5 partner exceptions · 0 unowned inbox threads</text>
  </g>
</g>
<g filter="url(#lift)">
  <rect x="858" y="208" width="262" height="318" rx="28" class="deep"/>
  <text x="888" y="250" class="mono" font-size="13" fill="#dceadf">EXCEPTION RULES</text>
  <path d="M888 278h190" stroke="#dceadf" stroke-opacity=".3" stroke-width="2"/>
  <g class="sans" font-size="15">
    <rect x="888" y="306" width="194" height="52" rx="14" fill="#fffdf7"/><text x="908" y="338" fill="#17231f">Legal boundary</text>
    <rect x="888" y="376" width="194" height="52" rx="14" fill="#fffdf7"/><text x="908" y="408" fill="#17231f">Deadline silence</text>
    <rect x="888" y="446" width="194" height="44" rx="22" class="mint"/><text x="912" y="474" fill="#173c32">Partner digest</text>
  </g>
</g>
<path d="M804 390 C 846 336, 880 336, 922 390" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<g transform="translate(918 80) rotate(7)"><rect width="164" height="58" rx="8" fill="none" stroke="#a74739" stroke-width="4"/><text x="26" y="36" class="mono" font-size="14" fill="#a74739">NO UNOWNED RISK</text></g>
<rect x="72" y="594" width="690" height="34" rx="17" fill="#173c32"/><text x="96" y="616" class="mono" font-size="12" fill="#fff">STATUS · OWNER · NEXT CHASE DATE · PARTNER EXCEPTION · DATED AUDIT NOTE</text>
</svg>'''
(out / 'idv-risk-register.svg').write_text(risk_register)

appointment_book = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 680" role="img" aria-labelledby="title desc">
<title id="title">Director IDV appointment book</title>
<desc id="desc">A professional practice appointment book showing client segments, approved IDV messages, call slots, partner exceptions and logged follow-up for Companies House identity verification communications.</desc>
<defs>
  <filter id="lift" x="-10%" y="-18%" width="126%" height="150%"><feDropShadow dx="0" dy="34" stdDeviation="26" flood-color="#173c32" flood-opacity="0.20"/></filter>
  <pattern id="linen" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M48 0H0v48" fill="none" stroke="#173c32" stroke-opacity=".045"/><path d="M0 24H48" stroke="#b9822e" stroke-opacity=".055"/></pattern>
  <style>.bg{fill:#f3ecdd}.paper{fill:#fffdf7;stroke:#c7bda9}.deep{fill:#173c32}.green{fill:#1f6a52}.mint{fill:#dceadf}.amber{fill:#d8a24f}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.mono{font-family:'Courier New',monospace;font-weight:900;letter-spacing:.11em}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}</style>
</defs>
<rect width="1240" height="680" rx="40" class="bg"/><rect width="1240" height="680" rx="40" fill="url(#linen)"/>
<text x="58" y="72" class="mono" font-size="15" fill="#1f6a52">DIRECTOR IDV / CLIENT APPOINTMENT BOOK</text><text x="58" y="136" class="serif ink" font-size="60">Turn the rollout into booked client touches, not loose reminders.</text>
<g filter="url(#lift)"><rect x="62" y="198" width="342" height="366" rx="28" class="paper"/><rect x="92" y="230" width="138" height="30" rx="15" class="deep"/><text x="112" y="251" class="mono" font-size="13" fill="#fff">SEGMENT</text><text x="92" y="314" class="serif ink" font-size="35">Who needs what?</text><g class="sans" font-size="16"><rect x="92" y="350" width="260" height="48" rx="14" class="mint"/><text x="114" y="381" fill="#173c32">Ready directors · log proof</text><rect x="92" y="414" width="260" height="48" rx="14" fill="#f6ead0"/><text x="114" y="445" fill="#173c32">Unsure directors · FAQ call</text><rect x="92" y="478" width="260" height="48" rx="14" fill="#f0d7d1"/><text x="114" y="509" fill="#173c32">Silent directors · partner watch</text></g></g>
<path d="M408 386 C 454 324, 496 324, 542 386" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<g filter="url(#lift)"><rect x="500" y="176" width="396" height="422" rx="30" class="deep"/><text x="532" y="224" class="mono" font-size="13" fill="#dceadf">BOOKED COMMUNICATION CADENCE</text><rect x="532" y="258" width="300" height="54" rx="16" fill="#fffdf7"/><text x="554" y="292" class="sans" font-size="17" fill="#17231f">Mon · initial explainer batch</text><rect x="532" y="330" width="300" height="54" rx="16" fill="#fffdf7"/><text x="554" y="364" class="sans" font-size="17" fill="#17231f">Wed · client question office hour</text><rect x="532" y="402" width="300" height="54" rx="16" fill="#fffdf7"/><text x="554" y="436" class="sans" font-size="17" fill="#17231f">Fri · partner exception digest</text><path d="M532 502h292" stroke="#dceadf" stroke-opacity=".32" stroke-width="2"/><text x="532" y="542" class="mono" font-size="12" fill="#dceadf">EVERY TOUCH HAS WORDING · OWNER · STATUS</text></g>
<path d="M900 386 C 948 324, 988 324, 1036 386" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<g filter="url(#lift)"><rect x="944" y="212" width="236" height="332" rx="28" class="paper"/><text x="974" y="256" class="mono" font-size="13" fill="#1f6a52">CALL OUTCOME</text><g class="sans" font-size="15"><circle cx="988" cy="308" r="10" class="green"/><text x="1014" y="313" fill="#17231f">Briefed</text><circle cx="988" cy="362" r="10" class="amber"/><text x="1014" y="367" fill="#17231f">Needs chase</text><circle cx="988" cy="416" r="10" class="red"/><text x="1014" y="421" fill="#17231f">Partner review</text></g><rect x="974" y="466" width="158" height="38" rx="19" class="mint"/><text x="998" y="491" class="sans" font-size="15" fill="#173c32">Tracker updated</text></g>
<g transform="translate(948 84) rotate(7)"><rect width="184" height="58" rx="8" fill="none" stroke="#a74739" stroke-width="4"/><text x="26" y="36" class="mono" font-size="14" fill="#a74739">NO LOST CLIENTS</text></g><rect x="74" y="610" width="778" height="34" rx="17" fill="#173c32"/><text x="98" y="632" class="mono" font-size="12" fill="#fff">CLIENT SEGMENT → BOOKED TOUCHPOINT → APPROVED WORDING → LOGGED OUTCOME → PARTNER EXCEPTION</text>
</svg>'''
(out / 'idv-appointment-book.svg').write_text(appointment_book)

launch_docket = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 700" role="img" aria-labelledby="title desc">
<title id="title">Director IDV launch docket</title>
<desc id="desc">A professional client communications launch docket showing partner sign-off, send groups, approved email copy, reminders and evidence logging for Companies House ID verification.</desc>
<defs>
  <filter id="lift" x="-10%" y="-18%" width="126%" height="150%"><feDropShadow dx="0" dy="34" stdDeviation="28" flood-color="#173c32" flood-opacity="0.20"/></filter>
  <pattern id="grain" width="52" height="52" patternUnits="userSpaceOnUse"><path d="M52 0H0v52" fill="none" stroke="#173c32" stroke-opacity=".045"/><circle cx="14" cy="34" r="1.3" fill="#b9822e" fill-opacity=".18"/></pattern>
  <style>.bg{fill:#f5efe2}.paper{fill:#fffdf7;stroke:#c7bda9}.deep{fill:#173c32}.green{fill:#1f6a52}.mint{fill:#dceadf}.amber{fill:#d8a24f}.red{fill:#a74739}.ink{fill:#17231f}.muted{fill:#60706a}.rule{stroke:#d7d0c1;stroke-width:2}.mono{font-family:'Courier New',monospace;font-weight:900;letter-spacing:.11em}.sans{font-family:Aptos,'Segoe UI',sans-serif;font-weight:800}.serif{font-family:Georgia,'Times New Roman',serif;font-weight:700}</style>
</defs>
<rect width="1240" height="700" rx="40" class="bg"/><rect width="1240" height="700" rx="40" fill="url(#grain)"/>
<text x="58" y="74" class="mono" font-size="15" fill="#1f6a52">DIRECTOR IDV / CLIENT SEND DOCKET</text><text x="58" y="138" class="serif ink" font-size="60">A first-send file the whole practice can trust.</text>
<g filter="url(#lift)"><rect x="64" y="196" width="332" height="388" rx="28" class="paper"/><rect x="94" y="230" width="152" height="30" rx="15" class="deep"/><text x="112" y="251" class="mono" font-size="13" fill="#fff">SIGN-OFF</text><text x="94" y="316" class="serif ink" font-size="35">Partner-approved launch note</text><path d="M96 358h242M96 390h206M96 422h228" class="rule"/><rect x="96" y="486" width="208" height="44" rx="22" class="mint"/><text x="122" y="514" class="sans" font-size="16" fill="#173c32">Scope + caveats logged</text></g>
<g filter="url(#lift)"><rect x="440" y="172" width="360" height="438" rx="30" class="deep"/><text x="474" y="222" class="mono" font-size="13" fill="#dceadf">SEND GROUPS</text><text x="474" y="282" class="serif" font-size="35" fill="#fffdf7">Who receives which wording?</text><g class="sans" font-size="16"><rect x="474" y="324" width="270" height="54" rx="15" fill="#fffdf7"/><text x="496" y="358" fill="#17231f">Directors · explainer + FAQ</text><rect x="474" y="398" width="270" height="54" rx="15" fill="#fffdf7"/><text x="496" y="432" fill="#17231f">PSCs · boundary note</text><rect x="474" y="472" width="270" height="54" rx="15" fill="#fffdf7"/><text x="496" y="506" fill="#17231f">Silent clients · chase sequence</text></g><path d="M474 558h238" stroke="#dceadf" stroke-opacity=".32" stroke-width="2"/></g>
<g filter="url(#lift)"><rect x="844" y="210" width="328" height="356" rx="28" class="paper"/><rect x="874" y="242" width="162" height="30" rx="15" class="green"/><text x="894" y="263" class="mono" font-size="13" fill="#fff">EVIDENCE LOG</text><text x="874" y="326" class="serif ink" font-size="34">Every send returns to the tracker</text><g class="sans" font-size="15"><circle cx="892" cy="376" r="10" class="green"/><text x="918" y="381" fill="#17231f">Message version recorded</text><circle cx="892" cy="430" r="10" class="amber"/><text x="918" y="435" fill="#17231f">Reminder date assigned</text><circle cx="892" cy="484" r="10" class="red"/><text x="918" y="489" fill="#17231f">Exception owner named</text></g></g>
<path d="M398 386 C 438 326, 482 326, 522 386" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/><path d="M800 386 C 842 326, 884 326, 926 386" stroke="#1f6a52" stroke-width="4" stroke-dasharray="10 9" fill="none"/>
<g transform="translate(958 82) rotate(7)"><rect width="178" height="58" rx="8" fill="none" stroke="#a74739" stroke-width="4"/><text x="24" y="36" class="mono" font-size="14" fill="#a74739">FIRST SEND READY</text></g><rect x="74" y="628" width="828" height="34" rx="17" fill="#173c32"/><text x="98" y="650" class="mono" font-size="12" fill="#fff">PARTNER APPROVAL → SEND GROUPS → APPROVED COPY → REMINDER CADENCE → DATED EVIDENCE LOG</text>
</svg>'''
(out / 'idv-launch-docket.svg').write_text(launch_docket)

for asset in ['idv-comms-workflow.svg', 'idv-deadline-control-room.svg', 'idv-partner-briefing-file.svg', 'idv-correspondence-desk.svg', 'idv-evidence-matrix.svg', 'idv-client-question-queue.svg', 'idv-risk-register.svg', 'idv-appointment-book.svg', 'idv-launch-docket.svg']:
    print(out / asset)

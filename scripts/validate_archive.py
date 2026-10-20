from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
required=['identity/profile.md','workflow/ai-rules.md','workflow/preferences.md','memory/lessons.md','memory/decisions.md','skills/capabilities.md','archive/projects.md','ai-integration.md']
errors=[]
for name in required:
 if not (root/name).is_file(): errors.append('missing: '+name)
patterns=[r'gh[pousr]_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{40,}',r'sk-[A-Za-z0-9_-]{35,}',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----']
for p in root.rglob('*'):
 if not p.is_file() or '.git' in p.parts: continue
 if p.name.startswith('.env') or p.suffix in ('.pem','.key'): errors.append('credential filename: '+str(p.relative_to(root)))
 if p.suffix in ('.md','.py','.yml','.json'):
  text=p.read_text(encoding='utf-8-sig')
  if p.suffix=='.md':
   body=text.split('---',2)[-1].lstrip() if text.startswith('---\n') else text.lstrip()
   if not body.startswith(('# AI-READONLY:','# AI-EDITABLE:')): errors.append('missing AI marker: '+str(p.relative_to(root)))
  if any(re.search(x,text) for x in patterns): errors.append('possible credential: '+str(p.relative_to(root)))
if errors: raise SystemExit('\n'.join(errors))
print('PASS: required files, UTF-8, AI markers, credential-pattern checks')

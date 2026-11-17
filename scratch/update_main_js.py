with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update roleSwitch block
old_role_block = """const roleSwitch=document.querySelector('.role-switch');
if(roleSwitch){
  const roleInput=document.querySelector('input[name="role"]');
  const isReg=document.querySelector('form[data-form]')?.dataset.form==='register';
  const copy={
    client:isReg?'Get a live dashboard for your campaigns.':'Log in to see your campaign results.',
    admin:isReg?'Set up an admin account to manage clients and campaigns.':'Log in to manage client accounts and campaigns.'
  };
  const setRole=r=>{roleSwitch.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.role===r));if(roleInput)roleInput.value=r;const s=document.getElementById('authSub');if(s)s.textContent=copy[r]};
  roleSwitch.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>setRole(b.dataset.role)));
  const rp=new URLSearchParams(location.search).get('role');
  setRole(rp==='admin'?'admin':'client');
}"""

new_role_block = """const roleSwitch=document.querySelector('.role-switch');
if(roleSwitch){
  const roleInput=document.querySelector('input[name="role"]');
  const isReg=document.querySelector('form[data-form]')?.dataset.form==='register';
  const copy={
    client:isReg?'Get a live dashboard for your campaigns.':'Log in to see your campaign results, qualified leads, and ROI.',
    admin:isReg?'Set up an admin account to manage clients and campaigns.':'Log in to manage 38 client brands, specialist pods, and ad spend.'
  };
  const setRole=r=>{
    roleSwitch.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.role===r));
    if(roleInput)roleInput.value=r;
    const s=document.getElementById('authSub');if(s)s.textContent=copy[r];
    const t=document.getElementById('authTitle');
    if(t && !isReg) t.textContent = r === 'admin' ? 'Agency Admin Login' : 'Client Partner Login';
    const em=document.getElementById('email');
    if(em && !em.value) em.placeholder = r === 'admin' ? 'admin@stackly.agency' : 'rhea@voltrix.io';
  };
  roleSwitch.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>setRole(b.dataset.role)));
  const rp=new URLSearchParams(location.search).get('role');
  setRole(rp==='admin'?'admin':'client');

  const fillClient=document.getElementById('fillClientDemo');
  const fillAdmin=document.getElementById('fillAdminDemo');
  const emailInput=document.getElementById('email');
  const passInput=document.getElementById('password');

  if(fillClient){
    fillClient.addEventListener('click',e=>{
      e.preventDefault();
      setRole('client');
      if(emailInput) emailInput.value='rhea@voltrix.io';
      if(passInput) passInput.value='password123';
      const f=fillClient.closest('form');
      if(f) msg(f,'Client Partner credentials loaded (Rhea Nair / Voltrix). Click Log in to proceed.',true);
    });
  }
  if(fillAdmin){
    fillAdmin.addEventListener('click',e=>{
      e.preventDefault();
      setRole('admin');
      if(emailInput) emailInput.value='alex@stackly.agency';
      if(passInput) passInput.value='password123';
      const f=fillAdmin.closest('form');
      if(f) msg(f,'Agency Administrator credentials loaded (Alex Vance / Director). Click Log in to proceed.',true);
    });
  }
}"""

# 2. Update login block
old_login_block = """  if(k=='login'){
    const users=JSON.parse(localStorage.getItem('stackly_users')||'[]');
    const u=users.find(x=>x.email.toLowerCase()===d.email.toLowerCase());
    const role=d.role||'client';
    if(u&&u.password!==d.password)return msg(f,'Incorrect password. Please try again.',false);
    if(u&&u.role!==role)return msg(f,'This email is registered as '+u.role+'. Select '+u.role+' to continue.',false);
    localStorage.setItem('stackly_user',JSON.stringify({name:u?u.name:d.email.split('@')[0],email:d.email,role:u?u.role:role}));
    location.href='dashboard.html';
  }"""

new_login_block = """  if(k=='login'){
    const users=JSON.parse(localStorage.getItem('stackly_users')||'[]');
    const u=users.find(x=>x.email.toLowerCase()===d.email.toLowerCase());
    const role=d.role||'client';
    if(u&&u.password!==d.password)return msg(f,'Incorrect password. Please try again.',false);
    if(u&&u.role!==role)return msg(f,'This email is registered as '+u.role+'. Select '+u.role+' to continue.',false);
    const displayName = u ? u.name : (role === 'admin' ? 'Alex Vance' : (d.email.split('@')[0] || 'Rhea Nair'));
    localStorage.setItem('stackly_user',JSON.stringify({name:displayName,email:d.email,role:role}));
    location.href='dashboard.html?role='+role;
  }"""

code = code.replace(old_role_block.replace('\r\n', '\n'), new_role_block.replace('\r\n', '\n'))
code = code.replace(old_login_block.replace('\r\n', '\n'), new_login_block.replace('\r\n', '\n'))

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated main.js successfully!")

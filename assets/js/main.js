const IMG=(id,w=1200)=>`images/photo-${id.replace(/^photo-/, '')}.webp`;
const user=()=>{try{return JSON.parse(localStorage.getItem('stackly_user'))}catch(e){return null}};
const DEMO_NAMES={'rhea@voltrix.io':'Rhea Nair','alex@stackly.agency':'Alex Vance'};
const nameFromEmail=email=>DEMO_NAMES[(email||'').trim().toLowerCase()]||'';
const legacyNameFromEmail=email=>{
  const local=((email||'').trim().toLowerCase().split('@')[0]||'').replace(/[._-]+/g,' ').trim();
  return local.replace(/\b[a-z]/g,c=>c.toUpperCase());
};
const page=location.pathname.split('/').pop().replace('.html','')||'index';
const pages=[['index','Home'],['about','About'],['features','Features'],['blog','Blog'],['contact','Contact']];
function buildNav(){
  const nav=document.getElementById('nav');if(!nav)return;
  const auth=`<a href="login.html" class="btn btn-ghost btn-sm ms-lg-2 mt-2 mt-lg-0">Log in</a><a href="register.html" class="btn btn-pink btn-sm ms-lg-2 mt-2 mt-lg-0">Register</a>`;
  nav.innerHTML=`<nav class="navbar navbar-expand-lg site-nav"><div class="container">
  <a class="brand" href="index.html"><img class="brand-logo" src="logo_green.webp?v=30" alt="Stackly"></a>
  <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#m" aria-label="Menu"><i class="bi bi-list"></i></button>
  <div class="collapse navbar-collapse" id="m"><ul class="navbar-nav mx-auto align-items-lg-center">
  ${pages.map(p=>`<li class="nav-item"><a class="nav-link ${p[0]==page?'active':''}" href="${p[0]}.html">${p[1]}</a></li>`).join('')}
  </ul><div class="nav-auth d-flex flex-wrap align-items-lg-center ms-lg-auto">${auth}</div></div></div></nav>`;
  const lo=document.getElementById('logout');if(lo)lo.onclick=()=>{localStorage.removeItem('stackly_user');location.href='login.html'};
  const n=document.querySelector('.site-nav'),t=()=>n.classList.toggle('scrolled',scrollY>40);t();addEventListener('scroll',t,{passive:true});
  const col=document.getElementById('m');
  if(col){
    const lock=v=>{document.body.classList.toggle('menu-open',v);document.documentElement.classList.toggle('menu-open',v)};
    col.addEventListener('show.bs.collapse',()=>{if(innerWidth<992)lock(true)});
    col.addEventListener('hidden.bs.collapse',()=>lock(false));
    col.querySelectorAll('.nav-link,.btn').forEach(a=>a.addEventListener('click',()=>{if(innerWidth<992)bootstrap.Collapse.getOrCreateInstance(col).hide()}));
    addEventListener('resize',()=>{if(innerWidth>=992)lock(false)});
  }
}
function buildFoot(){
  const f=document.getElementById('foot');if(!f)return;
  f.innerHTML=`<footer class="foot"><div class="container"><div class="row g-5">
  <div class="col-lg-4"><div class="brand mb-3"><a href="index.html" class="d-inline-block"><img class="brand-logo" src="logo_green.webp?v=30" alt="Stackly"></a></div><p>A digital marketing agency for SEO, paid media, social and analytics, with reporting tied to revenue.</p>
  <div class="soc"><a href="404.html" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a><a href="404.html" aria-label="Instagram"><i class="bi bi-instagram"></i></a><a href="404.html" aria-label="X"><i class="bi bi-twitter-x"></i></a><a href="404.html" aria-label="YouTube"><i class="bi bi-youtube"></i></a></div></div>
  <div class="col-6 col-lg-2 foot-col"><div class="foot-col-inner"><h5>Company</h5>${pages.map(p=>`<a href="${p[0]}.html">${p[1]}</a>`).join('')}</div></div>
  <div class="col-6 col-lg-2 foot-col"><div class="foot-col-inner"><h5>Services</h5><a href="404.html">SEO</a><a href="404.html">Paid media</a><a href="404.html">Social media</a><a href="404.html">Analytics</a><a href="404.html">Email marketing</a></div></div>
  <div class="col-lg-4"><h5>Get one growth tip a week</h5><form class="d-flex gap-2 news"><input class="form-control" type="email" required placeholder="you@company.com" aria-label="Email"><button class="btn btn-pink">Subscribe</button></form><small class="d-block mt-2 news-msg"></small></div>
  </div><hr class="my-4 border-secondary"><small>&copy; 2026 Stackly Digital. All rights reserved.</small></div></footer>`;
  f.querySelector('.news').onsubmit=e=>{e.preventDefault();location.href='404.html'};
}
document.querySelectorAll('[data-img]').forEach(i=>{
  if(!i.getAttribute('src')) i.src=IMG(i.dataset.img,+i.dataset.w||900);
  i.loading=i.classList.contains('eager')?'eager':'lazy';
});
document.querySelectorAll('img').forEach(i=>{
  i.addEventListener('error',function(){
    const s=this.getAttribute('src')||'';
    if(s.includes('/photo-')){
      this.src=s.replace('/photo-','/');
    } else if(s.includes('images/')&&!s.includes('/photo-')){
      this.src=s.replace('images/','images/photo-');
    }
  });
});
buildNav();buildFoot();
const blogChips=[...document.querySelectorAll('.chip-f')];
if(blogChips.length){
  const cards=[...document.querySelectorAll('.row[data-stagger] > div')],feat=document.querySelector('.feat-post');
  const filter=cat=>{blogChips.forEach(c=>c.classList.toggle('on',c.textContent.trim()===cat));cards.forEach(c=>{const t=(c.querySelector('.tag')?.textContent||'').trim();c.style.display=(cat==='All'||t===cat)?'':'none'});if(feat)feat.style.display=cat==='All'?'':'none'};
  blogChips.forEach(c=>c.addEventListener('click',e=>{e.preventDefault();filter(c.textContent.trim())}));
  filter('All');
}
const roleSwitch=document.querySelector('.role-switch');
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


}
const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
const runCount=c=>{const end=+c.dataset.count,s=c.dataset.suffix||'',pre=c.dataset.prefix||'',dec=+c.dataset.dec||0,fmt=v=>pre+v.toLocaleString(undefined,{minimumFractionDigits:dec,maximumFractionDigits:dec})+s;if(reduceMotion){c.textContent=fmt(end);return}const o={v:0};gsap.to(o,{v:end,duration:1.6,ease:'power2.out',onUpdate:()=>c.textContent=fmt(o.v)})};
const dashTabs=[...document.querySelectorAll('.side a[data-nav]')];
const showTab=(id,scroll)=>{
  const sec=document.getElementById(id);
  if(!sec)return;
  const parentDash=sec.closest('.dash-mode')||document;
  parentDash.querySelectorAll('.dash-sec').forEach(s=>s.classList.toggle('on',s.id===id));
  parentDash.querySelectorAll('.side a[data-nav]').forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+id));
  sec.querySelectorAll('[data-count]').forEach(runCount);
  if(scroll)window.scrollTo({top:0,behavior:reduceMotion?'auto':'smooth'});
};
if(dashTabs.length){
  dashTabs.forEach(a=>a.addEventListener('click',e=>{e.preventDefault();showTab(a.getAttribute('href').slice(1),true)}));
}
gsap.registerPlugin(ScrollTrigger);
const mm=gsap.matchMedia();
mm.add('(prefers-reduced-motion: no-preference)',()=>{
  if(document.querySelector('.hero')){
    const tl=gsap.timeline({defaults:{ease:'power4.out'}});
    tl.from('.site-nav',{y:-80,opacity:0,duration:.8})
      .from('.hero h1 span b',{yPercent:115,duration:1.1,stagger:.14,onComplete:()=>{gsap.set('.hero h1 span, .page-hero h1 span',{overflow:'visible',paddingRight:0})}},.1)
      .from('.hero .fade',{y:30,opacity:0,duration:.8,stagger:.1},.7)
      .from('.chart-card',{y:60,opacity:0,rotate:2,duration:1.2},.4);
    const a=document.querySelector('.hero .area');if(a)tl.from(a,{opacity:0,duration:1.2},1.6);
    tl.from('.chip',{scale:.6,opacity:0,duration:.7,stagger:.25,ease:'back.out(2)'},1.9);
    gsap.to('.chip.a',{y:-10,repeat:-1,yoyo:true,duration:2.2,ease:'sine.inOut'});
    gsap.to('.chip.b',{y:10,repeat:-1,yoyo:true,duration:2.6,ease:'sine.inOut'});
  }
  document.querySelectorAll('.draw').forEach(p=>{const L=p.getTotalLength();gsap.fromTo(p,{strokeDasharray:L,strokeDashoffset:L},{strokeDashoffset:0,duration:2.2,ease:'power2.inOut',delay:.5,scrollTrigger:{trigger:p,start:'top 95%',once:true}})});
  const mt=document.querySelector('.m-track');if(mt&&window.matchMedia('(min-width:768px)').matches){mt.innerHTML+=mt.innerHTML;gsap.to(mt,{xPercent:-50,duration:30,ease:'none',repeat:-1})}
  gsap.utils.toArray('[data-stagger]').forEach(g=>gsap.from(g.children,{y:60,opacity:0,duration:.9,stagger:.12,ease:'power3.out',scrollTrigger:{trigger:g,start:'top 85%'}}));
  gsap.utils.toArray('[data-reveal]').forEach(e=>gsap.from(e,{y:40,opacity:0,duration:1,ease:'power3.out',scrollTrigger:{trigger:e,start:'top 88%'}}));
  gsap.utils.toArray('.parallax img').forEach(i=>gsap.to(i,{yPercent:-14,ease:'none',scrollTrigger:{trigger:i.parentElement,scrub:true}}));
  gsap.utils.toArray('[data-count]').filter(c=>!c.closest('.dash-sec')).forEach(c=>{const o={v:0},end=+c.dataset.count,s=c.dataset.suffix||'',pre=c.dataset.prefix||'',dec=+c.dataset.dec||0;gsap.to(o,{v:end,duration:2,ease:'power2.out',scrollTrigger:{trigger:c,start:'top 92%',once:true},onUpdate:()=>c.textContent=pre+o.v.toLocaleString(undefined,{minimumFractionDigits:dec,maximumFractionDigits:dec})+s})});
  gsap.utils.toArray('.step').forEach(s=>gsap.from(s,{x:-30,opacity:0,duration:.8,scrollTrigger:{trigger:s,start:'top 88%'}}));
  gsap.utils.toArray('.prog div').forEach(b=>gsap.from(b,{scaleX:0,duration:1.2,ease:'power3.out',scrollTrigger:{trigger:b,start:'top 95%'}}));
  gsap.from('.auth-form form > *',{y:24,opacity:0,stagger:.08,duration:.7,delay:.2});
  gsap.from('.dash-main .kpi',{y:30,opacity:0,stagger:.1,duration:.7,delay:.2});
});
const msg=(f,t,ok=true)=>{let m=f.querySelector('.fm');if(!m){m=document.createElement('div');f.appendChild(m)}m.className='fm mt-3 small fw-bold '+(ok?'text-success':'text-danger');m.textContent=t};
const ALPHA=/^[A-Za-z\s'.-]+$/;
document.querySelectorAll('[data-alpha]').forEach(i=>i.addEventListener('input',()=>{const v=i.value.replace(/[^A-Za-z\s'.-]/g,'');if(v!==i.value)i.value=v}));
const EMAIL_COM=/^[^\s@]+@[^\s@]+\.com$/i;
document.querySelectorAll('input[type="email"]').forEach(i=>i.addEventListener('input',()=>i.setCustomValidity(EMAIL_COM.test(i.value.trim())?'':'Email must end with .com')));
document.addEventListener('submit',e=>{
  const em=e.target.querySelector?e.target.querySelector('input[type="email"]'):null;
  if(em&&!EMAIL_COM.test(em.value.trim())){
    em.setCustomValidity('Email must end with .com');em.reportValidity();
    e.preventDefault();e.stopPropagation();
  }
},true);
document.querySelectorAll('form[data-form]').forEach(f=>f.addEventListener('submit',e=>{
  e.preventDefault();const k=f.dataset.form,d=Object.fromEntries(new FormData(f));
  const alpha=f.querySelector('[data-alpha]');
  if(alpha&&!ALPHA.test(alpha.value.trim()))return msg(f,'Name must contain letters only, no numbers.',false);
  if((k=='login'||k=='register')&&(!d.password||d.password.length<6))return msg(f,'Password must be at least 6 characters.',false);
  if(k=='contact'){location.href='404.html';return}
  if(k=='login'){
    const users=JSON.parse(localStorage.getItem('stackly_users')||'[]');
    const u=users.find(x=>x.email.toLowerCase()===d.email.toLowerCase());
    const role=d.role||'client';
    if(u&&u.password!==d.password)return msg(f,'Incorrect password. Please try again.',false);
    if(u&&u.role!==role)return msg(f,'This email is registered as '+u.role+'. Select '+u.role+' to continue.',false);
    const displayName = (u && u.name && String(u.name).trim()) ? u.name : (nameFromEmail(d.email) || d.email);
    localStorage.setItem('stackly_user',JSON.stringify({name:displayName,email:d.email,role:role}));
    location.href='dashboard.html?role='+role;
  }
  if(k=='register'){
    if(d.password!==d.confirm)return msg(f,'Passwords do not match. Re-enter both fields.',false);
    const users=JSON.parse(localStorage.getItem('stackly_users')||'[]');
    if(users.some(x=>x.email.toLowerCase()===d.email.toLowerCase()))return msg(f,'An account with this email already exists. Please log in.',false);
    users.push({name:d.name,email:d.email,password:d.password,role:d.role||'client'});
    localStorage.setItem('stackly_users',JSON.stringify(users));
    location.href='login.html?role='+(d.role||'client');
  }
}));
if(page=='dashboard'){
  let u=user();
  const qRole=new URLSearchParams(location.search).get('role');
  let currentRole=(qRole==='admin'||qRole==='client')?qRole:(u&&u.role?u.role:'client');

  if(!u){
    u={name:currentRole==='admin'?'Alex Vance':'Rhea Nair',email:currentRole==='admin'?'alex@stackly.agency':'rhea@voltrix.io',role:currentRole};
    localStorage.setItem('stackly_user',JSON.stringify(u));
  }
  if(!u.email) u.email = currentRole==='admin' ? 'alex@stackly.agency' : 'rhea@voltrix.io';
  if(!u.name || !String(u.name).trim()) u.name = nameFromEmail(u.email) || u.email;
  try {
    const regs=JSON.parse(localStorage.getItem('stackly_users')||'[]');
    const reg=regs.find(x=>x.email&&u.email&&x.email.toLowerCase()===u.email.toLowerCase());
    if(reg&&reg.name&&String(reg.name).trim()) u.name=reg.name;
    else if(u.name===legacyNameFromEmail(u.email)) u.name=nameFromEmail(u.email)||u.email;
  } catch(e) {}
  localStorage.setItem('stackly_user',JSON.stringify(u));

  const setDashboardRole = role => {
    currentRole = role;
    u.role = role;
    if(role === 'client' && (!u.name || u.name === 'Alex Vance')) u.name = 'Rhea Nair';
    if(role === 'admin' && (!u.name || u.name === 'Rhea Nair')) u.name = 'Alex Vance';
    localStorage.setItem('stackly_user', JSON.stringify(u));

    document.querySelectorAll('.uname').forEach(e => e.textContent = u.name);
    document.querySelectorAll('.uemail').forEach(e => e.textContent = u.email);
    document.querySelectorAll('.urole').forEach(e => e.textContent = role === 'admin' ? 'Super Admin / Director' : 'Client Partner');

    const clientDash = document.getElementById('clientDash');
    const adminDash = document.getElementById('adminDash');
    const roleBtnClient = document.getElementById('roleBtnClient');
    const roleBtnAdmin = document.getElementById('roleBtnAdmin');

    if (role === 'admin') {
      if (clientDash) {
        clientDash.classList.add('d-none');
        clientDash.style.setProperty('display', 'none', 'important');
      }
      if (adminDash) {
        adminDash.classList.remove('d-none');
        adminDash.style.removeProperty('display');
      }
      if (roleBtnClient) roleBtnClient.classList.remove('on');
      if (roleBtnAdmin) roleBtnAdmin.classList.add('on');
      document.body.classList.remove('cp-theme');
      showAdmTab('adm-overview');
    } else {
      if (adminDash) {
        adminDash.classList.add('d-none');
        adminDash.style.setProperty('display', 'none', 'important');
      }
      if (clientDash) {
        clientDash.classList.remove('d-none');
        clientDash.style.removeProperty('display');
      }
      if (roleBtnAdmin) roleBtnAdmin.classList.remove('on');
      if (roleBtnClient) roleBtnClient.classList.add('on');
      document.body.classList.add('cp-theme');
      showCpTab('cp-overview');
    }
  };

  // 1. Client Portal tab switching
  const showCpTab = id => {
    document.querySelectorAll('.cp-sec').forEach(s => s.classList.remove('on'));
    const target = document.getElementById(id);
    if(target) target.classList.add('on');
    document.querySelectorAll('.cp-tab[data-cpnav]').forEach(t => t.classList.toggle('on', t.dataset.cpnav === id));
    // Also sync drawer items
    document.querySelectorAll('.dash-drawer-item[data-cpnav]').forEach(t => t.classList.toggle('on', t.dataset.cpnav === id));
    if(target) target.querySelectorAll('[data-count]').forEach(runCount);
  };
  document.querySelectorAll('.cp-tab[data-cpnav]').forEach(tab => {
    tab.addEventListener('click', () => showCpTab(tab.dataset.cpnav));
  });

  // Client Portal pill tabs
  document.querySelectorAll('.cp-pill-tabs').forEach(group => {
    group.querySelectorAll('.cp-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        group.querySelectorAll('.cp-pill').forEach(p => p.classList.remove('on'));
        pill.classList.add('on');
      });
    });
  });

  // 2. Admin Suite Tab Switching
  window.showAdmTab = id => {
    document.querySelectorAll('.adm-sec').forEach(s => s.classList.remove('on'));
    const target = document.getElementById(id);
    if(target) target.classList.add('on');
    document.querySelectorAll('.adm-tab[data-admnav]').forEach(t => t.classList.toggle('on', t.dataset.admnav === id));
    // Also sync drawer items
    document.querySelectorAll('.dash-drawer-item[data-admnav]').forEach(t => t.classList.toggle('on', t.dataset.admnav === id));
    if(target) target.querySelectorAll('[data-count]').forEach(runCount);
  };
  document.querySelectorAll('.adm-tab[data-admnav]').forEach(tab => {
    tab.addEventListener('click', () => showAdmTab(tab.dataset.admnav));
  });

  // Admin Pill tabs inside cards
  document.querySelectorAll('.adm-pill-group').forEach(group => {
    group.querySelectorAll('.adm-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        group.querySelectorAll('.adm-pill').forEach(p => p.classList.remove('on'));
        pill.classList.add('on');
      });
    });
  });

  // 3. Admin Client Search & Category Filter
  const clientSearch = document.getElementById('admClientSearch');
  if (clientSearch) {
    clientSearch.addEventListener('input', e => {
      const q = e.target.value.toLowerCase().trim();
      document.querySelectorAll('#admClientTable tbody tr').forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(q) ? '' : 'none';
      });
    });
  }

  const clientFilters = document.getElementById('admClientFilters');
  if (clientFilters) {
    clientFilters.querySelectorAll('button[data-filter]').forEach(btn => {
      btn.addEventListener('click', () => {
        clientFilters.querySelectorAll('button').forEach(b => {
          b.className = 'btn btn-sm btn-outline-secondary';
        });
        btn.className = 'btn btn-sm btn-cobalt';
        const f = btn.dataset.filter;
        document.querySelectorAll('#admClientTable tbody tr').forEach(row => {
          if (f === 'all') {
            row.style.display = '';
          } else {
            row.style.display = row.dataset.cat === f ? '' : 'none';
          }
        });
      });
    });
  }

  // 4. Growth Simulator Logic
  const calcBrands = document.getElementById('calcBrands');
  const calcSpend = document.getElementById('calcSpend');
  if (calcBrands && calcSpend) {
    const updateSim = () => {
      const b = +calcBrands.value;
      const s = +calcSpend.value;
      document.getElementById('calcBrandsVal').textContent = b + ' Brands';
      document.getElementById('calcSpendVal').textContent = '$' + s.toLocaleString();

      const mrr = Math.round(b * (s * 0.15 + 2400));
      const totalSpend = b * s;
      const pods = Math.max(1, Math.ceil(b / 9));
      const leads = Math.round(b * (s / 75));

      document.getElementById('resMRR').textContent = '$' + mrr.toLocaleString();
      document.getElementById('resSpend').textContent = '$' + totalSpend.toLocaleString();
      document.getElementById('resPods').textContent = pods + ' Pods';
      document.getElementById('resLeads').textContent = leads.toLocaleString() + '/mo';
    };
    calcBrands.addEventListener('input', updateSim);
    calcSpend.addEventListener('input', updateSim);
    updateSim();
  }

  // Bind Role Switcher Buttons in Top Header
  window.setDashboardRole = setDashboardRole;
  document.querySelectorAll('[data-dashboard-role]').forEach(btn => {
    btn.addEventListener('click', () => setDashboardRole(btn.dataset.dashboardRole));
  });

  // ================================================================
  // MOBILE DRAWER — Hamburger menu (full-screen overlay like site nav)
  // ================================================================
  const drawer = document.getElementById('dashDrawer');
  const drawerBackdrop = document.getElementById('dashDrawerBackdrop');
  const burger = document.getElementById('dashBurger');
  const drawerClose = document.getElementById('dashDrawerClose');

  const openDrawer = () => {
    if(!drawer) return;
    drawer.classList.add('open');
    drawerBackdrop.classList.add('open');
    document.documentElement.classList.add('dash-drawer-lock');
    document.body.classList.add('dash-drawer-lock');
    drawer.setAttribute('aria-hidden', 'false');
  };
  const closeDrawer = () => {
    if(!drawer) return;
    drawer.classList.remove('open');
    drawerBackdrop.classList.remove('open');
    document.documentElement.classList.remove('dash-drawer-lock');
    document.body.classList.remove('dash-drawer-lock');
    drawer.setAttribute('aria-hidden', 'true');
  };

  if(burger) burger.addEventListener('click', openDrawer);
  if(drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if(drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

  // Close drawer on Escape key
  document.addEventListener('keydown', e => { if(e.key === 'Escape') closeDrawer(); });

  // Close drawer on resize to desktop
  window.addEventListener('resize', () => { if(window.innerWidth >= 992) closeDrawer(); });

  // Drawer: show correct nav based on current role
  const syncDrawerRole = role => {
    const clientNav = document.getElementById('drawerClientNav');
    const adminNav = document.getElementById('drawerAdminNav');
    const dBtnClient = document.getElementById('drawerBtnClient');
    const dBtnAdmin = document.getElementById('drawerBtnAdmin');
    if(clientNav) clientNav.classList.toggle('d-none', role === 'admin');
    if(adminNav) adminNav.classList.toggle('d-none', role !== 'admin');
    if(dBtnClient) dBtnClient.classList.toggle('on', role !== 'admin');
    if(dBtnAdmin) dBtnAdmin.classList.toggle('on', role === 'admin');
  };

  // Drawer client nav items
  document.querySelectorAll('.dash-drawer-item[data-cpnav]').forEach(item => {
    item.addEventListener('click', () => {
      showCpTab(item.dataset.cpnav);
      closeDrawer();
    });
  });

  // Drawer admin nav items
  document.querySelectorAll('.dash-drawer-item[data-admnav]').forEach(item => {
    item.addEventListener('click', () => {
      showAdmTab(item.dataset.admnav);
      closeDrawer();
    });
  });

  // Drawer role buttons
  document.querySelectorAll('.drawer-role-btn[data-dashboard-role]').forEach(btn => {
    btn.addEventListener('click', () => {
      setDashboardRole(btn.dataset.dashboardRole);
      syncDrawerRole(btn.dataset.dashboardRole);
      closeDrawer();
    });
  });

  // Patch setDashboardRole to also sync drawer
  const _origSetRole = setDashboardRole;
  window.setDashboardRole = role => {
    _origSetRole(role);
    syncDrawerRole(role);
  };
  // Re-bind header role buttons with the patched version
  document.querySelectorAll('[data-dashboard-role]').forEach(btn => {
    btn.onclick = null;
    btn.addEventListener('click', () => window.setDashboardRole(btn.dataset.dashboardRole));
  });

  // Initial role activation
  setDashboardRole(currentRole);
  syncDrawerRole(currentRole);

  // Restore exact dashboard view (role + active tab) after returning from 404
  try {
    const raw = sessionStorage.getItem('stackly_back_state');
    if (raw) {
      const st = JSON.parse(raw);
      if (st && st.ts && (Date.now() - st.ts) < 300000) {
        const r = st.role === 'admin' ? 'admin' : 'client';
        setDashboardRole(r);
        syncDrawerRole(r);
        if (r === 'admin' && st.admTab) showAdmTab(st.admTab);
        if (r === 'client' && st.cpTab) showCpTab(st.cpTab);

        const targetScroll = typeof st.scroll === 'number' ? st.scroll : 0;
        const restoreScroll = () => window.scrollTo(0, targetScroll);
        requestAnimationFrame(restoreScroll);
        setTimeout(restoreScroll, 120);
        setTimeout(restoreScroll, 400);
        window.addEventListener('load', restoreScroll, { once: true });
      }
      sessionStorage.removeItem('stackly_back_state');
    }
  } catch (e) {}
}

// Clear stale restore state if the dashboard is restored from the back/forward cache
window.addEventListener('pageshow', function (e) {
  if (e.persisted) {
    try { sessionStorage.removeItem('stackly_back_state'); } catch (err) {}
  }
});

new_hero_and_overview = """<!-- ========================================================================= -->
<!-- ======================= 2. ADMIN ROLE DASHBOARD ======================== -->
<!-- ========================================================================= -->
<div id="adminDash" class="adm-suite d-none">

  <!-- Executive Hero Command Banner (Matching Website Hero DNA) -->
  <div class="adm-hero">
    <div class="container-fluid px-lg-5">
      <div class="d-flex justify-content-between align-items-start align-items-lg-center flex-column flex-lg-row gap-4">
        <div>
          <div class="d-flex align-items-center gap-2 mb-2 flex-wrap">
            <span class="adm-pill-tag"><i class="bi bi-shield-check me-1"></i>Agency Director</span>
            <span class="adm-live-badge"><span class="cp-pulse"></span>38 Client Retainers Live</span>
            <span class="adm-pill-tag"><i class="bi bi-activity me-1"></i>100% Tracking Health</span>
            <span class="adm-pill-tag"><i class="bi bi-lightning-charge-fill me-1 text-warning"></i>$1.42M Media Managed</span>
          </div>
          <h1 class="adm-title">Agency Command Suite</h1>
          <p class="adm-sub mb-0">Portfolio governance across 38 client brands, 4 specialist delivery pods & multi-network revenue attribution.</p>
        </div>
        <div class="d-flex align-items-center gap-2 flex-wrap">
          <button type="button" class="btn btn-pink btn-sm fw-bold" onclick="showAdminToast('Opening New Client Brand onboarding modal...');return false">
            <i class="bi bi-building-add me-1"></i>Onboard Client
          </button>
          <button type="button" class="btn btn-ghost btn-sm fw-bold" onclick="showAdminToast('Exporting Q1 2026 P&L CSV statement...');return false">
            <i class="bi bi-download me-1"></i>Export P&L Report
          </button>
          <button type="button" class="btn btn-cobalt btn-sm fw-bold" onclick="showAdmTab('adm-lab');return false">
            <i class="bi bi-sliders me-1"></i>Growth Simulator
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Executive Pill Sub-Navigation -->
  <div class="adm-nav-bar">
    <div class="container-fluid px-lg-5">
      <div class="adm-tabs-scroll">
        <button type="button" class="adm-tab on" data-admnav="adm-overview">
          <i class="bi bi-grid-fill"></i><span>Executive Bento</span>
        </button>
        <button type="button" class="adm-tab" data-admnav="adm-clients">
          <i class="bi bi-building"></i><span>Client Roster</span><span class="adm-badge">38 Brands</span>
        </button>
        <button type="button" class="adm-tab" data-admnav="adm-pods">
          <i class="bi bi-people-fill"></i><span>Specialist Pods</span><span class="adm-badge">4 Pods</span>
        </button>
        <button type="button" class="adm-tab" data-admnav="adm-channels">
          <i class="bi bi-pie-chart-fill"></i><span>Channels & ROAS</span>
        </button>
        <button type="button" class="adm-tab" data-admnav="adm-lab">
          <i class="bi bi-calculator-fill"></i><span>Growth Simulator</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Admin Main Workspace -->
  <div class="adm-body">
    <div class="container-fluid px-lg-5">

      <!-- ================= 1. OVERVIEW SECTION (EXECUTIVE BENTO) ================= -->
      <section id="adm-overview" class="adm-sec on">

        <!-- Bento Row 1: Asymmetrical 3-Card Spotlight -->
        <div class="row g-4 mb-4">
          <!-- Bento 1: Gross MRR & Milestone Progress -->
          <div class="col-lg-5">
            <div class="adm-card adm-bento-hero">
              <div class="d-flex justify-content-between align-items-center mb-3">
                <span class="tag tag-cobalt"><i class="bi bi-wallet2 me-1"></i>Gross Retainer MRR</span>
                <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1 fw-bold">
                  <i class="bi bi-arrow-up-short"></i>+22.4% Net MoM
                </span>
              </div>
              <div class="adm-bento-hero-val">$384,500<span class="adm-bento-unit">/month</span></div>
              <p class="small text-muted mb-3">Total recurring client agency retainers & media management fees for Q1 2026.</p>
              
              <!-- Milestone Pacing -->
              <div class="p-3 rounded-3 mb-3" style="background:#f4f3ff;border:1px solid #e2e0fb">
                <div class="d-flex justify-content-between small fw-bold mb-1">
                  <span>Q1 Milestone Target ($400,000)</span>
                  <span class="text-primary">96.1% Reached</span>
                </div>
                <div class="progress" style="height:8px;background:#e2e0fb">
                  <div class="progress-bar" style="width:96.1%;background:linear-gradient(90deg, #3B2BF0, #FF4D8D)"></div>
                </div>
              </div>

              <!-- Revenue Split Breakdown -->
              <div class="row g-2 pt-1 border-top">
                <div class="col-6">
                  <small class="text-muted d-block" style="font-size:0.75rem">Fixed Strategic Retainers</small>
                  <b class="fs-6 text-dark">$286,000 <span class="text-muted small" style="font-size:0.7rem">(74%)</span></b>
                </div>
                <div class="col-6">
                  <small class="text-muted d-block" style="font-size:0.75rem">Media Spend Commissions</small>
                  <b class="fs-6 text-dark">$98,500 <span class="text-muted small" style="font-size:0.7rem">(26%)</span></b>
                </div>
              </div>
            </div>
          </div>

          <!-- Bento 2: 38-Brand Portfolio Health Matrix -->
          <div class="col-lg-4">
            <div class="adm-card">
              <div class="d-flex justify-content-between align-items-center mb-3">
                <h5 class="adm-card-title mb-0">Portfolio Health Matrix</h5>
                <span class="adm-badge">38 Brands</span>
              </div>
              <p class="adm-card-sub mb-3">Live account status across all active enterprise & mid-market retainers.</p>

              <div class="d-flex flex-column gap-2 mb-3">
                <div class="p-2 rounded-3 d-flex align-items-center justify-content-between" style="background:rgba(47,214,160,0.1);border:1px solid rgba(47,214,160,0.25)">
                  <div class="d-flex align-items-center gap-2">
                    <span style="width:10px;height:10px;background:#2FD6A0;border-radius:50%"></span>
                    <span class="small fw-bold">Scaling Brands (ROAS &gt; 4.0x)</span>
                  </div>
                  <b class="text-success small">32 Brands</b>
                </div>

                <div class="p-2 rounded-3 d-flex align-items-center justify-content-between" style="background:rgba(59,43,240,0.08);border:1px solid rgba(59,43,240,0.2)">
                  <div class="d-flex align-items-center gap-2">
                    <span style="width:10px;height:10px;background:#3B2BF0;border-radius:50%"></span>
                    <span class="small fw-bold">30-Day Onboarding Sprints</span>
                  </div>
                  <b class="text-primary small">4 Brands</b>
                </div>

                <div class="p-2 rounded-3 d-flex align-items-center justify-content-between" style="background:rgba(255,77,141,0.08);border:1px solid rgba(255,77,141,0.2)">
                  <div class="d-flex align-items-center gap-2">
                    <span style="width:10px;height:10px;background:#FF4D8D;border-radius:50%"></span>
                    <span class="small fw-bold">Creative Refresh / Review</span>
                  </div>
                  <b class="text-danger small">2 Brands</b>
                </div>
              </div>

              <div class="d-flex justify-content-between align-items-center pt-2 border-top small text-muted">
                <span>Annual Retention: <b class="text-dark">96.2%</b></span>
                <button class="btn btn-sm btn-outline-primary py-1 px-2" style="font-size:0.78rem" onclick="showAdmTab('adm-clients')">
                  Roster &rarr;
                </button>
              </div>
            </div>
          </div>

          <!-- Bento 3: Specialist Headcount & Utilization -->
          <div class="col-lg-3">
            <div class="adm-card">
              <div class="small fw-bold text-muted text-uppercase mb-1" style="letter-spacing:0.05em">Agency Staffing</div>
              <div class="d-flex align-items-baseline gap-2 mb-2">
                <span class="adm-bento-stat text-primary">84%</span>
                <span class="small fw-bold text-muted">Capacity</span>
              </div>
              <p class="small text-muted mb-3">32 of 38 specialist allocations active across 4 dedicated pods.</p>

              <div class="d-flex flex-column gap-2 mb-3">
                <div class="d-flex justify-content-between small fw-bold">
                  <span class="text-muted">Pod Alpha (SaaS)</span>
                  <span class="text-success">88%</span>
                </div>
                <div class="d-flex justify-content-between small fw-bold">
                  <span class="text-muted">Pod Bravo (DTC)</span>
                  <span class="text-warning">94%</span>
                </div>
                <div class="d-flex justify-content-between small fw-bold">
                  <span class="text-muted">Pod Delta (Health)</span>
                  <span class="text-success">76%</span>
                </div>
                <div class="d-flex justify-content-between small fw-bold">
                  <span class="text-muted">Pod Enterprise</span>
                  <span class="text-success">82%</span>
                </div>
              </div>

              <button type="button" class="btn btn-sm btn-outline-secondary w-100" style="font-size:0.78rem;font-weight:700" onclick="showAdmTab('adm-pods')">
                <i class="bi bi-people me-1"></i>Manage 4 Pods
              </button>
            </div>
          </div>
        </div>

        <!-- Bento Row 2: Dual Core Operations (Revenue/Spend Curve + Channel Attribution) -->
        <div class="row g-4 mb-4">
          <!-- Left: Revenue & Managed Ad Spend Chart -->
          <div class="col-lg-8">
            <div class="adm-card">
              <div class="d-flex justify-content-between align-items-start mb-3 flex-wrap gap-2">
                <div>
                  <h5 class="adm-card-title mb-1">Agency Revenue vs Managed Ad Spend Flow</h5>
                  <p class="adm-card-sub mb-0">Monthly retainer fees & ad spend velocity across all 38 client brands</p>
                </div>
                <div class="adm-pill-group">
                  <button type="button" class="adm-pill on">Q1 2026</button>
                  <button type="button" class="adm-pill">Trailing 6M</button>
                  <button type="button" class="adm-pill">1 Year</button>
                </div>
              </div>

              <!-- SVG Area Flow Chart -->
              <div class="position-relative">
                <svg viewBox="0 0 650 200" class="w-100" style="overflow:visible;height:auto">
                  <defs>
                    <linearGradient id="admg1" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0" stop-color="#3B2BF0" stop-opacity=".25"/>
                      <stop offset="1" stop-color="#3B2BF0" stop-opacity="0"/>
                    </linearGradient>
                    <linearGradient id="admg2" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0" stop-color="#FF4D8D" stop-opacity=".2"/>
                      <stop offset="1" stop-color="#FF4D8D" stop-opacity="0"/>
                    </linearGradient>
                  </defs>
                  <line x1="0" x2="650" y1="35" y2="35" stroke="#ece9ff" stroke-dasharray="4 4"/>
                  <line x1="0" x2="650" y1="85" y2="85" stroke="#ece9ff" stroke-dasharray="4 4"/>
                  <line x1="0" x2="650" y1="135" y2="135" stroke="#ece9ff" stroke-dasharray="4 4"/>
                  <line x1="0" x2="650" y1="185" y2="185" stroke="#ece9ff" stroke-dasharray="4 4"/>
                  
                  <!-- Spend Curve -->
                  <path d="M0,160 C100,150 180,120 280,105 S450,75 650,25 L650,200 L0,200Z" fill="url(#admg2)"/>
                  <path d="M0,160 C100,150 180,120 280,105 S450,75 650,25" fill="none" stroke="#FF4D8D" stroke-width="3" stroke-linecap="round"/>

                  <!-- Revenue Curve -->
                  <path d="M0,175 C100,165 180,140 280,130 S450,95 650,55 L650,200 L0,200Z" fill="url(#admg1)"/>
                  <path d="M0,175 C100,165 180,140 280,130 S450,95 650,55" fill="none" stroke="#3B2BF0" stroke-width="3" stroke-linecap="round"/>

                  <circle cx="280" cy="130" r="5" fill="#3B2BF0" stroke="#fff" stroke-width="2"/>
                  <circle cx="650" cy="55" r="5" fill="#3B2BF0" stroke="#fff" stroke-width="2"/>
                  <circle cx="280" cy="105" r="5" fill="#FF4D8D" stroke="#fff" stroke-width="2"/>
                  <circle cx="650" cy="25" r="5" fill="#FF4D8D" stroke="#fff" stroke-width="2"/>

                  <text x="5" y="198" font-size="11" fill="#9b98c9">Jan 2026</text>
                  <text x="250" y="198" font-size="11" fill="#9b98c9">Feb 2026</text>
                  <text x="580" y="198" font-size="11" fill="#9b98c9">Mar 2026</text>
                </svg>
              </div>

              <div class="d-flex justify-content-between align-items-center mt-3 pt-3 border-top flex-wrap gap-2">
                <div class="d-flex align-items-center gap-3">
                  <span class="small fw-bold d-flex align-items-center gap-2"><span style="width:12px;height:12px;background:#3B2BF0;border-radius:3px"></span>Retainer Revenue ($384.5k)</span>
                  <span class="small fw-bold d-flex align-items-center gap-2"><span style="width:12px;height:12px;background:#FF4D8D;border-radius:3px"></span>Ad Spend Paced ($1.42M)</span>
                </div>
                <small class="text-success fw-bold"><i class="bi bi-shield-check me-1"></i>100% Tracking Verified</small>
              </div>
            </div>
          </div>

          <!-- Right: Channel Attribution Matrix -->
          <div class="col-lg-4">
            <div class="adm-card h-100">
              <h5 class="adm-card-title mb-1">Attributed Channel Mix</h5>
              <p class="adm-card-sub mb-3">Share of closed leads & revenue by channel</p>

              <div class="d-flex flex-column gap-3">
                <div>
                  <div class="d-flex justify-content-between small fw-bold mb-1">
                    <span><i class="bi bi-search text-primary me-2"></i>Organic Search (SEO)</span>
                    <span>36% &middot; $138.4k</span>
                  </div>
                  <div class="prog" style="height:8px"><div style="width:36%;background:#3B2BF0"></div></div>
                </div>

                <div>
                  <div class="d-flex justify-content-between small fw-bold mb-1">
                    <span><i class="bi bi-megaphone text-danger me-2"></i>Paid Search (Google)</span>
                    <span>31% &middot; $119.2k</span>
                  </div>
                  <div class="prog" style="height:8px"><div style="width:31%;background:#FF4D8D"></div></div>
                </div>

                <div>
                  <div class="d-flex justify-content-between small fw-bold mb-1">
                    <span><i class="bi bi-share text-success me-2"></i>Paid Social (Meta & TikTok)</span>
                    <span>22% &middot; $84.6k</span>
                  </div>
                  <div class="prog" style="height:8px"><div style="width:22%;background:#2FD6A0"></div></div>
                </div>

                <div>
                  <div class="d-flex justify-content-between small fw-bold mb-1">
                    <span><i class="bi bi-envelope-paper text-warning me-2"></i>Email Lifecycle CRM</span>
                    <span>11% &middot; $42.3k</span>
                  </div>
                  <div class="prog" style="height:8px"><div style="width:11%;background:#f59e0b"></div></div>
                </div>
              </div>

              <div class="mt-4 p-3 rounded-3" style="background:#fafafe;border:1px solid #ece9ff">
                <div class="d-flex align-items-center gap-2 mb-1">
                  <i class="bi bi-lightning-charge-fill text-primary"></i>
                  <b class="small">Blended Client ROAS: 4.42x</b>
                </div>
                <small class="text-muted d-block" style="font-size:0.75rem">+0.62 pts above 3.80x industry benchmark.</small>
              </div>
            </div>
          </div>
        </div>

        <!-- Bento Row 3: Live Brand Operations & Real-Time Event Audit Feed -->
        <div class="row g-4 mb-4">
          <!-- Left: High Velocity Client Campaigns -->
          <div class="col-lg-7">
            <div class="adm-card">
              <div class="d-flex justify-content-between align-items-center mb-3">
                <h5 class="adm-card-title mb-0">High-Velocity Client Campaigns</h5>
                <button class="btn btn-sm btn-outline-primary" onclick="showAdmTab('adm-clients')">View All 38</button>
              </div>
              <div class="d-flex flex-column gap-2">
                <div class="adm-client-mini-card">
                  <div class="d-flex align-items-center gap-3">
                    <div class="adm-client-icon" style="background:rgba(59,43,240,.1);color:#3B2BF0"><i class="bi bi-lightning-fill"></i></div>
                    <div>
                      <div class="fw-bold">Voltrix (B2B SaaS)</div>
                      <small class="muted">Rhea Nair &middot; Pod Alpha &middot; 4 Campaigns Live</small>
                    </div>
                  </div>
                  <div class="text-end">
                    <div class="fw-bold text-success">+18.9% Leads</div>
                    <small class="muted">$19.5k spend &middot; 4.8x ROAS</small>
                  </div>
                </div>

                <div class="adm-client-mini-card">
                  <div class="d-flex align-items-center gap-3">
                    <div class="adm-client-icon" style="background:rgba(47,214,160,.14);color:#0a8a5f"><i class="bi bi-house-door-fill"></i></div>
                    <div>
                      <div class="fw-bold">Homestead (Real Estate)</div>
                      <small class="muted">Daniel Park &middot; Pod Delta &middot; Scaling</small>
                    </div>
                  </div>
                  <div class="text-end">
                    <div class="fw-bold text-success">+212% Pipeline</div>
                    <small class="muted">$28.0k spend &middot; 4.2x ROAS</small>
                  </div>
                </div>

                <div class="adm-client-mini-card">
                  <div class="d-flex align-items-center gap-3">
                    <div class="adm-client-icon" style="background:rgba(255,77,141,.12);color:#FF4D8D"><i class="bi bi-bag-check-fill"></i></div>
                    <div>
                      <div class="fw-bold">Craftly (DTC Retail)</div>
                      <small class="muted">Meera Joshi &middot; Pod Bravo &middot; Shopping Ads</small>
                    </div>
                  </div>
                  <div class="text-end">
                    <div class="fw-bold text-success">4.8x Return</div>
                    <small class="muted">$45.0k spend &middot; Active</small>
                  </div>
                </div>

                <div class="adm-client-mini-card">
                  <div class="d-flex align-items-center gap-3">
                    <div class="adm-client-icon" style="background:rgba(59,43,240,.1);color:#3B2BF0"><i class="bi bi-heart-pulse-fill"></i></div>
                    <div>
                      <div class="fw-bold">Vitalis (Health Tech)</div>
                      <small class="muted">Dr. Samuel Ross &middot; Pod Delta &middot; Lead Gen</small>
                    </div>
                  </div>
                  <div class="text-end">
                    <div class="fw-bold text-success">+31% Conv</div>
                    <small class="muted">$22.5k spend &middot; 4.6x ROAS</small>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right: Real-Time Agency Event Stream (Live Audit) -->
          <div class="col-lg-5">
            <div class="adm-card">
              <div class="d-flex justify-content-between align-items-center mb-3">
                <h5 class="adm-card-title mb-0">Live Agency Operations Stream</h5>
                <span class="badge bg-success-subtle text-success border border-success-subtle"><span class="cp-pulse" style="width:6px;height:6px"></span>Real-Time</span>
              </div>
              <div class="d-flex flex-column gap-3">
                <div class="d-flex align-items-start gap-2 pb-2 border-bottom">
                  <div class="audit-icon blue"><i class="bi bi-graph-up-arrow"></i></div>
                  <div class="lh-sm">
                    <div class="small fw-bold">Voltrix Lead Surge (+34 MQLs)</div>
                    <small class="text-muted">Pod Alpha Google Ads campaign hit 4.8x ROAS</small>
                    <div class="text-muted" style="font-size:0.7rem">12 mins ago</div>
                  </div>
                </div>

                <div class="d-flex align-items-start gap-2 pb-2 border-bottom">
                  <div class="audit-icon green"><i class="bi bi-shield-check"></i></div>
                  <div class="lh-sm">
                    <div class="small fw-bold">Vitalis Meta CAPI Tracking Verified</div>
                    <small class="text-muted">100% match quality on server-side checkout events</small>
                    <div class="text-muted" style="font-size:0.7rem">45 mins ago</div>
                  </div>
                </div>

                <div class="d-flex align-items-start gap-2 pb-2 border-bottom">
                  <div class="audit-icon blue"><i class="bi bi-cash-stack"></i></div>
                  <div class="lh-sm">
                    <div class="small fw-bold">Homestead Retainer Cleared ($12,000)</div>
                    <small class="text-muted">Automatic invoice payment cleared via Stripe</small>
                    <div class="text-muted" style="font-size:0.7rem">2 hours ago</div>
                  </div>
                </div>

                <div class="d-flex align-items-start gap-2">
                  <div class="audit-icon green"><i class="bi bi-megaphone-fill"></i></div>
                  <div class="lh-sm">
                    <div class="small fw-bold">Pod Bravo Launched TikTok Batch #4</div>
                    <small class="text-muted">Brewline & Craftly ad creatives approved for live flight</small>
                    <div class="text-muted" style="font-size:0.7rem">4 hours ago</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </section>

"""

with open('dashboard.html', 'r', encoding='utf-8') as f:
    orig = f.read()

clients_start = orig.find('<!-- ================= 2. CLIENT ROSTER SECTION ================= -->')
adm_start = orig.find('<!-- ========================================================================= -->\\n<!-- ======================= 2. ADMIN ROLE DASHBOARD ======================== -->')
if adm_start == -1:
    adm_start = orig.find('<!-- ======================= 2. ADMIN ROLE DASHBOARD ======================== -->')

before_adm = orig[:adm_start]
after_overview = orig[clients_start:]

updated = before_adm + new_hero_and_overview + after_overview

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Updated dashboard.html hero & overview successfully!")

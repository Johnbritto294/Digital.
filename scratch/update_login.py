login_code = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Welcome back | Stackly Digital</title><meta name="description" content="Stackly is a digital marketing agency for SEO, paid media, social and analytics.">
<link rel="preconnect" href="https://images.unsplash.com"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
<link href="assets/css/style.css?v=31" rel="stylesheet"></head>
<body>
<div class="auth"><div class="auth-img"><img class="eager" data-img="1551288049-bebda4e38f71" data-w="1200" alt=""><div><p class="quote">"Every lead, every dollar, in one place."</p></div></div>
<div class="auth-form"><form data-form="login" novalidate><div class="auth-head"><a href="index.html" class="auth-brand"><img class="auth-logo" src="logo_green.webp?v=31" alt="Stackly"></a><a href="index.html" class="back-home"><i class="bi bi-arrow-left"></i>Back to home</a></div>

<!-- Role Switcher -->
<div class="role-switch mb-2" role="group" aria-label="Select role">
  <button type="button" class="on" data-role="client"><i class="bi bi-person-circle me-1"></i>Client Partner</button>
  <button type="button" data-role="admin"><i class="bi bi-shield-check me-1"></i>Agency Admin</button>
</div>

<!-- Quick Demo Account Fillers -->
<div class="d-flex gap-2 mb-3">
  <button type="button" class="btn btn-sm btn-outline-primary flex-fill" id="fillClientDemo" style="font-size:0.78rem;font-weight:700;border-radius:10px;padding:.4rem">
    <i class="bi bi-person me-1"></i>Fill Client (Rhea)
  </button>
  <button type="button" class="btn btn-sm btn-outline-danger flex-fill" id="fillAdminDemo" style="font-size:0.78rem;font-weight:700;border-radius:10px;padding:.4rem">
    <i class="bi bi-shield-check me-1"></i>Fill Admin (Alex)
  </button>
</div>

<input type="hidden" name="role" value="client">
<h1 id="authTitle" style="font-size:2.4rem;font-family:'Syne',sans-serif;font-weight:800;letter-spacing:-.03em">Welcome back</h1>
<p id="authSub" class="muted mb-4">Log in to see your campaign results.</p>
<div class="mb-3"><label class="form-label fw-bold small" for="email">Email</label><input id="email" name="email" type="email" class="form-control" required placeholder="name@company.com"></div>
<div class="mb-3"><label class="form-label fw-bold small" for="password">Password</label><input id="password" name="password" type="password" class="form-control" required minlength="6" placeholder="******"></div>
<div class="d-flex justify-content-between mb-3"><div class="form-check"><input class="form-check-input" type="checkbox" id="r" checked><label class="form-check-label small" for="r">Remember me</label></div><a href="404.html" class="small">Forgot password?</a></div>
<button class="btn btn-cobalt btn-lg w-100 mt-2" id="loginBtn" style="font-weight:800">Log in to Dashboard</button>
<p class="mt-4 text-center muted small">New to Stackly? <a href="register.html" class="fw-bold">Create an account</a></p></form></div></div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="assets/js/main.js?v=31"></script></body></html>
"""

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(login_code)
print("Updated login.html successfully!")

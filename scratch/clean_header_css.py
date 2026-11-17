with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = """body.cp-theme{background:#f7f7fb!important;--adm-bg:#f7f7fb;--adm-surface:#fff;--adm-text:#0F0D2E;--adm-muted:#9b98c9;--adm-border:#e8e6f8;--adm-surface-alt:#f0effe;--adm-header-bg:#ffffff}
body.cp-theme .dash-top{background:#fff!important;border-bottom:1px solid #e8e6f8!important;box-shadow:0 2px 16px rgba(59,43,240,.06)!important}
body.cp-theme .dash-top .brand-logo{filter:brightness(0)!important}
body.cp-theme .dash-user{color:#0F0D2E!important}
body.cp-theme .dash-user small{color:#9b98c9!important}
body.cp-theme .role-badge-switch{background:rgba(15,13,46,.08)!important}
body.cp-theme .role-badge-switch button{color:#615f85!important}
body.cp-theme .role-badge-switch button.on{color:#fff!important}"""

replacement = """body.cp-theme{background:#f7f7fb!important;--adm-bg:#f7f7fb;--adm-surface:#fff;--adm-text:#0F0D2E;--adm-muted:#9b98c9;--adm-border:#e8e6f8;--adm-surface-alt:#f0effe}"""

if target in css:
    css = css.replace(target, replacement)
    print("Cleaned up cp-theme header overrides successfully!")
else:
    # try normalized line endings
    css_norm = css.replace('\r\n', '\n')
    target_norm = target.replace('\r\n', '\n')
    if target_norm in css_norm:
        css = css_norm.replace(target_norm, replacement)
        print("Cleaned up cp-theme header overrides with normalized endings!")
    else:
        print("Target not found directly, checking...")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

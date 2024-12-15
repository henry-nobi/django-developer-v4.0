from django.shortcuts import render

# Authentication Views
def auth_login(request):
    return render(request, 'pages/auth-login.html')

def auth_register(request):
    return render(request, 'pages/auth-register.html')

def auth_recoverpw(request):
    return render(request, 'pages/auth-recoverpw.html')

def auth_lock_screen(request):
    return render(request, 'pages/auth-lock-screen.html')

def auth_confirm_mail(request):
    return render(request, 'pages/auth-confirm-mail.html')

def email_verification(request):
    return render(request, 'pages/email-verification.html')

def auth_logout(request):
    return render(request, 'pages/auth-logout.html')

# Error Pages
def error_404(request):
    return render(request, 'pages/error-404.html')

def error_500(request):
    return render(request, 'pages/error-500.html')

def error_503(request):
    return render(request, 'pages/error-503.html')

def error_429(request):
    return render(request, 'pages/error-429.html')

def offline_page(request):
    return render(request, 'pages/offline-page.html')

# Utility Pages
def pages_starter(request):
    return render(request, 'pages/pages-starter.html')

def pages_profile(request):
    return render(request, 'pages/pages-profile.html')

def pages_pricing(request):
    return render(request, 'pages/pages-pricing.html')

def pages_timeline(request):
    return render(request, 'pages/pages-timeline.html')

def pages_invoice(request):
    return render(request, 'pages/pages-invoice.html')

def pages_faqs(request):
    return render(request, 'pages/pages-faqs.html')

def pages_gallery(request):
    return render(request, 'pages/pages-gallery.html')

def pages_maintenance(request):
    return render(request, 'pages/pages-maintenance.html')

def pages_coming_soon(request):
    return render(request, 'pages/pages-coming-soon.html')

# UI Component Views
def ui_accordions(request):
    return render(request, 'pages/ui-accordions.html')

def ui_alerts(request):
    return render(request, 'pages/ui-alerts.html')

def ui_badges(request):
    return render(request, 'pages/ui-badges.html')

def ui_breadcrumb(request):
    return render(request, 'pages/ui-breadcrumb.html')

def ui_buttons(request):
    return render(request, 'pages/ui-buttons.html')

def ui_cards(request):
    return render(request, 'pages/ui-cards.html')

def ui_collapse(request):
    return render(request, 'pages/ui-collapse.html')

def ui_dropdowns(request):
    return render(request, 'pages/ui-dropdowns.html')

def ui_video(request):
    return render(request, 'pages/ui-video.html')

def ui_grid(request):
    return render(request, 'pages/ui-grid.html')

def ui_images(request):
    return render(request, 'pages/ui-images.html')

def ui_list(request):
    return render(request, 'pages/ui-list.html')

def ui_modals(request):
    return render(request, 'pages/ui-modals.html')

def ui_placeholders(request):
    return render(request, 'pages/ui-placeholders.html')

def ui_pagination(request):
    return render(request, 'pages/ui-pagination.html')

def ui_popovers(request):
    return render(request, 'pages/ui-popovers.html')

def ui_progress(request):
    return render(request, 'pages/ui-progress.html')

def ui_scrollspy(request):
    return render(request, 'pages/ui-scrollspy.html')

def ui_spinners(request):
    return render(request, 'pages/ui-spinners.html')

def ui_tabs(request):
    return render(request, 'pages/ui-tabs.html')

def ui_tooltips(request):
    return render(request, 'pages/ui-tooltips.html')

def ui_typography(request):
    return render(request, 'pages/ui-typography.html')

# Extended UI Views
def extended_carousel(request):
    return render(request, 'pages/extended-carousel.html')

def extended_notifications(request):
    return render(request, 'pages/extended-notifications.html')

def extended_offcanvas(request):
    return render(request, 'pages/extended-offcanvas.html')

def extended_range_slider(request):
    return render(request, 'pages/extended-range-slider.html')

def extended_scrollbar(request):
    return render(request, 'pages/extended-scrollbar.html')

def extended_scrollspy(request):
    return render(request, 'pages/extended-scrollspy.html')

# Icons Views
def icons_feather(request):
    return render(request, 'pages/icons-feather.html')

def icons_mdi(request):
    return render(request, 'pages/icons-mdi.html')

# Forms Views
def forms_elements(request):
    return render(request, 'pages/forms-elements.html')

def forms_validation(request):
    return render(request, 'pages/forms-validation.html')

def forms_quilljs(request):
    return render(request, 'pages/forms-quilljs.html')

def forms_pickers(request):
    return render(request, 'pages/forms-pickers.html')

def forms_advanced(request):
    return render(request, 'pages/forms-advanced.html')

# Tables Views
def tables_basic(request):
    return render(request, 'pages/tables-basic.html')

def tables_datatables(request):
    return render(request, 'pages/tables-datatables.html')

# Charts Views
def charts_line(request):
    return render(request, 'pages/charts-line.html')

def charts_area(request):
    return render(request, 'pages/charts-area.html')

def charts_column(request):
    return render(request, 'pages/charts-column.html')

def charts_bar(request):
    return render(request, 'pages/charts-bar.html')

def charts_mixed(request):
    return render(request, 'pages/charts-mixed.html')

def charts_timeline(request):
    return render(request, 'pages/charts-timeline.html')

def charts_flot(request):
    return render(request, 'pages/charts-flot.html')

def charts_morris(request):
    return render(request, 'pages/charts-morris.html')

def charts_sparklines(request):
    return render(request, 'pages/charts-sparklines.html')

def charts_rangearea(request):
    return render(request, 'pages/charts-rangearea.html')

def charts_funnel(request):
    return render(request, 'pages/charts-funnel.html')

def charts_candlestick(request):
    return render(request, 'pages/charts-candlestick.html')

def charts_boxplot(request):
    return render(request, 'pages/charts-boxplot.html')

def charts_bubble(request):
    return render(request, 'pages/charts-bubble.html')

def charts_scatter(request):
    return render(request, 'pages/charts-scatter.html')

def charts_heatmap(request):
    return render(request, 'pages/charts-heatmap.html')

def charts_treemap(request):
    return render(request, 'pages/charts-treemap.html')

def charts_pie(request):
    return render(request, 'pages/charts-pie.html')

def charts_radialbar(request):
    return render(request, 'pages/charts-radialbar.html')

def charts_radar(request):
    return render(request, 'pages/charts-radar.html')

def charts_polararea(request):
    return render(request, 'pages/charts-polararea.html')

# Widgets
def widgets(request):
    return render(request, 'pages/widgets.html')

# UI Component Views
def ui_carousel(request):
    return render(request, 'pages/ui-carousel.html')

def ui_general(request):
    return render(request, 'pages/ui-general.html')

def ui_offcanvas(request):
    return render(request, 'pages/ui-offcanvas.html')

# Index Views
def index_sidebar_light_rtl(request):
    return render(request, 'pages/index-sidebar-light-rtl.html')

def index_sidebar_light(request):
    return render(request, 'pages/index-sidebar-light.html')

def index_sidebar_rtl(request):
    return render(request, 'pages/index-sidebar-rtl.html')

def index(request):
    return render(request, 'pages/index.html')

def landing(request):
    return render(request, 'pages/landing.html')

def preview(request):
    return render(request, 'pages/preview.html')

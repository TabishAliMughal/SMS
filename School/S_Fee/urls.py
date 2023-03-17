from django.urls import path
from School.S_Fee import collectfeeviews, createfeeviews, feetypeviews, generatevouchers, views

app_name = 'Fee'

urlpatterns = [
    # List
    path('due/list/',views.ManageDueFeeView,name='due_fee_list'),
    path('due/list/<_from>/<type>/<message>/',views.ManageDueFeeView,name='due_fee_list'),
    path('due/list/<_from>/<type>/<message>/<added>/<not_added>/',views.ManageDueFeeView,name='due_fee_list'),
    path('due/class/',views.ManageDueFeeClassView,name='due_fee_class'),
    # Collect
    path('due/collect/',collectfeeviews.ManageFeeCollectView,name='fee_collect'),
    path('due/<pk>/collect/',collectfeeviews.ManageStudentFeeCollectView,name='student_due_fee_collect'),
    path('due/<pk>/collect/bulk/',collectfeeviews.ManageStudentBulkFeeCollectView,name='student_due_fee_collect_bulk'),
    # Receipt
    path('due/collect/receipt/<fee>',collectfeeviews.ManageCreateReceiptView,name='fee_receipt'),
    # Create
    path('type/create/',feetypeviews.ManageFeeTypesCreateView,name='fee_type_create'),
    path('type/list/',feetypeviews.ManageFeeTypesListView,name='fee_type_list'),
    path('due/create/',createfeeviews.ManageCreateFeeView,name='due_fee_create'),
    path('due/create/student/',createfeeviews.ManageCreateStudentFeeView,name='student_due_fee_create'),
    path('due/create/class/',createfeeviews.ManageCreateClassFeeView,name='class_due_fee_create'),
    path('due/create/selected/classes',createfeeviews.ManageCreateSelectedClassesFeeView,name='selected_classes_due_fee_create'),
    path('due/create/school/',createfeeviews.ManageCreateSchoolFeeView,name='school_due_fee_create'),
    # Vouchers
    path('vouchers/generate/',generatevouchers.ManageFeeVouchersView,name='fee_vouchers'),
    path('vouchers/generate/<student>',generatevouchers.ManageFeeGenerateVouchersView,name='generate_fee_vouchers'),
    path('vouchers/create/student/',generatevouchers.ManageCreateStudentFeeVoucherView,name='student_fee_voucher_create'),
    path('vouchers/create/class/',generatevouchers.ManageCreateClassFeeVoucherView,name='class_fee_voucher_create'),
    path('vouchers/create/school/',generatevouchers.ManageCreateSchoolFeeVoucherView,name='school_fee_voucher_create'),
    path('vouchers/create/selected/classes',generatevouchers.ManageCreateSelectedClassesFeeVoucherView,name='selected_classes_fee_voucher_create'),

]
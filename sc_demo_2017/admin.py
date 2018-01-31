from django.contrib import admin

# Register your models here.
class NVDIMMModelAdmin(admin.ModelAdmin):
    list_display = ["bw","lat","iops"]
    search_fields = list_display
from .models import NVDIMM
admin.site.register(NVDIMM,NVDIMMModelAdmin)


class NVMEModelAdmin(admin.ModelAdmin):
    list_display = ["bw","lat","iops"]
    search_fields = list_display
from .models import NVME
admin.site.register(NVME,NVMEModelAdmin)

class NVDIMMREADModelAdmin(admin.ModelAdmin):
    list_display = ["bw","lat","iops"]
    search_fields = list_display
from .models import NVDIMM_READ
admin.site.register(NVDIMM_READ,NVDIMMREADModelAdmin)

class NVMEREADModelAdmin(admin.ModelAdmin):
    list_display = ["bw","lat","iops"]
    search_fields = list_display
from .models import NVME_READ
admin.site.register(NVME_READ,NVMEREADModelAdmin)

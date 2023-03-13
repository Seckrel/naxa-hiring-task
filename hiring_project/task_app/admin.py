from django.contrib import admin
from .models import (Province, District, Municipality, Donor, ExecutingAgency,
                     ImplementingPartner, CounterpartMinistry, Sector, TypeOfAssistance,
                     Project, Agreement, CommitmentDisbursement)


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('type_of_assistance', 'executing_agency',
                         'implementing_partner', 'project_sector')


admin.site.register(Project, ProjectAdmin)

admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Donor)
admin.site.register(ExecutingAgency)
admin.site.register(ImplementingPartner)
admin.site.register(CounterpartMinistry)
admin.site.register(Sector)
admin.site.register(TypeOfAssistance)
admin.site.register(Agreement)
admin.site.register(CommitmentDisbursement)
